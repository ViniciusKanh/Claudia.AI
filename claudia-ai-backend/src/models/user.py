from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    preferences = db.Column(db.Text)  # JSON string para preferências
    
    # Relacionamentos
    conversations = db.relationship('Conversation', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, username, email, preferences=None):
        self.username = username
        self.email = email
        self.preferences = json.dumps(preferences) if preferences else json.dumps({})
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'is_active': self.is_active,
            'preferences': json.loads(self.preferences) if self.preferences else {}
        }
    
    def get_preferences(self):
        """Retorna preferências como dicionário"""
        try:
            return json.loads(self.preferences) if self.preferences else {}
        except json.JSONDecodeError:
            return {}
    
    def set_preferences(self, preferences_dict):
        """Define preferências a partir de dicionário"""
        self.preferences = json.dumps(preferences_dict)
    
    def __repr__(self):
        return f'<User {self.username}>'

