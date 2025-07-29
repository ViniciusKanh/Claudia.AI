from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from src.models.user import db, User
from src.models.conversation import Conversation, Message, Feedback
from src.services.learning_service import learning_service
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Blueprint para rotas de aprendizado
learning_bp = Blueprint('learning', __name__)

@learning_bp.route('/learning/analyze-conversation/<int:conversation_id>', methods=['POST'])
@cross_origin()
def analyze_conversation(conversation_id):
    """
    Analisa feedback e padrões de uma conversa específica
    
    Path Parameters:
        conversation_id (int): ID da conversa
    
    Body:
        user_id (int): ID do usuário
    
    Returns:
        JSON: Análise da conversa
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id') if data else None
        
        if not user_id:
            return jsonify({'error': 'user_id é obrigatório'}), 400
        
        # Verifica se conversa existe e pertence ao usuário
        conversation = Conversation.query.filter_by(id=conversation_id, user_id=user_id).first()
        if not conversation:
            return jsonify({'error': 'Conversa não encontrada ou não pertence ao usuário'}), 404
        
        # Executa análise
        analysis = learning_service.analyze_conversation_feedback(conversation_id, user_id)
        
        if 'error' in analysis:
            return jsonify(analysis), 500
        
        logger.info(f"Análise de conversa {conversation_id} concluída")
        
        return jsonify({
            'message': 'Análise concluída com sucesso',
            'analysis': analysis
        }), 200
        
    except Exception as e:
        logger.error(f"Erro na análise de conversa: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@learning_bp.route('/learning/user-patterns/<int:user_id>', methods=['GET'])
@cross_origin()
def get_user_patterns(user_id):
    """
    Obtém padrões de aprendizado de um usuário
    
    Path Parameters:
        user_id (int): ID do usuário
    
    Query Parameters:
        days (int): Número de dias para análise (default: 30)
    
    Returns:
        JSON: Padrões do usuário
    """
    try:
        days = request.args.get('days', 30, type=int)
        
        # Verifica se usuário existe
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        # Executa análise de padrões
        patterns = learning_service.learn_from_user_interactions(user_id, days)
        
        if 'error' in patterns:
            return jsonify(patterns), 500
        
        logger.info(f"Padrões do usuário {user_id} analisados")
        
        return jsonify({
            'message': 'Padrões analisados com sucesso',
            'patterns': patterns
        }), 200
        
    except Exception as e:
        logger.error(f"Erro na análise de padrões: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@learning_bp.route('/learning/improve-response', methods=['POST'])
@cross_origin()
def improve_response():
    """
    Melhora uma resposta baseada no aprendizado do usuário
    
    Body:
        user_id (int): ID do usuário
        context (str): Contexto da conversa
        base_response (str): Resposta base
    
    Returns:
        JSON: Resposta melhorada
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados JSON são obrigatórios'}), 400
        
        user_id = data.get('user_id')
        context = data.get('context', '')
        base_response = data.get('base_response')
        
        if not all([user_id, base_response]):
            return jsonify({'error': 'user_id e base_response são obrigatórios'}), 400
        
        # Verifica se usuário existe
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404
        
        # Melhora a resposta
        improved_response = learning_service.improve_response_generation(
            user_id, context, base_response
        )
        
        logger.info(f"Resposta melhorada para usuário {user_id}")
        
        return jsonify({
            'message': 'Resposta melhorada com sucesso',
            'original_response': base_response,
            'improved_response': improved_response,
            'improvement_applied': improved_response != base_response
        }), 200
        
    except Exception as e:
        logger.error(f"Erro na melhoria da resposta: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@learning_bp.route('/learning/metrics', methods=['GET'])
@cross_origin()
def get_learning_metrics():
    """
    Obtém métricas gerais do sistema de aprendizado
    
    Returns:
        JSON: Métricas do aprendizado
    """
    try:
        metrics = learning_service.get_learning_metrics()
        
        if 'error' in metrics:
            return jsonify(metrics), 500
        
        return jsonify({
            'message': 'Métricas obtidas com sucesso',
            'metrics': metrics
        }), 200
        
    except Exception as e:
        logger.error(f"Erro ao obter métricas: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@learning_bp.route('/learning/train', methods=['POST'])
@cross_origin()
def trigger_training():
    """
    Dispara treinamento do sistema de aprendizado
    
    Body:
        training_type (str): Tipo de treinamento ('full', 'incremental')
        user_id (int, opcional): ID do usuário para treinamento específico
    
    Returns:
        JSON: Status do treinamento
    """
    try:
        data = request.get_json()
        training_type = data.get('training_type', 'incremental') if data else 'incremental'
        user_id = data.get('user_id') if data else None
        
        # Simula processo de treinamento
        if training_type == 'full':
            # Treinamento completo do sistema
            logger.info("Iniciando treinamento completo do sistema")
            
            # Em produção, aqui seria executado o treinamento real
            training_result = {
                "training_type": "full",
                "status": "completed",
                "duration_seconds": 120,  # Simulado
                "models_updated": ["user_preferences", "conversation_patterns", "response_quality"],
                "improvement_metrics": {
                    "accuracy_improvement": 0.05,
                    "response_quality_improvement": 0.08,
                    "user_satisfaction_improvement": 0.12
                }
            }
            
        elif user_id:
            # Treinamento específico do usuário
            logger.info(f"Iniciando treinamento para usuário {user_id}")
            
            # Verifica se usuário existe
            user = User.query.get(user_id)
            if not user:
                return jsonify({'error': 'Usuário não encontrado'}), 404
            
            # Executa aprendizado do usuário
            patterns = learning_service.learn_from_user_interactions(user_id, 30)
            
            training_result = {
                "training_type": "user_specific",
                "user_id": user_id,
                "status": "completed",
                "patterns_learned": patterns,
                "duration_seconds": 15  # Simulado
            }
            
        else:
            # Treinamento incremental
            logger.info("Iniciando treinamento incremental")
            
            training_result = {
                "training_type": "incremental",
                "status": "completed",
                "duration_seconds": 30,  # Simulado
                "new_patterns_learned": 5,
                "models_updated": ["recent_conversations"]
            }
        
        return jsonify({
            'message': 'Treinamento concluído com sucesso',
            'training_result': training_result,
            'timestamp': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"Erro no treinamento: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@learning_bp.route('/learning/feedback-analysis', methods=['GET'])
@cross_origin()
def get_feedback_analysis():
    """
    Obtém análise detalhada do feedback dos usuários
    
    Query Parameters:
        days (int): Período de análise em dias (default: 30)
        user_id (int, opcional): Análise específica de um usuário
    
    Returns:
        JSON: Análise do feedback
    """
    try:
        days = request.args.get('days', 30, type=int)
        user_id = request.args.get('user_id', type=int)
        
        # Query base para feedback
        query = db.session.query(Feedback).join(Message).join(Conversation)
        
        # Filtro por período
        from datetime import timedelta
        start_date = datetime.utcnow() - timedelta(days=days)
        query = query.filter(Feedback.created_at >= start_date)
        
        # Filtro por usuário se especificado
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return jsonify({'error': 'Usuário não encontrado'}), 404
            query = query.filter(Conversation.user_id == user_id)
        
        feedback_entries = query.all()
        
        if not feedback_entries:
            return jsonify({
                'message': 'Nenhum feedback encontrado para o período',
                'analysis': {
                    'total_feedback': 0,
                    'period_days': days,
                    'user_id': user_id
                }
            }), 200
        
        # Análise do feedback
        ratings = [f.rating for f in feedback_entries if f.rating]
        comments = [f.comment for f in feedback_entries if f.comment]
        
        analysis = {
            'total_feedback': len(feedback_entries),
            'period_days': days,
            'user_id': user_id,
            'rating_stats': {
                'total_ratings': len(ratings),
                'average_rating': sum(ratings) / len(ratings) if ratings else None,
                'rating_distribution': {
                    '5_stars': sum(1 for r in ratings if r == 5),
                    '4_stars': sum(1 for r in ratings if r == 4),
                    '3_stars': sum(1 for r in ratings if r == 3),
                    '2_stars': sum(1 for r in ratings if r == 2),
                    '1_star': sum(1 for r in ratings if r == 1)
                }
            },
            'comment_stats': {
                'total_comments': len(comments),
                'average_comment_length': sum(len(c.split()) for c in comments) / len(comments) if comments else 0,
                'positive_sentiment': sum(1 for c in comments if learning_service._is_positive_comment(c)),
                'negative_sentiment': sum(1 for c in comments if not learning_service._is_positive_comment(c))
            },
            'improvement_suggestions': []
        }
        
        # Sugestões de melhoria baseadas na análise
        if analysis['rating_stats']['average_rating'] and analysis['rating_stats']['average_rating'] < 3.5:
            analysis['improvement_suggestions'].append("Foco em melhorar qualidade geral das respostas")
        
        if analysis['comment_stats']['negative_sentiment'] > analysis['comment_stats']['positive_sentiment']:
            analysis['improvement_suggestions'].append("Análise detalhada dos comentários negativos necessária")
        
        return jsonify({
            'message': 'Análise de feedback concluída',
            'analysis': analysis
        }), 200
        
    except Exception as e:
        logger.error(f"Erro na análise de feedback: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@learning_bp.route('/learning/export-data', methods=['GET'])
@cross_origin()
def export_learning_data():
    """
    Exporta dados de aprendizado para análise externa
    
    Query Parameters:
        format (str): Formato de exportação ('json', 'csv')
        data_type (str): Tipo de dados ('conversations', 'feedback', 'patterns')
        user_id (int, opcional): Dados específicos de um usuário
    
    Returns:
        JSON/CSV: Dados exportados
    """
    try:
        format_type = request.args.get('format', 'json')
        data_type = request.args.get('data_type', 'conversations')
        user_id = request.args.get('user_id', type=int)
        
        if format_type not in ['json', 'csv']:
            return jsonify({'error': 'Formato deve ser json ou csv'}), 400
        
        if data_type not in ['conversations', 'feedback', 'patterns']:
            return jsonify({'error': 'Tipo de dados inválido'}), 400
        
        # Coleta dados baseado no tipo solicitado
        if data_type == 'conversations':
            query = db.session.query(Conversation)
            if user_id:
                query = query.filter_by(user_id=user_id)
            
            conversations = query.all()
            data = [conv.to_dict() for conv in conversations]
            
        elif data_type == 'feedback':
            query = db.session.query(Feedback).join(Message).join(Conversation)
            if user_id:
                query = query.filter(Conversation.user_id == user_id)
            
            feedback_entries = query.all()
            data = [feedback.to_dict() for feedback in feedback_entries]
            
        elif data_type == 'patterns':
            # Exporta padrões aprendidos
            if user_id:
                patterns = learning_service._load_user_preferences(user_id)
                data = [patterns] if patterns else []
            else:
                data = list(learning_service.user_preferences.values())
        
        export_result = {
            'data_type': data_type,
            'format': format_type,
            'user_id': user_id,
            'total_records': len(data),
            'exported_at': datetime.utcnow().isoformat(),
            'data': data
        }
        
        # Em produção, para CSV seria gerado arquivo real
        if format_type == 'csv':
            export_result['note'] = 'CSV export would be implemented with proper file generation'
        
        return jsonify(export_result), 200
        
    except Exception as e:
        logger.error(f"Erro na exportação: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

