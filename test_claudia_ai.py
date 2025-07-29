#!/usr/bin/env python3
"""
Script de teste automatizado para Claudia.AI
Testa todas as funcionalidades do sistema backend e frontend
"""

import requests
import json
import time
import sys
from datetime import datetime

# Configurações
BACKEND_URL = "http://localhost:5000"
FRONTEND_URL = "http://localhost:5173"

class ClaudiaAITester:
    def __init__(self):
        self.backend_url = BACKEND_URL
        self.frontend_url = FRONTEND_URL
        self.test_results = []
        self.user_id = 1  # Mock user ID para testes
        
    def log_test(self, test_name, success, message="", data=None):
        """Registra resultado de um teste"""
        result = {
            "test_name": test_name,
            "success": success,
            "message": message,
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")
        
        if data and not success:
            print(f"   Dados: {json.dumps(data, indent=2)}")
    
    def test_backend_health(self):
        """Testa health check do backend"""
        try:
            response = requests.get(f"{self.backend_url}/api/health", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                self.log_test(
                    "Backend Health Check", 
                    True, 
                    f"Status: {data.get('status', 'unknown')}", 
                    data
                )
                return True
            else:
                self.log_test(
                    "Backend Health Check", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("Backend Health Check", False, f"Erro: {str(e)}")
            return False
    
    def test_ai_status(self):
        """Testa status da IA"""
        try:
            response = requests.get(f"{self.backend_url}/api/ai/status", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                self.log_test(
                    "AI Status Check", 
                    True, 
                    f"Status: {data.get('status', 'unknown')}", 
                    data
                )
                return True
            else:
                self.log_test(
                    "AI Status Check", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("AI Status Check", False, f"Erro: {str(e)}")
            return False
    
    def test_ai_generation(self):
        """Testa geração de resposta da IA"""
        try:
            payload = {
                "conversation_id": 1,
                "message": "Teste de geração de resposta",
                "user_id": self.user_id
            }
            
            response = requests.post(
                f"{self.backend_url}/api/ai/generate", 
                json=payload, 
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data.get('ai_response', {})
                
                if ai_response.get('content'):
                    self.log_test(
                        "AI Response Generation", 
                        True, 
                        f"Resposta gerada: {len(ai_response['content'])} caracteres"
                    )
                    return True
                else:
                    self.log_test(
                        "AI Response Generation", 
                        False, 
                        "Resposta vazia", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "AI Response Generation", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("AI Response Generation", False, f"Erro: {str(e)}")
            return False
    
    def test_learning_metrics(self):
        """Testa métricas de aprendizado"""
        try:
            response = requests.get(f"{self.backend_url}/api/learning/metrics", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                metrics = data.get('metrics', {})
                
                required_metrics = [
                    'total_conversations', 'total_ai_messages', 'total_feedback',
                    'feedback_coverage', 'learning_models_loaded'
                ]
                
                missing_metrics = [m for m in required_metrics if m not in metrics]
                
                if not missing_metrics:
                    self.log_test(
                        "Learning Metrics", 
                        True, 
                        f"Todas as métricas presentes: {len(metrics)} métricas"
                    )
                    return True
                else:
                    self.log_test(
                        "Learning Metrics", 
                        False, 
                        f"Métricas faltando: {missing_metrics}", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "Learning Metrics", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("Learning Metrics", False, f"Erro: {str(e)}")
            return False
    
    def test_user_patterns(self):
        """Testa análise de padrões do usuário"""
        try:
            response = requests.get(
                f"{self.backend_url}/api/learning/user-patterns/{self.user_id}?days=30", 
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                patterns = data.get('patterns', {})
                
                if patterns:
                    self.log_test(
                        "User Patterns Analysis", 
                        True, 
                        f"Padrões analisados para usuário {self.user_id}"
                    )
                    return True
                else:
                    self.log_test(
                        "User Patterns Analysis", 
                        True, 
                        "Nenhum padrão encontrado (normal para usuário novo)"
                    )
                    return True
            else:
                self.log_test(
                    "User Patterns Analysis", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("User Patterns Analysis", False, f"Erro: {str(e)}")
            return False
    
    def test_response_improvement(self):
        """Testa melhoria de resposta"""
        try:
            payload = {
                "user_id": self.user_id,
                "context": "Conversa sobre tecnologia",
                "base_response": "Esta é uma resposta de teste que pode ser melhorada."
            }
            
            response = requests.post(
                f"{self.backend_url}/api/learning/improve-response", 
                json=payload, 
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                improved_response = data.get('improved_response')
                
                if improved_response:
                    self.log_test(
                        "Response Improvement", 
                        True, 
                        f"Resposta processada: {len(improved_response)} caracteres"
                    )
                    return True
                else:
                    self.log_test(
                        "Response Improvement", 
                        False, 
                        "Resposta melhorada vazia", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "Response Improvement", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("Response Improvement", False, f"Erro: {str(e)}")
            return False
    
    def test_training_trigger(self):
        """Testa disparo de treinamento"""
        try:
            payload = {
                "training_type": "incremental"
            }
            
            response = requests.post(
                f"{self.backend_url}/api/learning/train", 
                json=payload, 
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                training_result = data.get('training_result', {})
                
                if training_result.get('status') == 'completed':
                    self.log_test(
                        "Training Trigger", 
                        True, 
                        f"Treinamento {training_result.get('training_type')} concluído"
                    )
                    return True
                else:
                    self.log_test(
                        "Training Trigger", 
                        False, 
                        f"Status de treinamento: {training_result.get('status')}", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "Training Trigger", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("Training Trigger", False, f"Erro: {str(e)}")
            return False
    
    def test_frontend_accessibility(self):
        """Testa acessibilidade do frontend"""
        try:
            response = requests.get(self.frontend_url, timeout=5)
            
            if response.status_code == 200:
                content = response.text
                
                # Verifica elementos essenciais
                essential_elements = [
                    "Claudia.AI",
                    "Bem-vindo",
                    "Nova Conversa",
                    "Inteligência que cresce com você"
                ]
                
                missing_elements = [elem for elem in essential_elements if elem not in content]
                
                if not missing_elements:
                    self.log_test(
                        "Frontend Accessibility", 
                        True, 
                        "Todos os elementos essenciais presentes"
                    )
                    return True
                else:
                    self.log_test(
                        "Frontend Accessibility", 
                        False, 
                        f"Elementos faltando: {missing_elements}"
                    )
                    return False
            else:
                self.log_test(
                    "Frontend Accessibility", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("Frontend Accessibility", False, f"Erro: {str(e)}")
            return False
    
    def test_api_info(self):
        """Testa endpoint de informações da API"""
        try:
            response = requests.get(f"{self.backend_url}/api/info", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                
                required_fields = ['name', 'version', 'description', 'endpoints']
                missing_fields = [field for field in required_fields if field not in data]
                
                if not missing_fields:
                    self.log_test(
                        "API Info", 
                        True, 
                        f"Versão: {data.get('version')}, Endpoints: {len(data.get('endpoints', {}))}"
                    )
                    return True
                else:
                    self.log_test(
                        "API Info", 
                        False, 
                        f"Campos faltando: {missing_fields}", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "API Info", 
                    False, 
                    f"Status code: {response.status_code}"
                )
                return False
                
        except Exception as e:
            self.log_test("API Info", False, f"Erro: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Executa todos os testes"""
        print("🧪 Iniciando testes automatizados da Claudia.AI")
        print("=" * 60)
        
        # Lista de testes a executar
        tests = [
            self.test_backend_health,
            self.test_api_info,
            self.test_ai_status,
            self.test_ai_generation,
            self.test_learning_metrics,
            self.test_user_patterns,
            self.test_response_improvement,
            self.test_training_trigger,
            self.test_frontend_accessibility
        ]
        
        # Executa cada teste
        for test in tests:
            try:
                test()
            except Exception as e:
                self.log_test(test.__name__, False, f"Erro inesperado: {str(e)}")
            
            # Pequena pausa entre testes
            time.sleep(0.5)
        
        # Relatório final
        self.generate_report()
    
    def generate_report(self):
        """Gera relatório final dos testes"""
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL DOS TESTES")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result['success'])
        failed_tests = total_tests - passed_tests
        
        success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        print(f"Total de testes: {total_tests}")
        print(f"Testes aprovados: {passed_tests}")
        print(f"Testes falharam: {failed_tests}")
        print(f"Taxa de sucesso: {success_rate:.1f}%")
        
        if failed_tests > 0:
            print("\n❌ TESTES QUE FALHARAM:")
            for result in self.test_results:
                if not result['success']:
                    print(f"  - {result['test_name']}: {result['message']}")
        
        print("\n🎯 RESUMO DO SISTEMA:")
        
        # Categoriza resultados
        backend_tests = [r for r in self.test_results if 'backend' in r['test_name'].lower() or 'api' in r['test_name'].lower() or 'ai' in r['test_name'].lower()]
        learning_tests = [r for r in self.test_results if 'learning' in r['test_name'].lower() or 'pattern' in r['test_name'].lower() or 'training' in r['test_name'].lower()]
        frontend_tests = [r for r in self.test_results if 'frontend' in r['test_name'].lower()]
        
        def category_status(tests):
            if not tests:
                return "N/A"
            passed = sum(1 for t in tests if t['success'])
            total = len(tests)
            return f"{passed}/{total} ({'✅' if passed == total else '⚠️' if passed > 0 else '❌'})"
        
        print(f"  Backend/API: {category_status(backend_tests)}")
        print(f"  Sistema de Aprendizado: {category_status(learning_tests)}")
        print(f"  Frontend: {category_status(frontend_tests)}")
        
        # Status geral
        if success_rate >= 90:
            print(f"\n🎉 SISTEMA CLAUDIA.AI: EXCELENTE ({success_rate:.1f}%)")
        elif success_rate >= 75:
            print(f"\n✅ SISTEMA CLAUDIA.AI: BOM ({success_rate:.1f}%)")
        elif success_rate >= 50:
            print(f"\n⚠️ SISTEMA CLAUDIA.AI: PRECISA MELHORIAS ({success_rate:.1f}%)")
        else:
            print(f"\n❌ SISTEMA CLAUDIA.AI: CRÍTICO ({success_rate:.1f}%)")
        
        # Salva relatório em arquivo
        report_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": failed_tests,
                "success_rate": success_rate
            },
            "test_results": self.test_results
        }
        
        with open("claudia_ai_test_report.json", "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Relatório detalhado salvo em: claudia_ai_test_report.json")

def main():
    """Função principal"""
    tester = ClaudiaAITester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()

