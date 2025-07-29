from flask import Blueprint, request, jsonify, Response, stream_template
from flask_cors import cross_origin
from src.models.user import db, User
from src.models.conversation import Conversation, Message, Feedback
from src.services.ai_service import ai_service
from datetime import datetime
import json
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Blueprint para rotas de IA
ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai/generate', methods=['POST'])
@cross_origin()
def generate_response():
    """
    Gera resposta da IA para uma mensagem
    
    Body:
        conversation_id (int): ID da conversa
        message (str): Mensagem do usuário
        user_id (int): ID do usuário
        config (dict, opcional): Configurações de geração
    
    Returns:
        JSON: Resposta da IA com metadados
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
        
        conversation_id = data.get('conversation_id')
        user_message = data.get('message')
        user_id = data.get('user_id')
        config = data.get('config', {})
        
        # Validações
        if not all([conversation_id, user_message, user_id]):
            return jsonify({'error': 'conversation_id, message e user_id são obrigatórios'}), 400
        
        # Verifica se conversa existe e pertence ao usuário
        conversation = Conversation.query.filter_by(id=conversation_id, user_id=user_id).first()
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada ou não pertence ao usuário'}), 404
        
        # Salva mensagem do usuário
        user_msg = Message(
            conversation_id=conversation_id,
            role='user',
            content=user_message,
            timestamp=datetime.utcnow()
        )
        db.session.add(user_msg)
        db.session.flush()  # Para obter o ID
        
        # Obtém histórico de mensagens para contexto
        messages = Message.query.filter_by(conversation_id=conversation_id)\
            .order_by(Message.timestamp.asc()).all()
        
        # Prepara contexto para a IA
        message_history = []
        for msg in messages:
            message_history.append({
                'role': msg.role,
                'content': msg.content
            })
        
        # Gera resposta da IA
        ai_response = ai_service.generate_response(
            messages=message_history,
            config=config,
            user_id=user_id
        )
        
        if ai_response['success']:
            # Salva resposta da IA
            ai_msg = Message(
                conversation_id=conversation_id,
                role='assistant',
                content=ai_response['response'],
                timestamp=datetime.utcnow(),
                tokens_used=ai_response['metadata'].get('tokens_used'),
                processing_time=ai_response['metadata'].get('processing_time')
            )
            ai_msg.set_metadata(ai_response['metadata'])
            db.session.add(ai_msg)
            
            # Atualiza timestamp da conversa
            conversation.updated_at = datetime.utcnow()
            
            db.session.commit()
            
            logger.info(f"Resposta gerada para conversa {conversation_id}")
            
            return jsonify({
                'user_message': user_msg.to_dict(),
                'ai_response': ai_msg.to_dict(),
                'metadata': ai_response['metadata']
            }), 200
        else:
            # Erro na geração
            db.session.rollback()
            return jsonify({
                'error': 'Erro na geração de resposta',
                'details': ai_response.get('metadata', {})
            }), 500
            
    except Exception as e:
        logger.error(f"Erro na geração de resposta: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/stream', methods=['POST'])
@cross_origin()
def stream_response():
    """
    Gera resposta da IA em streaming
    
    Body:
        conversation_id (int): ID da conversa
        message (str): Mensagem do usuário
        user_id (int): ID do usuário
        config (dict, opcional): Configurações de geração
    
    Returns:
        Stream: Resposta da IA em chunks
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
        
        conversation_id = data.get('conversation_id')
        user_message = data.get('message')
        user_id = data.get('user_id')
        config = data.get('config', {})
        
        # Validações
        if not all([conversation_id, user_message, user_id]):
            return jsonify({'error': 'conversation_id, message e user_id são obrigatórios'}), 400
        
        # Verifica se conversa existe
        conversation = Conversation.query.filter_by(id=conversation_id, user_id=user_id).first()
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        def generate_stream():
            try:
                # Salva mensagem do usuário
                user_msg = Message(
                    conversation_id=conversation_id,
                    role='user',
                    content=user_message,
                    timestamp=datetime.utcnow()
                )
                db.session.add(user_msg)
                db.session.commit()
                
                # Obtém histórico
                messages = Message.query.filter_by(conversation_id=conversation_id)\
                    .order_by(Message.timestamp.asc()).all()
                
                message_history = [{'role': msg.role, 'content': msg.content} for msg in messages]
                
                # Inicia streaming
                full_response = ""
                start_time = datetime.utcnow()
                
                for chunk in ai_service.stream_response(message_history, config):
                    full_response += chunk
                    yield f"data: {json.dumps({'chunk': chunk, 'type': 'content'})}\n\n"
                
                # Salva resposta completa
                processing_time = (datetime.utcnow() - start_time).total_seconds()
                
                ai_msg = Message(
                    conversation_id=conversation_id,
                    role='assistant',
                    content=full_response,
                    timestamp=datetime.utcnow(),
                    processing_time=processing_time
                )
                db.session.add(ai_msg)
                conversation.updated_at = datetime.utcnow()
                db.session.commit()
                
                # Envia evento de finalização
                yield f"data: {json.dumps({'type': 'done', 'message_id': ai_msg.id})}\n\n"
                
            except Exception as e:
                logger.error(f"Erro no streaming: {str(e)}")
                yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"
        
        return Response(
            generate_stream(),
            mimetype='text/event-stream',
            headers={
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Access-Control-Allow-Origin': '*'
            }
        )
        
    except Exception as e:
        logger.error(f"Erro no setup do streaming: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/feedback', methods=['POST'])
@cross_origin()
def submit_feedback():
    """
    Submete feedback sobre uma resposta da IA
    
    Body:
        message_id (int): ID da mensagem
        user_id (int): ID do usuário
        rating (int): Avaliação de 1-5
        comment (str, opcional): Comentário
        feedback_type (str, opcional): Tipo de feedback
    
    Returns:
        JSON: Feedback criado
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
        
        message_id = data.get('message_id')
        user_id = data.get('user_id')
        rating = data.get('rating')
        comment = data.get('comment')
        feedback_type = data.get('feedback_type')
        
        # Validações
        if not all([message_id, user_id]):
            return jsonify({'error': 'message_id e user_id são obrigatórios'}), 400
        
        if rating and (rating < 1 or rating > 5):
            return jsonify({'error': 'rating deve estar entre 1 e 5'}), 400
        
        # Verifica se mensagem existe
        message = Message.query.get(message_id)
        if not message:
            return jsonify({'error': 'Mensagem não encontrada'}), 404
        
        # Verifica se usuário tem acesso à conversa
        conversation = Conversation.query.filter_by(
            id=message.conversation_id, 
            user_id=user_id
        ).first()
        if not conversation:
            return jsonify({'error': 'Acesso negado à conversa'}), 403
        
        # Verifica se já existe feedback do usuário para esta mensagem
        existing_feedback = Feedback.query.filter_by(
            message_id=message_id,
            user_id=user_id
        ).first()
        
        if existing_feedback:
            # Atualiza feedback existente
            if rating:
                existing_feedback.rating = rating
            if comment:
                existing_feedback.comment = comment
            if feedback_type:
                existing_feedback.feedback_type = feedback_type
            
            db.session.commit()
            
            logger.info(f"Feedback atualizado para mensagem {message_id}")
            return jsonify(existing_feedback.to_dict()), 200
        else:
            # Cria novo feedback
            feedback = Feedback(
                message_id=message_id,
                user_id=user_id,
                rating=rating,
                comment=comment,
                feedback_type=feedback_type
            )
            
            db.session.add(feedback)
            db.session.commit()
            
            logger.info(f"Novo feedback criado para mensagem {message_id}")
            return jsonify(feedback.to_dict()), 201
            
    except Exception as e:
        logger.error(f"Erro ao submeter feedback: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/status', methods=['GET'])
@cross_origin()
def get_ai_status():
    """
    Obtém status e informações do modelo de IA
    
    Returns:
        JSON: Status e informações do modelo
    """
    try:
        model_info = ai_service.get_model_info()
        
        return jsonify({
            'status': 'online' if model_info['is_loaded'] else 'demo_mode',
            'model_info': model_info['model_info'],
            'stats': model_info['stats'],
            'config': model_info['config'],
            'timestamp': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao obter status da IA: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/config', methods=['PUT'])
@cross_origin()
def update_ai_config():
    """
    Atualiza configurações do modelo de IA
    
    Body:
        config (dict): Novas configurações
    
    Returns:
        JSON: Configurações atualizadas
    """
    try:
        data = request.get_json()
        
        if not data or 'config' not in data:
            return jsonify({'error': 'Configurações são obrigatórias'}), 400
        
        new_config = data['config']
        
        # Valida configurações
        valid_keys = ['max_new_tokens', 'temperature', 'top_p', 'top_k', 'repetition_penalty', 'do_sample']
        invalid_keys = [key for key in new_config.keys() if key not in valid_keys]
        
        if invalid_keys:
            return jsonify({'error': f'Chaves inválidas: {invalid_keys}'}), 400
        
        # Atualiza configurações
        success = ai_service.update_config(new_config)
        
        if success:
            return jsonify({
                'message': 'Configurações atualizadas com sucesso',
                'config': ai_service.default_config
            }), 200
        else:
            return jsonify({'error': 'Erro ao atualizar configurações'}), 500
            
    except Exception as e:
        logger.error(f"Erro ao atualizar configurações: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/metrics', methods=['GET'])
@cross_origin()
def get_ai_metrics():
    """
    Obtém métricas detalhadas da IA
    
    Query Parameters:
        period (str): Período para métricas - 'day', 'week', 'month' (default: 'day')
    
    Returns:
        JSON: Métricas da IA
    """
    try:
        period = request.args.get('period', 'day')
        
        # Calcula data de início baseada no período
        from datetime import timedelta
        now = datetime.utcnow()
        
        if period == 'week':
            start_date = now - timedelta(weeks=1)
        elif period == 'month':
            start_date = now - timedelta(days=30)
        else:  # day
            start_date = now - timedelta(days=1)
        
        # Métricas de mensagens
        total_messages = Message.query.filter(
            Message.timestamp >= start_date,
            Message.role == 'assistant'
        ).count()
        
        # Métricas de feedback
        feedback_stats = db.session.query(
            db.func.avg(Feedback.rating).label('avg_rating'),
            db.func.count(Feedback.id).label('total_feedback')
        ).join(Message).filter(
            Message.timestamp >= start_date
        ).first()
        
        # Métricas do serviço
        service_stats = ai_service.get_model_info()['stats']
        
        return jsonify({
            'period': period,
            'start_date': start_date.isoformat(),
            'end_date': now.isoformat(),
            'messages_generated': total_messages,
            'average_rating': float(feedback_stats.avg_rating) if feedback_stats.avg_rating else None,
            'total_feedback': feedback_stats.total_feedback,
            'service_stats': service_stats
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao obter métricas: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

