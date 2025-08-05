# 🔧 Scripts da Claudia.AI

Esta pasta contém scripts de automação para facilitar a instalação, configuração e uso da Claudia.AI.

## 📋 Scripts Disponíveis

### 🚀 install-claudia-ai.sh
**Instalação completa e automática da Claudia.AI**

```bash
./scripts/install-claudia-ai.sh
```

**Funcionalidades:**
- ✅ Verificação automática de pré-requisitos
- ✅ Detecção de sistema operacional
- ✅ Instalação de dependências do sistema (opcional)
- ✅ Configuração do ambiente virtual Python
- ✅ Instalação de dependências Python e Node.js
- ✅ Inicialização do banco de dados SQLite
- ✅ Criação de arquivos de configuração (.env)
- ✅ Testes de instalação
- ✅ Criação de scripts de conveniência

**Pré-requisitos verificados:**
- Python 3.8+ (recomendado 3.11+)
- Node.js 16+ (recomendado 18+)
- npm/pnpm
- Git

**Sistemas suportados:**
- Linux (Ubuntu/Debian, RedHat/CentOS)
- macOS (com Homebrew)
- Windows (WSL recomendado)

---

### ⚡ quick-start.sh
**Inicialização rápida da aplicação**

```bash
./scripts/quick-start.sh
```

**Funcionalidades:**
- ✅ Verificação de pré-requisitos básicos
- ✅ Inicialização automática do banco de dados
- ✅ Início do backend Flask (porta 5000)
- ✅ Início do frontend React (porta 5173)
- ✅ Monitoramento de saúde dos serviços
- ✅ Verificação de conectividade
- ✅ Exibição de informações de acesso
- ✅ Monitoramento contínuo da aplicação

**URLs de acesso:**
- Frontend: http://localhost:5173
- Backend: http://localhost:5000

**Controles:**
- `Ctrl+C`: Parar aplicação
- Monitoramento automático a cada 30 segundos

---

### ⏹️ stop-claudia-ai.sh
**Parada segura da aplicação**

```bash
./scripts/stop-claudia-ai.sh
```

**Funcionalidades:**
- ✅ Parada gentil dos processos (SIGTERM)
- ✅ Parada forçada se necessário (SIGKILL)
- ✅ Liberação de portas (5000, 5173)
- ✅ Limpeza de arquivos temporários
- ✅ Verificação de parada completa
- ✅ Relatório de status final

**Opções:**
```bash
./scripts/stop-claudia-ai.sh --force    # Parada forçada
./scripts/stop-claudia-ai.sh --help     # Ajuda
```

---

### 🔍 check-status.sh
**Verificação completa de status**

```bash
./scripts/check-status.sh
```

**Verificações realizadas:**
- ✅ Processos em execução (backend/frontend)
- ✅ Portas de rede (5000, 5173)
- ✅ Conectividade HTTP
- ✅ Arquivos e configuração
- ✅ Logs do sistema
- ✅ Recursos do sistema (CPU, memória, disco)
- ✅ Status da IA
- ✅ Health checks

**Informações exibidas:**
- PIDs dos processos
- Tempo de execução
- Status de conectividade
- Tamanho de arquivos e logs
- Uso de recursos
- Resumo geral

---

## 🚀 Fluxo de Uso Recomendado

### 1. Primeira Instalação
```bash
# 1. Instalar tudo
./scripts/install-claudia-ai.sh

# 2. Iniciar aplicação
./scripts/quick-start.sh

# 3. Acessar no navegador
# http://localhost:5173
```

### 2. Uso Diário
```bash
# Iniciar
./scripts/quick-start.sh

# Verificar status (em outro terminal)
./scripts/check-status.sh

# Parar quando terminar
# Ctrl+C ou ./scripts/stop-claudia-ai.sh
```

### 3. Solução de Problemas
```bash
# Verificar status detalhado
./scripts/check-status.sh

# Parar tudo
./scripts/stop-claudia-ai.sh --force

# Reiniciar
./scripts/quick-start.sh

# Ver logs
tail -f claudia-ai.log
tail -f claudia-ai-backend/logs/app.log
```

## 🔧 Personalização dos Scripts

### Variáveis de Ambiente

Os scripts respeitam as seguintes variáveis de ambiente:

