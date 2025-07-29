import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from src.models.user import db
from src.models.conversation import Conversation, Message, Feedback, SystemConfig
from src.routes.user import user_bp
from src.routes.conversation import conversation_bp
from src.routes.ai import ai_bp
from src.routes.learning import learning_bp
from src.services.ai_service import initialize_ai_service
from src.services.learning_service import initialize_learning_service
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configurações da aplicação
app.config['SECRET_KEY'] = 'claudia-ai-secret-key-2025'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração CORS para permitir requisições do frontend
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Registra blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(conversation_bp, url_prefix='/api')
app.register_blueprint(ai_bp, url_prefix='/api')
app.register_blueprint(learning_bp, url_prefix='/api')

# Inicializa banco de dados
db.init_app(app)
with app.app_context():
    db.create_all()
    logger.info("Banco de dados inicializado")
    
    # Configura dados iniciais se necessário
    if not SystemConfig.query.filter_by(key='app_version').first():
        SystemConfig.set_config('app_version', '1.0.0', 'Versão da aplicação Claudia.AI')
        SystemConfig.set_config('ai_model', 'Llama 3.1 70B', 'Modelo de IA utilizado')
        SystemConfig.set_config('max_conversations_per_user', '100', 'Máximo de conversas por usuário')
        logger.info("Configurações iniciais criadas")

# Inicializa serviço de IA
initialize_ai_service()

# Inicializa serviço de aprendizado
initialize_learning_service()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve arquivos estáticos do frontend"""
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        # Verifica conexão com banco de dados
        db.session.execute(db.text('SELECT 1'))
        
        # Verifica status do serviço de IA
        from src.services.ai_service import ai_service
        ai_status = ai_service.get_model_info()
        
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'ai_service': 'online' if ai_status['is_loaded'] else 'demo_mode',
            'version': SystemConfig.get_config('app_version', '1.0.0'),
            'timestamp': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

@app.route('/api/info', methods=['GET'])
def app_info():
    """Informações da aplicação"""
    return jsonify({
        'name': 'Claudia.AI Backend',
        'version': SystemConfig.get_config('app_version', '1.0.0'),
        'description': 'Backend da IA conversacional Claudia.AI baseada em Llama 3.1 70B',
        'ai_model': SystemConfig.get_config('ai_model', 'Llama 3.1 70B'),
        'features': [
            'Conversas inteligentes',
            'Aprendizado contínuo',
            'Feedback de usuários',
            'Streaming de respostas',
            'Suporte ao português'
        ],
        'endpoints': {
            'conversations': '/api/conversations',
            'ai': '/api/ai',
            'users': '/api/users',
            'learning': '/api/learning',
            'health': '/api/health'
        }
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handler para 404"""
    return jsonify({'error': 'Endpoint não encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para 500"""
    logger.error(f"Erro interno: {str(error)}")
    return jsonify({'error': 'Erro interno do servidor'}), 500

@app.before_request
def log_request_info():
    """Log de requisições"""
    if not request.path.startswith('/static'):
        logger.info(f"{request.method} {request.path} - {request.remote_addr}")

if __name__ == '__main__':
    logger.info("Iniciando Claudia.AI Backend...")
    logger.info("Acesse http://localhost:5000 para a interface")
    logger.info("API disponível em http://localhost:5000/api")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
