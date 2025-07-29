# Guia de Instalação Completo - Claudia.AI

Este guia fornece instruções detalhadas para instalar e configurar a Claudia.AI em diferentes ambientes.

## 📋 Pré-requisitos

### Requisitos de Sistema

**Mínimos:**
- CPU: 2 cores
- RAM: 4GB
- Armazenamento: 2GB livres
- SO: Linux, macOS, Windows 10+

**Recomendados:**
- CPU: 4+ cores
- RAM: 8GB+
- Armazenamento: 10GB+ livres
- SO: Ubuntu 20.04+ / macOS 12+ / Windows 11

### Software Necessário

1. **Python 3.11+**
   ```bash
   # Verificar versão
   python --version
   # ou
   python3 --version
   ```

2. **Node.js 20+**
   ```bash
   # Verificar versão
   node --version
   npm --version
   ```

3. **Git**
   ```bash
   # Verificar versão
   git --version
   ```

## 🔧 Instalação Passo a Passo

### 1. Preparação do Ambiente

#### Linux (Ubuntu/Debian)
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl

# Instalar pnpm (opcional, mas recomendado)
npm install -g pnpm
```

#### macOS
```bash
# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar dependências
brew install python@3.11 node git

# Instalar pnpm
npm install -g pnpm
```

#### Windows
```powershell
# Instalar via Chocolatey (recomendado)
# Primeiro instale o Chocolatey: https://chocolatey.org/install

choco install python nodejs git -y

# Instalar pnpm
npm install -g pnpm
```

### 2. Download do Projeto

```bash
# Opção 1: Clone via HTTPS
git clone https://github.com/seu-usuario/claudia-ai.git

# Opção 2: Clone via SSH (se configurado)
git clone git@github.com:seu-usuario/claudia-ai.git

# Entrar no diretório
cd claudia-ai
```

### 3. Configuração do Backend

```bash
# Navegar para o backend
cd claudia-ai-backend

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Atualizar pip
pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt

# Verificar instalação
python -c "import flask; print('Flask instalado com sucesso')"
python -c "import sklearn; print('Scikit-learn instalado com sucesso')"
```

### 4. Configuração do Frontend

```bash
# Navegar para o frontend (em novo terminal)
cd claudia-ai-frontend

# Instalar dependências
pnpm install
# ou
npm install

# Verificar instalação
pnpm list react
# ou
npm list react
```

### 5. Configuração do Banco de Dados

O banco SQLite é criado automaticamente na primeira execução. Para configuração manual:

```bash
# No diretório do backend
cd claudia-ai-backend

# Criar diretório do banco (se não existir)
mkdir -p src/database

# O arquivo app.db será criado automaticamente
```

### 6. Configuração de Variáveis de Ambiente

#### Backend (.env)
```bash
# Criar arquivo .env no diretório do backend
cd claudia-ai-backend
cat > .env << EOF
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///src/database/app.db
SECRET_KEY=sua-chave-secreta-aqui
CORS_ORIGINS=http://localhost:5173
LOG_LEVEL=INFO
EOF
```

#### Frontend (.env)
```bash
# Criar arquivo .env no diretório do frontend
cd claudia-ai-frontend
cat > .env << EOF
VITE_API_URL=http://localhost:5000/api
VITE_APP_NAME=Claudia.AI
VITE_APP_VERSION=1.0.0
EOF
```

## 🚀 Primeira Execução

### 1. Iniciar o Backend

```bash
cd claudia-ai-backend
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

python src/main.py
```

Você deve ver:
```
INFO:__main__:Iniciando Claudia.AI Backend...
INFO:__main__:Acesse http://localhost:5000 para a interface
INFO:__main__:API disponível em http://localhost:5000/api
 * Running on http://127.0.0.1:5000
```

### 2. Iniciar o Frontend (novo terminal)

```bash
cd claudia-ai-frontend
pnpm run dev
# ou
npm run dev
```

Você deve ver:
```
  VITE v6.3.5  ready in 614 ms
  ➜  Local:   http://localhost:5173/
  ➜  Network: http://169.254.0.21:5173/
```

### 3. Verificar Instalação

1. **Backend**: Acesse http://localhost:5000/api/health
2. **Frontend**: Acesse http://localhost:5173
3. **Integração**: Teste uma conversa na interface

## 🔍 Verificação e Testes

### Testes Automatizados

```bash
# No diretório raiz do projeto
python test_claudia_ai.py
```

### Testes Manuais

1. **Health Check**:
   ```bash
   curl http://localhost:5000/api/health
   ```

2. **Criar Usuário**:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"username": "teste", "email": "teste@teste.com"}' \
        http://localhost:5000/api/users
   ```

