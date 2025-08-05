from flask import Blueprint, request, jsonify
from src.models.user import db, User
import logging

user_bp = Blueprint('user', __name__)
logger = logging.getLogger(__name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    """Lista todos os usuários"""
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        logger.error(f"Erro ao buscar usuários: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@user_bp.route('/users', methods=['POST'])
def create_user():
    """Cria um novo usuário"""
    try:
        data = request.get_json()
        
        if not data or not data.get('username') or not data.get('email'):
            return jsonify({'error': 'Username e email são obrigatórios'}), 400
        
        # Verificar se usuário já existe
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()
        
        if existing_user:
            return jsonify({'error': 'Usuário ou email já existe'}), 409
        
        # Criar novo usuário
        user = User(
            username=data['username'],
            email=data['email'],
            preferences=data.get('preferences', {})
        )
        
        db.session.add(user)
        db.session.commit()
        
        logger.info(f"Usuário criado: {user.username}")
        return jsonify(user.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao criar usuário: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Busca um usuário específico"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        return jsonify(user.to_dict()), 200
    except Exception as e:
        logger.error(f"Erro ao buscar usuário {user_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Atualiza um usuário"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Atualizar campos
        if 'username' in data:
            # Verificar se username já existe
            existing = User.query.filter(
                User.username == data['username'],
                User.id != user_id
            ).first()
            if existing:
                return jsonify({'error': 'Username já existe'}), 409
            user.username = data['username']
        
        if 'email' in data:
            # Verificar se email já existe
            existing = User.query.filter(
                User.email == data['email'],
                User.id != user_id
            ).first()
            if existing:
                return jsonify({'error': 'Email já existe'}), 409
            user.email = data['email']
        
        if 'preferences' in data:
            user.set_preferences(data['preferences'])
        
        if 'is_active' in data:
            user.is_active = data['is_active']
        
        db.session.commit()
        
        logger.info(f"Usuário atualizado: {user.username}")
        return jsonify(user.to_dict()), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao atualizar usuário {user_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Remove um usuário"""
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        username = user.username
        db.session.delete(user)
        db.session.commit()
        
        logger.info(f"Usuário removido: {username}")
        return jsonify({'message': 'Usuário removido com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao remover usuário {user_id}: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