```bash
# Portas personalizadas
export CLAUDIA_BACKEND_PORT=5000
export CLAUDIA_FRONTEND_PORT=5173

# Timeouts
export CLAUDIA_STARTUP_TIMEOUT=60
export CLAUDIA_HEALTH_CHECK_TIMEOUT=30

# Logs
export CLAUDIA_LOG_LEVEL=INFO
export CLAUDIA_LOG_FILE=claudia-ai.log
```

### Modificação de Portas

Para usar portas diferentes, edite os arquivos `.env`:

**Backend (.env):**
```bash
PORT=5001  # Nova porta do backend
```

**Frontend (.env):**
```bash
VITE_API_URL=http://localhost:5001  # Apontar para nova porta do backend
```

E execute:
```bash
# Parar aplicação atual
./scripts/stop-claudia-ai.sh

# Reiniciar com novas configurações
./scripts/quick-start.sh
```

## 📊 Logs e Monitoramento

### Arquivos de Log

| Arquivo | Descrição |
|---------|-----------|
| `claudia-ai.log` | Log principal da aplicação |
| `install.log` | Log de instalação |
| `backend.log` | Log temporário do backend |
| `frontend.log` | Log temporário do frontend |
| `claudia-ai-backend/logs/app.log` | Log detalhado do backend |
| `claudia-ai-backend/logs/error.log` | Log de erros do backend |

### Comandos de Monitoramento

```bash
# Ver logs em tempo real
tail -f claudia-ai.log

# Ver apenas erros
tail -f claudia-ai.log | grep ERROR

# Ver logs do backend
tail -f claudia-ai-backend/logs/app.log

# Verificar status periodicamente
watch -n 10 ./scripts/check-status.sh
```

## 🆘 Solução de Problemas Comuns

### Erro: "Porta já em uso"
```bash
# Verificar o que está usando a porta
lsof -i :5000
lsof -i :5173

# Parar processos específicos
./scripts/stop-claudia-ai.sh --force

# Ou matar processo específico
kill -9 <PID>
```

### Erro: "Ambiente virtual não encontrado"
```bash
# Reinstalar
./scripts/install-claudia-ai.sh
```

### Erro: "Dependências não instaladas"
```bash
# Backend
cd claudia-ai-backend
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd claudia-ai-frontend
pnpm install  # ou npm install
```

### Erro: "Banco de dados não criado"
```bash
cd claudia-ai-backend
source venv/bin/activate
python -c "
from src.main import create_app
from src.models.user import db
app = create_app()
with app.app_context():
    db.create_all()
"
```

### Performance Lenta
```bash
# Verificar recursos
./scripts/check-status.sh

# Ver processos que consomem CPU
top -p $(pgrep -f "python\|node" | tr '\n' ',' | sed 's/,$//')

# Limpar cache
rm -rf claudia-ai-frontend/.vite
rm -rf claudia-ai-frontend/node_modules/.cache
```

## 🔒 Segurança

### Configurações Recomendadas

**Para desenvolvimento local:**
- Os scripts são seguros para uso local
- Portas são expostas apenas em localhost
- Logs não contêm informações sensíveis

**Para produção:**
- Altere `SECRET_KEY` no arquivo `.env`
- Configure HTTPS
- Use banco de dados externo (PostgreSQL)
- Configure firewall adequadamente

### Permissões dos Scripts

```bash
# Verificar permissões
ls -la scripts/

# Tornar executáveis (se necessário)
chmod +x scripts/*.sh

# Remover permissões de execução (se necessário)
chmod -x scripts/*.sh
```

## 📝 Contribuição

Para melhorar os scripts:

1. Faça backup dos scripts originais
2. Modifique conforme necessário
3. Teste em ambiente isolado
4. Documente as mudanças
5. Compartilhe melhorias

### Estrutura dos Scripts

Todos os scripts seguem a mesma estrutura:

```bash
#!/bin/bash
# Cabeçalho com informações
# Configuração de cores e símbolos
# Variáveis globais
# Funções utilitárias
# Funções principais
# Função main()
# Verificação de argumentos
```

---

**Versão dos Scripts**: 1.0.0  
**Última Atualização**: Janeiro 2024  
**Compatibilidade**: Linux, macOS, Windows (WSL)

Para suporte adicional, consulte a documentação completa na pasta `docs/`.

