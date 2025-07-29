import time
import random
from typing import Dict, List, Optional, Generator
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIService:
    """
    Serviço de IA para integração com Llama 3.1 70B
    
    Esta classe gerencia a comunicação com o modelo de IA, incluindo:
    - Geração de respostas
    - Streaming de respostas em tempo real
    - Gerenciamento de contexto
    - Métricas de performance
    """
    
    def __init__(self, model_path: Optional[str] = None, device: str = "auto"):
        self.model_path = model_path
        self.device = device
        self.model = None
        self.tokenizer = None
        self.is_loaded = False
        self.model_info = {
            "name": "Llama 3.1 70B",
            "version": "3.1",
            "parameters": "70B",
            "context_length": 128000,
            "languages": ["pt", "en", "es", "fr", "de", "it", "hi", "th"]
        }
        
        # Configurações padrão
        self.default_config = {
            "max_new_tokens": 2048,
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
            "repetition_penalty": 1.1,
            "do_sample": True
        }
        
        # Estatísticas
        self.stats = {
            "total_requests": 0,
            "total_tokens_generated": 0,
            "average_response_time": 0.0,
            "last_request_time": None
        }
    
    def load_model(self) -> bool:
        """
        Carrega o modelo Llama 3.1 70B
        
        Returns:
            bool: True se o modelo foi carregado com sucesso
        """
        try:
            logger.info("Carregando modelo Llama 3.1 70B...")
            
            # Para demonstração, vamos simular o carregamento
            # Em produção, aqui seria feito o carregamento real do modelo
            if self.model_path:
                # Código real para carregar o modelo:
                # from transformers import AutoModelForCausalLM, AutoTokenizer
                # self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
                # self.model = AutoModelForCausalLM.from_pretrained(
                #     self.model_path,
                #     torch_dtype=torch.float16,
                #     device_map="auto"
                # )
                pass
            
            # Simulação de carregamento
            time.sleep(2)  # Simula tempo de carregamento
            self.is_loaded = True
            logger.info("Modelo carregado com sucesso!")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao carregar modelo: {str(e)}")
            return False
    
    def generate_response(self, 
                         messages: List[Dict[str, str]], 
                         config: Optional[Dict] = None,
                         user_id: Optional[int] = None) -> Dict:
        """
        Gera resposta da IA baseada no histórico de mensagens
        
        Args:
            messages: Lista de mensagens no formato [{"role": "user/assistant", "content": "..."}]
            config: Configurações de geração (opcional)
            user_id: ID do usuário para personalização (opcional)
            
        Returns:
            Dict com resposta, métricas e metadados
        """
        start_time = time.time()
        
        try:
            # Atualiza estatísticas
            self.stats["total_requests"] += 1
            self.stats["last_request_time"] = datetime.utcnow()
            
            # Mescla configurações
            generation_config = {**self.default_config, **(config or {})}
            
            # Prepara o prompt
            prompt = self._prepare_prompt(messages)
            
            # Gera resposta (simulada para demonstração)
            if self.is_loaded:
                response_text = self._generate_real_response(prompt, generation_config)
            else:
                response_text = self._generate_mock_response(prompt, messages)
            
            # Calcula métricas
            processing_time = time.time() - start_time
            tokens_used = len(response_text.split()) * 1.3  # Estimativa aproximada
            
            # Atualiza estatísticas
            self.stats["total_tokens_generated"] += tokens_used
            self.stats["average_response_time"] = (
                (self.stats["average_response_time"] * (self.stats["total_requests"] - 1) + processing_time) 
                / self.stats["total_requests"]
            )
            
            return {
                "response": response_text,
                "metadata": {
                    "model": self.model_info["name"],
                    "processing_time": processing_time,
                    "tokens_used": int(tokens_used),
                    "config_used": generation_config,
                    "timestamp": datetime.utcnow().isoformat()
                },
                "success": True
            }
            
        except Exception as e:
            logger.error(f"Erro na geração de resposta: {str(e)}")
            return {
                "response": "Desculpe, ocorreu um erro ao processar sua mensagem. Tente novamente.",
                "metadata": {
                    "error": str(e),
                    "processing_time": time.time() - start_time,
                    "timestamp": datetime.utcnow().isoformat()
                },
                "success": False
            }
    
    def stream_response(self, 
                       messages: List[Dict[str, str]], 
                       config: Optional[Dict] = None) -> Generator[str, None, None]:
        """
        Gera resposta em streaming para interface em tempo real
        
        Args:
            messages: Lista de mensagens
            config: Configurações de geração
            
        Yields:
            str: Chunks da resposta conforme são gerados
        """
        try:
            # Prepara o prompt
            prompt = self._prepare_prompt(messages)
            
            # Simula streaming de resposta
            if self.is_loaded:
                yield from self._stream_real_response(prompt, config or self.default_config)
            else:
                yield from self._stream_mock_response(prompt, messages)
                
        except Exception as e:
            logger.error(f"Erro no streaming: {str(e)}")
            yield f"Erro: {str(e)}"
    
    def _prepare_prompt(self, messages: List[Dict[str, str]]) -> str:
        """
        Prepara o prompt no formato adequado para o Llama 3.1
        
        Args:
            messages: Lista de mensagens
            
        Returns:
            str: Prompt formatado
        """
        # Formato de prompt para Llama 3.1
        prompt_parts = []
        
        # System prompt para Claudia.AI
        system_prompt = """Você é Claudia.AI, uma assistente de inteligência artificial amigável, inteligente e prestativa. 
        Você foi criada para ajudar usuários com uma ampla variedade de tarefas, sempre mantendo um tom respeitoso e profissional.
        Você fala português brasileiro naturalmente e pode ajudar em múltiplos idiomas.
        Seja criativa, precisa e útil em suas respostas."""
        
        prompt_parts.append(f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n{system_prompt}<|eot_id|>")
        
        # Adiciona mensagens do histórico
        for message in messages:
            role = message["role"]
            content = message["content"]
            prompt_parts.append(f"<|start_header_id|>{role}<|end_header_id|>\n{content}<|eot_id|>")
        
        # Adiciona início da resposta do assistente
        prompt_parts.append("<|start_header_id|>assistant<|end_header_id|>\n")
        
        return "".join(prompt_parts)
    
    def _generate_real_response(self, prompt: str, config: Dict) -> str:
        """
        Gera resposta usando o modelo real (quando carregado)
        
        Args:
            prompt: Prompt formatado
            config: Configurações de geração
            
        Returns:
            str: Resposta gerada
        """
        # Aqui seria implementada a geração real com o modelo
        # inputs = self.tokenizer(prompt, return_tensors="pt")
        # outputs = self.model.generate(**inputs, **config)
        # response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Por enquanto, retorna resposta simulada
        return self._generate_mock_response(prompt, [])
    
    def _generate_mock_response(self, prompt: str, messages: List[Dict[str, str]]) -> str:
        """
        Gera resposta simulada para demonstração
        
        Args:
            prompt: Prompt formatado
            messages: Lista de mensagens
            
        Returns:
            str: Resposta simulada
        """
        # Simula tempo de processamento
        time.sleep(random.uniform(1, 3))
        
        # Respostas simuladas baseadas no contexto
        mock_responses = [
            "Olá! Sou a Claudia.AI e estou aqui para ajudar você. Como posso ser útil hoje?",
            "Entendo sua pergunta. Baseado no que você me disse, posso sugerir algumas abordagens interessantes para resolver isso.",
            "Essa é uma questão muito interessante! Vou explicar de forma clara e detalhada.",
            "Fico feliz em poder ajudar com isso. Vou dar uma resposta completa e útil para você.",
            "Excelente pergunta! Deixe-me compartilhar algumas informações relevantes sobre esse tópico.",
            "Compreendo perfeitamente o que você está perguntando. Aqui está uma explicação detalhada:",
            "Obrigada por confiar em mim para essa questão. Vou fazer o meu melhor para ajudar você."
        ]
        
        # Se há mensagens anteriores, tenta ser mais contextual
        if messages:
            last_message = messages[-1]["content"].lower()
            
            if "olá" in last_message or "oi" in last_message:
                return "Olá! É um prazer falar com você. Sou a Claudia.AI, sua assistente de inteligência artificial. Como posso ajudar você hoje?"
            elif "como" in last_message and "você" in last_message:
                return "Estou funcionando perfeitamente, obrigada por perguntar! Sou uma IA criada para ser útil, amigável e inteligente. Estou sempre pronta para ajudar com suas dúvidas e tarefas. Em que posso ser útil para você?"
            elif "obrigad" in last_message:
                return "De nada! Fico muito feliz em poder ajudar. Se tiver mais alguma dúvida ou precisar de qualquer coisa, estarei aqui. É sempre um prazer conversar com você!"
        
        return random.choice(mock_responses)
    
    def _stream_real_response(self, prompt: str, config: Dict) -> Generator[str, None, None]:
        """
        Streaming de resposta real (quando modelo estiver carregado)
        """
        # Implementação real seria aqui
        yield from self._stream_mock_response(prompt, [])
    
    def _stream_mock_response(self, prompt: str, messages: List[Dict[str, str]]) -> Generator[str, None, None]:
        """
        Simula streaming de resposta para demonstração
        """
        response = self._generate_mock_response(prompt, messages)
        words = response.split()
        
        for i, word in enumerate(words):
            yield word + (" " if i < len(words) - 1 else "")
            time.sleep(random.uniform(0.05, 0.2))  # Simula velocidade de geração
    
    def get_model_info(self) -> Dict:
        """
        Retorna informações sobre o modelo
        
        Returns:
            Dict: Informações do modelo e estatísticas
        """
        return {
            "model_info": self.model_info,
            "is_loaded": self.is_loaded,
            "stats": self.stats,
            "config": self.default_config
        }
    
    def update_config(self, new_config: Dict) -> bool:
        """
        Atualiza configurações padrão do modelo
        
        Args:
            new_config: Novas configurações
            
        Returns:
            bool: True se atualizado com sucesso
        """
        try:
            self.default_config.update(new_config)
            logger.info(f"Configurações atualizadas: {new_config}")
            return True
        except Exception as e:
            logger.error(f"Erro ao atualizar configurações: {str(e)}")
            return False

# Instância global do serviço de IA
ai_service = AIService()

# Função para inicializar o serviço
def initialize_ai_service(model_path: Optional[str] = None) -> bool:
    """
    Inicializa o serviço de IA
    
    Args:
        model_path: Caminho para o modelo (opcional)
        
    Returns:
        bool: True se inicializado com sucesso
    """
    global ai_service
    
    if model_path:
        ai_service.model_path = model_path
        return ai_service.load_model()
    else:
        # Modo demonstração sem modelo real
        ai_service.is_loaded = False
        logger.info("Serviço de IA inicializado em modo demonstração")
        return True

