from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.conversation import Conversation, Message, Feedback
import logging

conversation_bp = Blueprint('conversation', __name__)
logger = logging.getLogger(__name__)

@conversation_bp.route('/conversations', methods=['GET'])
def get_conversations():
    """Lista conversas (opcionalmente filtradas por usuário)"""
    try:
        user_id = request.args.get('user_id', type=int)
        
        if user_id:
            conversations = Conversation.query.filter_by(user_id=user_id).order_by(Conversation.updated_at.desc()).all()
        else:
            conversations = Conversation.query.order_by(Conversation.updated_at.desc()).all()
        
        return jsonify([conv.to_dict() for conv in conversations]), 200
    except Exception as e:
        logger.error(f"Erro ao buscar conversas: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations', methods=['POST'])
def create_conversation():
    """Cria uma nova conversa"""
    try:
        data = request.get_json()
        
        if not data or not data.get('user_id'):
            return jsonify({'error': 'user_id é obrigatório'}), 400
        
        conversation = Conversation(
            user_id=data['user_id'],
            title=data.get('title', 'Nova Conversa'),
            metadata_dict=data.get('metadata', {})
        )
        
        db.session.add(conversation)
        db.session.commit()
        
        logger.info(f"Conversa criada: {conversation.id}")
        return jsonify(conversation.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao criar conversa: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """Busca uma conversa específica com suas mensagens"""
    try:
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        # Incluir mensagens na resposta
        result = conversation.to_dict()
        result['messages'] = [msg.to_dict() for msg in conversation.messages]
        
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Erro ao buscar conversa {conversation_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['PUT'])
def update_conversation(conversation_id):
    """Atualiza uma conversa"""
    try:
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        if 'title' in data:
            conversation.title = data['title']
        
        if 'metadata' in data:
            conversation.set_metadata(data['metadata'])
        
        if 'is_active' in data:
            conversation.is_active = data['is_active']
        
        db.session.commit()
        
        logger.info(f"Conversa atualizada: {conversation.id}")
        return jsonify(conversation.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao atualizar conversa {conversation_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['DELETE'])
def delete_conversation(conversation_id):
    """Remove uma conversa"""
    try:
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        db.session.delete(conversation)
        db.session.commit()
        
        logger.info(f"Conversa removida: {conversation_id}")
        return jsonify({'message': 'Conversa removida com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao remover conversa {conversation_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>/messages', methods=['POST'])
def add_message():
    """Adiciona uma mensagem à conversa"""
    try:
        conversation_id = request.view_args['conversation_id']
        data = request.get_json()
        
        if not data or not data.get('role') or not data.get('content'):
            return jsonify({'error': 'role e content são obrigatórios'}), 400
        
        # Verificar se conversa existe
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        message = Message(
            conversation_id=conversation_id,
            role=data['role'],
            content=data['content'],
            tokens=data.get('tokens', 0),
            metadata_dict=data.get('metadata', {})
        )
        
        db.session.add(message)
        db.session.commit()
        
        logger.info(f"Mensagem adicionada à conversa {conversation_id}")
        return jsonify(message.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao adicionar mensagem: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/messages/<int:message_id>/feedback', methods=['POST'])
def add_feedback():
    """Adiciona feedback a uma mensagem"""
    try:
        message_id = request.view_args['message_id']
        data = request.get_json()
        
        if not data or not data.get('rating'):
            return jsonify({'error': 'rating é obrigatório'}), 400
        
        rating = data['rating']
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({'error': 'rating deve ser um inteiro entre 1 e 5'}), 400
        
        # Verificar se mensagem existe
        message = Message.query.get(message_id)
        if not message:
            return jsonify({'error': 'Mensagem não encontrada'}), 404
        
        feedback = Feedback(
            message_id=message_id,
            rating=rating,
            comment=data.get('comment')
        )
        
        db.session.add(feedback)
        db.session.commit()
        
        logger.info(f"Feedback adicionado à mensagem {message_id}")
        return jsonify(feedback.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao adicionar feedback: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

