import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime
import logging
from sqlalchemy import text
# Carregar variáveis de ambiente
load_dotenv()

# Importar modelos e rotas
from src.models.user import db
from src.routes.user import user_bp
from src.routes.conversation import conversation_bp
from src.routes.ai import ai_bp

# Configuração de logging
logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__, static_folder='static', static_url_path='')
    
    # Configurações da aplicação
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-claudia-ai')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///src/database/app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_timeout': 20,
        'pool_recycle': -1,
        'pool_pre_ping': True
    }
    
    # Configuração CORS
    cors_origins = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://localhost:5173').split(',')
    CORS(app, resources={
        r"/api/*": {
            "origins": cors_origins,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Inicialização do banco de dados
    db.init_app(app)
    
    # Registro de blueprints
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(conversation_bp, url_prefix='/api')
    app.register_blueprint(ai_bp, url_prefix='/api')
    
    # Rotas principais
    @app.route('/')
    def index():
        """Serve o frontend React se disponível"""
        try:
            return send_from_directory(app.static_folder, 'index.html')
        except:
            return jsonify({
                'message': 'Claudia.AI Backend está funcionando!',
                'version': '1.0.0',
                'status': 'online',
                'frontend': 'not_deployed'
            })
    
    @app.route('/api/health')
    def health_check():
        """Endpoint de verificação de saúde"""
        try:
            # Testar conexão com banco de dados
            db.session.execute(text('SELECT 1'))
            db_status = 'healthy'
        except Exception as e:
            logger.error(f"Erro no banco de dados: {e}")
            db_status = 'unhealthy'
        
        return jsonify({
            'status': 'healthy' if db_status == 'healthy' else 'degraded',
            'timestamp': datetime.utcnow().isoformat(),
            'database': db_status,
            'version': '1.0.0',
            'environment': os.getenv('FLASK_ENV', 'production')
        })
    
    @app.route('/api/info')
    def app_info():
        """Informações da aplicação"""
        return jsonify({
            'name': 'Claudia.AI Backend',
            'version': '1.0.0',
            'description': 'Backend da Claudia.AI - Inteligência Artificial Conversacional',
            'author': 'Manus AI',
            'endpoints': {
                'health': '/api/health',
                'users': '/api/users',
                'conversations': '/api/conversations',
                'ai_generate': '/api/ai/generate',
                'ai_stream': '/api/ai/stream',
                'ai_status': '/api/ai/status',
                'ai_models': '/api/ai/models',
                'ai_config': '/api/ai/config',
                'ai_test': '/api/ai/test'
            },
            'documentation': {
                'openapi': '/api/docs',
                'postman': '/api/postman.json'
            },
            'timestamp': datetime.utcnow().isoformat()
        })
    
    @app.errorhandler(404)
    def not_found(error):
        """Handler para páginas não encontradas"""
        if request.path.startswith('/api/'):
            return jsonify({'error': 'Endpoint não encontrado'}), 404
        else:
            # Tentar servir o frontend para rotas SPA
            try:
                return send_from_directory(app.static_folder, 'index.html')
            except:
                return jsonify({'error': 'Página não encontrada'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handler para erros internos"""
        logger.error(f"Erro interno: {error}")
        return jsonify({'error': 'Erro interno do servidor'}), 500
    
    # Criar tabelas do banco de dados
    with app.app_context():
        try:
            # Criar diretório do banco se não existir
            db_dir = os.path.dirname(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
            if db_dir and not os.path.exists(db_dir):
                os.makedirs(db_dir, exist_ok=True)
            
            db.create_all()
            logger.info("Banco de dados inicializado com sucesso")
            
            # Criar usuário padrão se não existir
            from src.models.user import User
            if not User.query.first():
                default_user = User(
                    username='claudia_user',
                    email='user@claudia.ai',
                    preferences={'theme': 'green', 'language': 'pt-BR'}
                )
                db.session.add(default_user)
                db.session.commit()
                logger.info("Usuário padrão criado")
                
        except Exception as e:
            logger.error(f"Erro ao inicializar banco de dados: {e}")
    
    logger.info("Claudia.AI Backend inicializado com sucesso")
    return app

def main():
    """Função principal para executar a aplicação"""
    app = create_app()
    
    # Configurações do servidor
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Iniciando servidor em {host}:{port}")
    logger.info(f"Debug mode: {debug}")
    logger.info(f"Environment: {os.getenv('FLASK_ENV', 'production')}")
    
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )

if __name__ == '__main__':
    main()

