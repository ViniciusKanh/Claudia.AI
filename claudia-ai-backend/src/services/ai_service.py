import os
import logging
from datetime import datetime
import random

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        # AI_MODEL_TYPE é a variável principal. AI_MODE é mantida por
        # compatibilidade retroativa.
        self.model_type = os.getenv('AI_MODEL_TYPE') or os.getenv('AI_MODE', 'demo')
        self.model_name = os.getenv('AI_MODEL_NAME', 'demo')
        self.model = None
        self.tokenizer = None
        self.is_initialized = False
        
        # Respostas de demonstração
        self.demo_responses = [
            "Olá! Sou a Claudia, sua assistente de IA. Como posso ajudá-lo hoje?",
            "Que pergunta interessante! Vou fazer o meu melhor para responder.",
            "Estou aqui para conversar e ajudar no que você precisar. O que gostaria de saber?",
            "Como uma IA em desenvolvimento, estou sempre aprendendo. Conte-me mais sobre isso!",
            "Essa é uma ótima questão! Deixe-me pensar na melhor forma de responder.",
            "Adoro conversar sobre diferentes tópicos. Qual é o seu interesse principal?",
            "Sou uma IA criada para ser útil e amigável. Como posso tornar seu dia melhor?",
            "Interessante perspectiva! Você poderia elaborar mais sobre esse ponto?",
            "Estou funcionando em modo demonstração, mas posso ter conversas significativas!",
            "Que bom conversar com você! Há algo específico que gostaria de discutir?"
        ]
        
        self.initialize_model()
    
    def initialize_model(self):
        """Inicializa o modelo de IA baseado na configuração"""
        try:
            if self.model_type == 'openai':
                self._initialize_openai()
            elif self.model_type == 'huggingface':
                self._initialize_huggingface()
            elif self.model_type == 'llama':
                self._initialize_llama()
            else:
                logger.info("Usando modo demonstração")
                self.is_initialized = True
        except Exception as e:
            logger.error(f"Erro ao inicializar modelo: {e}")
            logger.info("Fallback para modo demonstração")
            self.model_type = 'demo'
            self.is_initialized = True
    
    def _initialize_openai(self):
        """Configura integração com OpenAI"""
        try:
            import openai
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OPENAI_API_KEY não configurada")
            
            openai.api_key = api_key
            self.model_name = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
            self.is_initialized = True
            logger.info(f"OpenAI configurado com modelo: {self.model_name}")
        except ImportError:
            logger.error("Biblioteca openai não instalada")
            raise
        except Exception as e:
            logger.error(f"Erro ao configurar OpenAI: {e}")
            raise
    
    def _initialize_huggingface(self):
        """Configura modelo do Hugging Face"""
        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            import torch
            
            model_name = os.getenv('HF_MODEL_NAME', 'microsoft/DialoGPT-medium')
            
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            
            # Configurar para GPU se disponível
            if torch.cuda.is_available():
                self.model = self.model.cuda()
                logger.info("Modelo carregado na GPU")
            
            self.is_initialized = True
            logger.info(f"Modelo Hugging Face carregado: {model_name}")
        except ImportError:
            logger.error("Bibliotecas transformers/torch não instaladas")
            raise
        except Exception as e:
            logger.error(f"Erro ao carregar modelo Hugging Face: {e}")
            raise
    
    def _initialize_llama(self):
        """Configura modelo Llama local"""
        try:
            from llama_cpp import Llama

            # Permite configurar caminho e nome do modelo via variáveis de ambiente
            self.model_name = os.getenv(
                'LLAMA_MODEL_NAME', 'llama-3.3-70b-instruct'
            )
            model_path = os.getenv(
                'LLAMA_MODEL_PATH', './models/llama-3.3-70b-instruct'
            )

            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Modelo não encontrado: {model_path}")

            self.model = Llama(
                model_path=model_path,
                n_ctx=2048,
                n_threads=8,
                verbose=False
            )
            self.is_initialized = True
            logger.info(
                f"Modelo Llama carregado com sucesso: {self.model_name}"
            )
        except ImportError:
            logger.error("Biblioteca llama-cpp-python não instalada")
            raise
        except Exception as e:
            logger.error(f"Erro ao carregar Llama: {e}")
            raise
    
    def generate_response(self, message, conversation_id=None, user_id=None, context=None):
        """Gera resposta usando o modelo configurado"""
        if not self.is_initialized:
            return self._error_response("Modelo não inicializado")
        
        try:
            if self.model_type == 'openai':
                return self._generate_openai_response(message, context)
            elif self.model_type == 'huggingface':
                return self._generate_hf_response(message, context)
            elif self.model_type == 'llama':
                return self._generate_llama_response(message, context)
            else:
                return self._generate_demo_response(message, context)
        except Exception as e:
            logger.error(f"Erro ao gerar resposta: {e}")
            return self._error_response("Erro ao gerar resposta")
    
    def _generate_openai_response(self, message, context=None):
        """Gera resposta usando OpenAI"""
        try:
            import openai
            
            messages = [
                {"role": "system", "content": "Você é Claudia, uma assistente IA amigável, prestativa e inteligente. Responda sempre em português de forma natural e conversacional."}
            ]
            
            # Adicionar contexto se fornecido
            if context and isinstance(context, list):
                messages.extend(context)
            
            messages.append({"role": "user", "content": message})
            
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                max_tokens=500,
                temperature=0.7,
                top_p=0.9
            )
            
            return {
                'response': response.choices[0].message.content.strip(),
                'tokens': response.usage.total_tokens,
                'model': self.model_name,
                'timestamp': datetime.utcnow().isoformat(),
                'status': 'success'
            }
        except Exception as e:
            logger.error(f"Erro OpenAI: {e}")
            return self._generate_demo_response(message)
    
    def _generate_hf_response(self, message, context=None):
        """Gera resposta usando Hugging Face"""
        try:
            import torch
            
            # Preparar input
            input_text = message
            if context:
                input_text = f"{context}\n{message}"
            
            # Tokenizar
            inputs = self.tokenizer.encode(input_text, return_tensors='pt')
            
            # Gerar resposta
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + 100,
                    temperature=0.7,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            # Decodificar resposta
            response_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extrair apenas a nova parte da resposta
            if input_text in response_text:
                response_text = response_text.replace(input_text, "").strip()
            
            return {
                'response': response_text or "Desculpe, não consegui gerar uma resposta adequada.",
                'tokens': len(outputs[0]),
                'model': 'huggingface-local',
                'timestamp': datetime.utcnow().isoformat(),
                'status': 'success'
            }
        except Exception as e:
            logger.error(f"Erro Hugging Face: {e}")
            return self._generate_demo_response(message)
    
    def _generate_llama_response(self, message, context=None):
        """Gera resposta usando Llama"""
        try:
            def build_prompt(msg, ctx):
                """Constrói prompt no formato Llama 3.x"""
                prompt = (
                    "<|begin_of_text|>"
                    "<|start_header_id|>system<|end_header_id|>\n"
                    "Você é Claudia, uma assistente IA amigável, prestativa e inteligente. Responda sempre em português de forma natural e conversacional."
                    "<|eot_id|>"
                )
                if ctx and isinstance(ctx, list):
                    for item in ctx:
                        role = item.get('role', 'user')
                        content = item.get('content', '')
                        prompt += (
                            f"<|start_header_id|>{role}<|end_header_id|>\n"
                            f"{content}<|eot_id|>"
                        )
                prompt += (
                    "<|start_header_id|>user<|end_header_id|>\n"
                    f"{msg}<|eot_id|>"
                    "<|start_header_id|>assistant<|end_header_id|>\n"
                )
                return prompt

            prompt = build_prompt(message, context)

            response = self.model(
                prompt,
                max_tokens=500,
                temperature=0.7,
                top_p=0.9,
                stop=["<|eot_id|>"],
                echo=False
            )

            text = response['choices'][0]['text'].strip()

            return {
                'response': text,
                'tokens': len(text.split()),
                'model': self.model_name,
                'timestamp': datetime.utcnow().isoformat(),
                'status': 'success'
            }
        except Exception as e:
            logger.error(f"Erro Llama: {e}")
            return self._generate_demo_response(message)
    
    def _generate_demo_response(self, message, context=None):
        """Gera resposta de demonstração"""
        # Escolher resposta baseada no conteúdo da mensagem
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['olá', 'oi', 'hello', 'bom dia', 'boa tarde', 'boa noite']):
            response = "Olá! Sou a Claudia, sua assistente de IA. É um prazer conversar com você! Como posso ajudá-lo hoje?"
        elif any(word in message_lower for word in ['como', 'você', 'está', 'vai']):
            response = "Estou muito bem, obrigada por perguntar! Estou funcionando perfeitamente e pronta para ajudar. E você, como está?"
        elif any(word in message_lower for word in ['nome', 'quem', 'você']):
            response = "Eu sou a Claudia.AI, uma inteligência artificial criada para ser sua assistente pessoal. Fui desenvolvida para ser amigável, útil e sempre disposta a aprender!"
        elif any(word in message_lower for word in ['ajuda', 'help', 'socorro']):
            response = "Claro! Estou aqui para ajudar. Posso conversar sobre diversos assuntos, responder perguntas, dar sugestões e muito mais. O que você gostaria de saber?"
        elif any(word in message_lower for word in ['obrigado', 'obrigada', 'thanks', 'valeu']):
            response = "De nada! Fico feliz em poder ajudar. Se precisar de mais alguma coisa, é só me chamar!"
        elif any(word in message_lower for word in ['tchau', 'bye', 'até logo', 'adeus']):
            response = "Até logo! Foi um prazer conversar com você. Volte sempre que quiser bater um papo!"
        else:
            # Resposta aleatória para outras mensagens
            response = random.choice(self.demo_responses)
        
        return {
            'response': response,
            'tokens': len(response.split()),
            'model': 'demo-mode',
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'demo'
        }
    
    def _error_response(self, error_message):
        """Retorna resposta de erro padronizada"""
        return {
            'response': f"Desculpe, ocorreu um erro: {error_message}. Tente novamente em alguns instantes.",
            'tokens': 0,
            'model': self.model_type,
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'error'
        }
    
    def get_model_info(self):
        """Retorna informações sobre o modelo atual"""
        return {
            'model_type': self.model_type,
            'model_name': self.model_name,
            'is_initialized': self.is_initialized,
            'status': 'online' if self.is_initialized else 'offline',
            'capabilities': {
                'text_generation': True,
                'conversation': True,
                'context_aware': self.model_type != 'demo',
                'multilingual': self.model_type != 'demo'
            }
        }
    
    def stream_response(self, message, conversation_id=None, user_id=None):
        """Gera resposta em streaming (simulado para demo)"""
        response_data = self.generate_response(message, conversation_id, user_id)
        
        # Simular streaming dividindo a resposta em chunks
        response_text = response_data['response']
        words = response_text.split()
        
        for i, word in enumerate(words):
            chunk = {
                'chunk': word + ' ',
                'is_final': i == len(words) - 1,
                'tokens': response_data['tokens'],
                'model': response_data['model'],
                'timestamp': datetime.utcnow().isoformat()
            }
            yield chunk

# Instância global do serviço
ai_service = AIService()

