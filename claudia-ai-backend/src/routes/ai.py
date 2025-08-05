from flask import Blueprint, request, jsonify, Response
from src.services.ai_service import ai_service
from src.models.user import db
from src.models.conversation import Conversation, Message
import logging
import json

ai_bp = Blueprint('ai', __name__)
logger = logging.getLogger(__name__)

@ai_bp.route('/ai/generate', methods=['POST'])
def generate_response():
    """Gera resposta da IA para uma mensagem"""
    try:
        data = request.get_json()
        message = data.get('message')
        conversation_id = data.get('conversation_id')
        user_id = data.get('user_id', 1)
        
        if not message:
            return jsonify({'error': 'Mensagem é obrigatória'}), 400
        
        # Buscar contexto da conversa se fornecido
        context = None
        if conversation_id:
            conversation = Conversation.query.get(conversation_id)
            if conversation:
                # Pegar últimas 5 mensagens para contexto
                recent_messages = Message.query.filter_by(
                    conversation_id=conversation_id
                ).order_by(Message.created_at.desc()).limit(5).all()
                
                context = []
                for msg in reversed(recent_messages):
                    context.append({
                        "role": msg.role,
                        "content": msg.content
                    })
        
        # Gerar resposta usando o serviço de IA
        response_data = ai_service.generate_response(
            message=message,
            conversation_id=conversation_id,
            user_id=user_id,
            context=context
        )
        
        # Salvar mensagem do usuário no banco se conversation_id fornecido
        if conversation_id:
            try:
                user_message = Message(
                    conversation_id=conversation_id,
                    role='user',
                    content=message,
                    tokens=len(message.split())
                )
                db.session.add(user_message)
                
                # Salvar resposta da IA
                ai_message = Message(
                    conversation_id=conversation_id,
                    role='assistant',
                    content=response_data['response'],
                    tokens=response_data.get('tokens', 0),
                    metadata_dict={
                        'model': response_data.get('model'),
                        'status': response_data.get('status')
                    }
                )
                db.session.add(ai_message)
                db.session.commit()
                
            except Exception as e:
                logger.error(f"Erro ao salvar mensagens: {e}")
                db.session.rollback()
        
        return jsonify(response_data), 200
        
    except Exception as e:
        logger.error(f"Erro ao gerar resposta: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/stream', methods=['POST'])
def stream_response():
    """Gera resposta da IA em streaming"""
    try:
        data = request.get_json()
        message = data.get('message')
        conversation_id = data.get('conversation_id')
        user_id = data.get('user_id', 1)
        
        if not message:
            return jsonify({'error': 'Mensagem é obrigatória'}), 400
        
        def generate():
            try:
                for chunk in ai_service.stream_response(message, conversation_id, user_id):
                    yield f"data: {json.dumps(chunk)}\n\n"
                
                # Enviar evento de fim
                yield f"data: {json.dumps({'event': 'end'})}\n\n"
                
            except Exception as e:
                logger.error(f"Erro no streaming: {e}")
                yield f"data: {json.dumps({'error': 'Erro no streaming'})}\n\n"
        
        return Response(
            generate(),
            mimetype='text/event-stream',
            headers={
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Access-Control-Allow-Origin': '*'
            }
        )
        
    except Exception as e:
        logger.error(f"Erro ao iniciar streaming: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/status', methods=['GET'])
def get_ai_status():
    """Retorna status do serviço de IA"""
    try:
        status = ai_service.get_model_info()
        return jsonify(status), 200
    except Exception as e:
        logger.error(f"Erro ao obter status da IA: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/models', methods=['GET'])
def get_available_models():
    """Lista modelos de IA disponíveis"""
    try:
        models = {
            'current': ai_service.get_model_info(),
            'available': [
                {
                    'type': 'demo',
                    'name': 'Demo Mode',
                    'description': 'Modo demonstração com respostas pré-definidas',
                    'requirements': 'Nenhum'
                },
                {
                    'type': 'openai',
                    'name': 'OpenAI GPT',
                    'description': 'Modelos GPT da OpenAI (GPT-3.5, GPT-4)',
                    'requirements': 'OPENAI_API_KEY'
                },
                {
                    'type': 'huggingface',
                    'name': 'Hugging Face',
                    'description': 'Modelos open-source do Hugging Face',
                    'requirements': 'transformers, torch'
                },
                {
                    'type': 'llama',
                    'name': 'Llama 3.3 70B Instruct',
                    'description': 'Modelo Llama 3.3 executado localmente',
                    'requirements': 'llama-cpp-python, modelo 3.3 baixado'
                }
            ]
        }
        return jsonify(models), 200
    except Exception as e:
        logger.error(f"Erro ao listar modelos: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/config', methods=['GET'])
def get_ai_config():
    """Retorna configuração atual da IA"""
    try:
        import os
        # AI_MODEL_TYPE é preferencial. AI_MODE permanece por compatibilidade.
        model_type = os.getenv('AI_MODEL_TYPE') or os.getenv('AI_MODE', 'demo')
        config = {
            'model_type': model_type,
            'model_name': os.getenv('AI_MODEL_NAME', 'demo'),
            'openai_configured': bool(os.getenv('OPENAI_API_KEY')),
            'hf_model': os.getenv('HF_MODEL_NAME', 'microsoft/DialoGPT-medium'),
            'llama_path': os.getenv('LLAMA_MODEL_PATH', './models/llama-3.3-70b-instruct'),
            'status': ai_service.get_model_info()
        }
        return jsonify(config), 200
    except Exception as e:
        logger.error(f"Erro ao obter configuração: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/test', methods=['POST'])
def test_ai():
    """Testa o serviço de IA com uma mensagem simples"""
    try:
        test_message = "Olá, você está funcionando?"
        
        response_data = ai_service.generate_response(
            message=test_message,
            conversation_id=None,
            user_id=None
        )
        
        return jsonify({
            'test_message': test_message,
            'ai_response': response_data,
            'test_status': 'success' if response_data.get('status') != 'error' else 'failed',
            'timestamp': response_data.get('timestamp')
        }), 200
        
    except Exception as e:
        logger.error(f"Erro no teste da IA: {str(e)}")
        return jsonify({
            'test_status': 'failed',
            'error': str(e)
        }), 500

