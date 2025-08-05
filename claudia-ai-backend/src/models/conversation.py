from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

# Importar db do user.py para evitar duplicação
from .user import db

class Conversation(db.Model):
    __tablename__ = 'conversations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False, default='Nova Conversa')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    metadata_json = db.Column(db.Text)  # JSON para metadados adicionais
    
    # Relacionamentos
    messages = db.relationship('Message', backref='conversation', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, user_id, title='Nova Conversa', metadata_dict=None):
        self.user_id = user_id
        self.title = title
        self.metadata_json = json.dumps(metadata_dict) if metadata_dict else json.dumps({})
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active,
            'metadata': self.get_metadata(),
            'message_count': len(self.messages) if self.messages else 0
        }
    
    def get_metadata(self):
        """Retorna metadados como dicionário"""
        try:
            return json.loads(self.metadata_json) if self.metadata_json else {}
        except json.JSONDecodeError:
            return {}
    
    def set_metadata(self, metadata_dict):
        """Define metadados a partir de dicionário"""
        self.metadata_json = json.dumps(metadata_dict)
    
    def __repr__(self):
        return f'<Conversation {self.id}: {self.title}>'

class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'user' ou 'assistant'
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tokens = db.Column(db.Integer, default=0)
    metadata_json = db.Column(db.Text)  # JSON para metadados adicionais
    
    # Relacionamentos
    feedbacks = db.relationship('Feedback', backref='message', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, conversation_id, role, content, tokens=0, metadata_dict=None):
        self.conversation_id = conversation_id
        self.role = role
        self.content = content
        self.tokens = tokens
        self.metadata_json = json.dumps(metadata_dict) if metadata_dict else json.dumps({})
    
    def to_dict(self):
        return {
            'id': self.id,
            'conversation_id': self.conversation_id,
            'role': self.role,
            'content': self.content,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'tokens': self.tokens,
            'metadata': self.get_metadata()
        }
    
    def get_metadata(self):
        """Retorna metadados como dicionário"""
        try:
            return json.loads(self.metadata_json) if self.metadata_json else {}
        except json.JSONDecodeError:
            return {}
    
    def set_metadata(self, metadata_dict):
        """Define metadados a partir de dicionário"""
        self.metadata_json = json.dumps(metadata_dict)
    
    def __repr__(self):
        return f'<Message {self.id}: {self.role}>'

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, message_id, rating, comment=None):
        self.message_id = message_id
        self.rating = rating
        self.comment = comment
    
    def to_dict(self):
        return {
            'id': self.id,
            'message_id': self.message_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f'<Feedback {self.id}: {self.rating}/5>'

class SystemConfig(db.Model):
    __tablename__ = 'system_config'
    
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, key, value, description=None):
        self.key = key
        self.value = value
        self.description = description
    
    def to_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'value': self.value,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<SystemConfig {self.key}>'

