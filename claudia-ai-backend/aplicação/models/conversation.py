from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from src.models.user import db, User
from src.models.conversation import Conversation, Message
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Blueprint para rotas de conversas
conversation_bp = Blueprint('conversation', __name__)

@conversation_bp.route('/conversations', methods=['GET'])
@cross_origin()
def get_conversations():
    """
    Lista todas as conversas do usuário
    
    Query Parameters:
        user_id (int): ID do usuário
        archived (bool): Incluir conversas arquivadas (default: False)
        limit (int): Limite de resultados (default: 50)
        offset (int): Offset para paginação (default: 0)
    
    Returns:
        JSON: Lista de conversas
    """
    try:
        # Parâmetros da query
        user_id = request.args.get('user_id', type=int)
        include_archived = request.args.get('archived', 'false').lower() == 'true'
        limit = request.args.get('limit', 50, type=int)
        offset = request.args.get('offset', 0, type=int)
        
        if not user_id:
            return jsonify({'error': 'user_id é obrigatório'}), 400
        
        # Verifica se usuário existe
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        # Query base
        query = Conversation.query.filter_by(user_id=user_id)
        
        # Filtro de arquivadas
        if not include_archived:
            query = query.filter_by(is_archived=False)
        
        # Ordenação e paginação
        conversations = query.order_by(Conversation.updated_at.desc()).offset(offset).limit(limit).all()
        
        # Converte para dict
        result = [conv.to_dict() for conv in conversations]
        
        return jsonify({
            'conversations': result,
            'total': len(result),
            'offset': offset,
            'limit': limit
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao buscar conversas: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations', methods=['POST'])
@cross_origin()
def create_conversation():
    """
    Cria nova conversa
    
    Body:
        user_id (int): ID do usuário
        title (str, opcional): Título da conversa
        metadata (dict, opcional): Metadados adicionais
    
    Returns:
        JSON: Conversa criada
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
        
        user_id = data.get('user_id')
        title = data.get('title')
        metadata = data.get('metadata', {})
        
        if not user_id:
            return jsonify({'error': 'user_id é obrigatório'}), 400
        
        # Verifica se usuário existe
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        # Cria nova conversa
        conversation = Conversation(
            user_id=user_id,
            title=title or f"Conversa {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )
        
        if metadata:
            conversation.set_metadata(metadata)
        
        db.session.add(conversation)
        db.session.commit()
        
        logger.info(f"Nova conversa criada: {conversation.id} para usuário {user_id}")
        
        return jsonify(conversation.to_dict()), 201
        
    except Exception as e:
        logger.error(f"Erro ao criar conversa: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['GET'])
@cross_origin()
def get_conversation(conversation_id):
    """
    Obtém conversa específica com suas mensagens
    
    Path Parameters:
        conversation_id (int): ID da conversa
    
    Query Parameters:
        include_messages (bool): Incluir mensagens (default: True)
        message_limit (int): Limite de mensagens (default: 100)
    
    Returns:
        JSON: Conversa com mensagens
    """
    try:
        include_messages = request.args.get('include_messages', 'true').lower() == 'true'
        message_limit = request.args.get('message_limit', 100, type=int)
        
        # Busca conversa
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        result = conversation.to_dict()
        
        # Inclui mensagens se solicitado
        if include_messages:
            messages = Message.query.filter_by(conversation_id=conversation_id)\
                .order_by(Message.timestamp.asc())\
                .limit(message_limit).all()
            
            result['messages'] = [msg.to_dict() for msg in messages]
        
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Erro ao buscar conversa {conversation_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['PUT'])
@cross_origin()
def update_conversation(conversation_id):
    """
    Atualiza conversa existente
    
    Path Parameters:
        conversation_id (int): ID da conversa
    
    Body:
        title (str, opcional): Novo título
        is_archived (bool, opcional): Status de arquivamento
        metadata (dict, opcional): Novos metadados
    
    Returns:
        JSON: Conversa atualizada
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
        
        # Busca conversa
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        # Atualiza campos
        if 'title' in data:
            conversation.title = data['title']
        
        if 'is_archived' in data:
            conversation.is_archived = data['is_archived']
        
        if 'metadata' in data:
            conversation.set_metadata(data['metadata'])
        
        conversation.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        logger.info(f"Conversa {conversation_id} atualizada")
        
        return jsonify(conversation.to_dict()), 200
        
    except Exception as e:
        logger.error(f"Erro ao atualizar conversa {conversation_id}: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>', methods=['DELETE'])
@cross_origin()
def delete_conversation(conversation_id):
    """
    Remove conversa e todas suas mensagens
    
    Path Parameters:
        conversation_id (int): ID da conversa
    
    Returns:
        JSON: Confirmação de remoção
    """
    try:
        # Busca conversa
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        # Remove conversa (cascade remove as mensagens)
        db.session.delete(conversation)
        db.session.commit()
        
        logger.info(f"Conversa {conversation_id} removida")
        
        return jsonify({'message': 'Conversa removida com sucesso'}), 200
        
    except Exception as e:
        logger.error(f"Erro ao remover conversa {conversation_id}: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>/messages', methods=['GET'])
@cross_origin()
def get_messages(conversation_id):
    """
    Lista mensagens de uma conversa
    
    Path Parameters:
        conversation_id (int): ID da conversa
    
    Query Parameters:
        limit (int): Limite de mensagens (default: 100)
        offset (int): Offset para paginação (default: 0)
        order (str): Ordem das mensagens - 'asc' ou 'desc' (default: 'asc')
    
    Returns:
        JSON: Lista de mensagens
    """
    try:
        limit = request.args.get('limit', 100, type=int)
        offset = request.args.get('offset', 0, type=int)
        order = request.args.get('order', 'asc')
        
        # Verifica se conversa existe
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        # Query de mensagens
        query = Message.query.filter_by(conversation_id=conversation_id)
        
        # Ordenação
        if order == 'desc':
            query = query.order_by(Message.timestamp.desc())
        else:
            query = query.order_by(Message.timestamp.asc())
        
        # Paginação
        messages = query.offset(offset).limit(limit).all()
        
        result = [msg.to_dict() for msg in messages]
        
        return jsonify({
            'messages': result,
            'conversation_id': conversation_id,
            'total': len(result),
            'offset': offset,
            'limit': limit
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao buscar mensagens da conversa {conversation_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@conversation_bp.route('/conversations/<int:conversation_id>/archive', methods=['POST'])
@cross_origin()
def archive_conversation(conversation_id):
    """
    Arquiva ou desarquiva uma conversa
    
    Path Parameters:
        conversation_id (int): ID da conversa
    
    Body:
        archived (bool): True para arquivar, False para desarquivar
    
    Returns:
        JSON: Conversa atualizada
    """
    try:
        data = request.get_json()
        archived = data.get('archived', True) if data else True
        
        # Busca conversa
        conversation = Conversation.query.get(conversation_id)
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada'}), 404
        
        conversation.is_archived = archived
        conversation.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        action = "arquivada" if archived else "desarquivada"
        logger.info(f"Conversa {conversation_id} {action}")
        
        return jsonify({
            'message': f'Conversa {action} com sucesso',
            'conversation': conversation.to_dict()
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao arquivar conversa {conversation_id}: {str(e)}")
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