3. **Testar IA**:
   ```bash
   # Primeiro criar conversa
   curl -X POST -H "Content-Type: application/json" \
        -d '{"title": "Teste", "user_id": 1}' \
        http://localhost:5000/api/conversations
   
   # Depois testar geração
   curl -X POST -H "Content-Type: application/json" \
        -d '{"conversation_id": 1, "message": "Olá!", "user_id": 1}' \
        http://localhost:5000/api/ai/generate
   ```

## 🐛 Solução de Problemas

### Problemas Comuns

#### 1. Erro de Porta em Uso
```bash
# Verificar processos usando a porta
lsof -i :5000  # Backend
lsof -i :5173  # Frontend

# Matar processo se necessário
kill -9 <PID>
```

#### 2. Erro de Dependências Python
```bash
# Reinstalar dependências
pip install --force-reinstall -r requirements.txt

# Verificar versão do Python
python --version
```

#### 3. Erro de Dependências Node.js
```bash
# Limpar cache e reinstalar
rm -rf node_modules package-lock.json
npm install
# ou
pnpm install
```

#### 4. Erro de Banco de Dados
```bash
# Remover banco e recriar
rm src/database/app.db
python src/main.py  # Recriará automaticamente
```

#### 5. Erro de CORS
Verifique se o arquivo `.env` do backend tem:
```
CORS_ORIGINS=http://localhost:5173
```

### Logs de Debug

#### Backend
```bash
# Executar com logs detalhados
FLASK_DEBUG=True python src/main.py
```

#### Frontend
```bash
# Executar com logs detalhados
pnpm run dev --debug
```

## 🔧 Configurações Avançadas

### Configuração de Produção

#### Backend
```bash
# Instalar servidor WSGI
pip install gunicorn

# Executar em produção
gunicorn -w 4 -b 0.0.0.0:5000 src.main:app
```

#### Frontend
```bash
# Build para produção
pnpm run build

# Servir arquivos estáticos
pnpm run preview
```

### Configuração de Banco PostgreSQL

```bash
# Instalar driver PostgreSQL
pip install psycopg2-binary

# Atualizar .env
DATABASE_URL=postgresql://user:password@localhost/claudia_ai
```

### Configuração de Redis (Cache)

```bash
# Instalar Redis
sudo apt install redis-server  # Ubuntu
brew install redis            # macOS

# Instalar cliente Python
pip install redis

# Configurar no .env
REDIS_URL=redis://localhost:6379/0
```

## 📊 Monitoramento

### Logs

```bash
# Logs do backend
tail -f logs/claudia-ai.log

# Logs do sistema
journalctl -u claudia-ai -f  # Se usando systemd
```

### Métricas

```bash
# Verificar métricas da API
curl http://localhost:5000/api/learning/metrics
```

## 🔄 Atualizações

### Atualizar o Sistema

```bash
# Fazer backup do banco
cp src/database/app.db src/database/app.db.backup

# Atualizar código
git pull origin main

# Atualizar dependências backend
cd claudia-ai-backend
source venv/bin/activate
pip install -r requirements.txt

# Atualizar dependências frontend
cd ../claudia-ai-frontend
pnpm install

# Reiniciar serviços
```

## 🆘 Suporte

### Recursos de Ajuda

1. **Documentação**: Consulte os arquivos em `docs/`
2. **Issues**: Reporte problemas no GitHub
3. **Logs**: Sempre inclua logs ao reportar problemas
4. **Versões**: Informe versões do Python, Node.js e SO

### Informações do Sistema

```bash
# Script para coletar informações
cat > system_info.sh << 'EOF'
#!/bin/bash
echo "=== Informações do Sistema ==="
echo "OS: $(uname -a)"
echo "Python: $(python --version)"
echo "Node.js: $(node --version)"
echo "NPM: $(npm --version)"
echo "Git: $(git --version)"
echo "Espaço em disco:"
df -h
echo "Memória:"
free -h
EOF

chmod +x system_info.sh
./system_info.sh
```

---

**Instalação concluída com sucesso!** 🎉

Para próximos passos, consulte o [Manual do Usuário](USER_GUIDE.md).

