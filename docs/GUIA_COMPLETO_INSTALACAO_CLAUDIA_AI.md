# 🤖 Guia Completo de Instalação da Claudia.AI

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Requisitos do Sistema](#requisitos-do-sistema)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação Passo a Passo](#instalação-passo-a-passo)
5. [Configuração](#configuração)
6. [Execução](#execução)
7. [Verificação](#verificação)
8. [Solução de Problemas](#solução-de-problemas)
9. [Personalização](#personalização)
10. [Manutenção](#manutenção)

---

## 🎯 Visão Geral

A **Claudia.AI** é uma inteligência artificial generativa completa desenvolvida com tecnologias modernas. Este guia fornece instruções detalhadas para instalação e configuração em ambiente local.

### Características Principais

- **Interface Moderna**: Design responsivo em React com tema verde e branco
- **IA Avançada**: Suporte a múltiplos modelos (OpenAI GPT, Hugging Face, Llama)
- **Sistema de Aprendizado**: Machine learning integrado para melhoria contínua
- **Backend Robusto**: API Flask com SQLite para persistência de dados
- **Multiplataforma**: Compatível com Linux, macOS e Windows

### Arquitetura do Sistema

A Claudia.AI é composta por três componentes principais:

**Frontend (React + Vite)**
- Interface de usuário responsiva
- Sistema de chat em tempo real
- Componentes reutilizáveis com Tailwind CSS
- Integração com API backend

**Backend (Flask + Python)**
- APIs RESTful completas
- Sistema de autenticação
- Integração com modelos de IA
- Banco de dados SQLite

**Sistema de IA**
- Suporte a múltiplos provedores
- Sistema de aprendizado contínuo
- Análise de feedback e métricas
- Personalização baseada em uso

---

## 💻 Requisitos do Sistema

### Requisitos Mínimos

| Componente | Especificação Mínima |
|------------|---------------------|
| **Sistema Operacional** | Linux (Ubuntu 20.04+), macOS (10.15+), Windows 10+ |
| **Processador** | Intel i5 / AMD Ryzen 5 ou equivalente |
| **Memória RAM** | 8 GB |
| **Espaço em Disco** | 5 GB livres |
| **Conexão Internet** | Banda larga para download de dependências |

### Requisitos Recomendados

| Componente | Especificação Recomendada |
|------------|---------------------------|
| **Sistema Operacional** | Linux (Ubuntu 22.04+), macOS (12.0+), Windows 11 |
| **Processador** | Intel i7 / AMD Ryzen 7 ou superior |
| **Memória RAM** | 16 GB ou mais |
| **Espaço em Disco** | 10 GB livres |
| **GPU** | NVIDIA GTX 1060+ (para modelos locais) |

---

## 🔧 Pré-requisitos

### 1. Python 3.11+

A Claudia.AI requer Python 3.11 ou superior para funcionar corretamente.

**Verificar versão instalada:**
```bash
python3 --version
# ou
python --version
```

**Instalação no Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev python3-pip
```

**Instalação no macOS:**
```bash
# Usando Homebrew
brew install python@3.11

# Ou baixar do site oficial
# https://www.python.org/downloads/
```

**Instalação no Windows:**
1. Baixe o instalador do [site oficial do Python](https://www.python.org/downloads/)
2. Execute o instalador
3. **IMPORTANTE**: Marque "Add Python to PATH"
4. Escolha "Install Now"

### 2. Node.js 18+

O frontend React requer Node.js versão 18 ou superior.

**Verificar versão instalada:**
```bash
node --version
npm --version
```

**Instalação no Ubuntu/Debian:**
```bash
# Usando NodeSource
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Verificar instalação
node --version
npm --version
```

**Instalação no macOS:**
```bash
# Usando Homebrew
brew install node

# Ou baixar do site oficial
# https://nodejs.org/
```

**Instalação no Windows:**
1. Baixe o instalador do [site oficial do Node.js](https://nodejs.org/)
2. Execute o instalador
3. Siga as instruções padrão
4. Reinicie o terminal

### 3. Git

Necessário para clonar o repositório e gerenciar versões.

**Verificar instalação:**
```bash
git --version
```

**Instalação:**
```bash
# Ubuntu/Debian
sudo apt install git

# macOS
brew install git

# Windows: baixar de https://git-scm.com/
```

### 4. Gerenciador de Pacotes Python (pip)

Geralmente instalado junto com Python, mas pode precisar de atualização.

**Verificar e atualizar:**
```bash
python3 -m pip --version
python3 -m pip install --upgrade pip
```

### 5. PNPM (Recomendado)

Gerenciador de pacotes mais rápido que o npm.

**Instalação:**
```bash
npm install -g pnpm
```

---



## 🚀 Instalação Passo a Passo

### Passo 1: Preparação do Ambiente

Primeiro, crie um diretório para o projeto e navegue até ele:

```bash
mkdir claudia-ai-projeto
cd claudia-ai-projeto
```

### Passo 2: Estrutura do Projeto

Extraia o arquivo ZIP fornecido ou crie a estrutura manualmente:

```
claudia-ai-projeto/
├── claudia-ai-backend/          # Backend Flask
│   ├── src/
│   │   ├── models/             # Modelos de dados
│   │   ├── routes/             # APIs RESTful
│   │   ├── services/           # Serviços de IA
│   │   └── main.py            # Aplicação principal
│   ├── requirements.txt        # Dependências Python
│   ├── .env                   # Configurações de ambiente
│   └── app.py                 # Ponto de entrada
├── claudia-ai-frontend/         # Frontend React
│   ├── src/
│   │   ├── components/        # Componentes React
│   │   └── App.jsx           # Aplicação principal
│   ├── package.json          # Dependências Node.js
│   └── .env                  # Configurações frontend
├── docs/                      # Documentação
├── scripts/                   # Scripts de automação
└── README.md                  # Documentação principal
```

### Passo 3: Configuração do Backend

**3.1. Navegue para o diretório do backend:**
```bash
cd claudia-ai-backend
```

**3.2. Crie um ambiente virtual Python:**
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**Verificar se o ambiente virtual está ativo:**
- O prompt deve mostrar `(venv)` no início
- `which python` deve apontar para o diretório venv

**3.3. Instale as dependências:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Lista de dependências instaladas:**
- Flask 2.3.3 - Framework web
- Flask-SQLAlchemy 3.0.5 - ORM para banco de dados
- Flask-CORS 4.0.0 - Suporte a CORS
- SQLAlchemy 2.0.23 - Toolkit SQL
- Requests 2.31.0 - Cliente HTTP
- OpenAI 1.3.0 - API OpenAI
- Transformers 4.35.0 - Modelos Hugging Face
- Torch 2.1.0 - PyTorch para ML
- Scikit-learn 1.3.2 - Machine Learning
- Pandas 2.1.3 - Manipulação de dados
- NumPy 1.25.2 - Computação numérica

**3.4. Configure as variáveis de ambiente:**

Edite o arquivo `.env` no diretório backend:
```bash
# Configurações da aplicação
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui

# Configurações do banco de dados
DATABASE_URL=sqlite:///src/database/app.db

# Configurações da IA (opcional)
OPENAI_API_KEY=sua-chave-openai-aqui
HUGGINGFACE_API_KEY=sua-chave-huggingface-aqui

# Configurações do servidor
HOST=0.0.0.0
PORT=5000
```

**Importante sobre as chaves de API:**
- As chaves são opcionais para o modo demonstração
- Para usar IA real, obtenha chaves em:
  - OpenAI: https://platform.openai.com/api-keys
  - Hugging Face: https://huggingface.co/settings/tokens

### Passo 4: Configuração do Frontend

**4.1. Abra um novo terminal e navegue para o frontend:**
```bash
cd claudia-ai-frontend
```

**4.2. Instale as dependências:**
```bash
# Usando PNPM (recomendado)
pnpm install

# Ou usando NPM
npm install

# Ou usando Yarn
yarn install
```

**Lista de dependências instaladas:**
- React 18.2.0 - Biblioteca de interface
- Vite 4.5.0 - Build tool e dev server
- Tailwind CSS 3.3.5 - Framework CSS
- Axios 1.6.0 - Cliente HTTP
- Lucide React 0.292.0 - Ícones
- Class Variance Authority 0.7.0 - Utilitário CSS

**4.3. Configure as variáveis de ambiente:**

Edite o arquivo `.env` no diretório frontend:
```bash
# URL da API backend
VITE_API_URL=http://localhost:5000

# Configurações de desenvolvimento
VITE_APP_NAME=Claudia.AI
VITE_APP_VERSION=1.0.0

# Configurações de produção (opcional)
VITE_PRODUCTION_API_URL=https://sua-api-producao.com
```

### Passo 5: Inicialização do Banco de Dados

**5.1. Volte para o diretório do backend:**
```bash
cd ../claudia-ai-backend
source venv/bin/activate  # Linux/macOS
# ou venv\Scripts\activate  # Windows
```

**5.2. Crie o banco de dados:**
```bash
python -c "
from src.main import create_app
from src.models.user import db
import os

# Criar diretório do banco se não existir
os.makedirs('src/database', exist_ok=True)

# Criar aplicação e banco
app = create_app()
with app.app_context():
    db.create_all()
    print('✅ Banco de dados criado com sucesso!')
    print('📁 Localização: src/database/app.db')
"
```

**5.3. Verificar criação do banco:**
```bash
ls -la src/database/
# Deve mostrar: app.db
```

### Passo 6: Teste da Instalação

**6.1. Teste o backend:**
```bash
# No diretório claudia-ai-backend com venv ativo
python src/main.py
```

Você deve ver:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
INFO:claudia_ai:Aplicação iniciada em modo desenvolvimento
INFO:claudia_ai:Banco de dados inicializado
```

**6.2. Teste a API (em outro terminal):**
```bash
curl http://localhost:5000/api/health
# Resposta esperada: {"status": "healthy", "timestamp": "..."}
```

**6.3. Teste o frontend:**
```bash
# Em outro terminal, no diretório claudia-ai-frontend
pnpm run dev
# ou npm run dev
```

Você deve ver:
```
  VITE v4.5.0  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**6.4. Acesse a aplicação:**
Abra o navegador e acesse: http://localhost:5173

Você deve ver a interface da Claudia.AI com:
- Header verde com logo
- Sidebar para conversas
- Área de chat central
- Campo de entrada de mensagem

---

## ⚙️ Configuração

### Configurações do Backend

O arquivo `.env` no backend controla diversos aspectos da aplicação:

**Configurações de Desenvolvimento:**
```bash
FLASK_ENV=development          # Modo de desenvolvimento
FLASK_DEBUG=True              # Debug ativo
LOG_LEVEL=INFO                # Nível de log
```

**Configurações de Produção:**
```bash
FLASK_ENV=production          # Modo de produção
FLASK_DEBUG=False             # Debug desativo
LOG_LEVEL=WARNING             # Log apenas warnings/errors
SECRET_KEY=chave-super-secreta # Chave de segurança forte
```

**Configurações de IA:**
```bash
# Modo de operação da IA
AI_MODEL_TYPE=demo                # demo, openai, huggingface, llama

# Configurações OpenAI
OPENAI_API_KEY=sk-...             # Sua chave da OpenAI
OPENAI_MODEL=gpt-3.5-turbo        # Modelo a usar

# Configurações Hugging Face
HUGGINGFACE_API_KEY=hf_...        # Sua chave do HF
HUGGINGFACE_MODEL=microsoft/DialoGPT-large

# Configurações para modelo Llama local
AI_MODEL_NAME=Llama3.3-70B-Instruct
LLAMA_MODEL_PATH=/path/to/model
```

**Configurações de Banco:**
```bash
# SQLite (padrão)
DATABASE_URL=sqlite:///src/database/app.db

# PostgreSQL (produção)
DATABASE_URL=postgresql://user:pass@localhost/claudia_ai

# MySQL (alternativa)
DATABASE_URL=mysql://user:pass@localhost/claudia_ai
```

### Configurações do Frontend

O arquivo `.env` no frontend configura a conexão com o backend:

```bash
# URL da API (desenvolvimento)
VITE_API_URL=http://localhost:5000

# URL da API (produção)
VITE_API_URL=https://api.claudia-ai.com

# Configurações da aplicação
VITE_APP_NAME=Claudia.AI
VITE_APP_VERSION=1.0.0
VITE_APP_DESCRIPTION=Inteligência Artificial Generativa

# Configurações de interface
VITE_THEME=green              # green, blue, purple
VITE_LANGUAGE=pt-BR           # pt-BR, en-US, es-ES
```

### Personalização da Interface

**Cores do Tema (Tailwind CSS):**

Edite `claudia-ai-frontend/tailwind.config.js`:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        // Tema Verde (padrão)
        primary: {
          50: '#f0fdf4',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d',
        },
        // Tema personalizado
        claudia: {
          green: '#2D5A27',
          lightGreen: '#4A7C59',
          accent: '#7FB069',
          background: '#ffffff',
          text: '#1f2937',
        }
      }
    }
  }
}
```

**Fontes Personalizadas:**

Edite `claudia-ai-frontend/index.html`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

---

## ▶️ Execução

### Método 1: Execução Manual

**Terminal 1 - Backend:**
```bash
cd claudia-ai-backend
source venv/bin/activate  # Linux/macOS
# ou venv\Scripts\activate  # Windows
python src/main.py
```

**Terminal 2 - Frontend:**
```bash
cd claudia-ai-frontend
pnpm run dev
# ou npm run dev
```

### Método 2: Scripts Automatizados

**Script de Inicialização (Linux/macOS):**

Crie `start-claudia.sh`:
```bash
#!/bin/bash
echo "🚀 Iniciando Claudia.AI..."

# Iniciar backend
cd claudia-ai-backend
source venv/bin/activate
python src/main.py &
BACKEND_PID=$!

# Aguardar backend inicializar
sleep 5

# Iniciar frontend
cd ../claudia-ai-frontend
pnpm run dev &
FRONTEND_PID=$!

echo "✅ Claudia.AI iniciada!"
echo "🌐 Frontend: http://localhost:5173"
echo "🔧 Backend: http://localhost:5000"
echo ""
echo "Para parar, pressione Ctrl+C"

# Aguardar sinal de interrupção
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
```

**Tornar executável e usar:**
```bash
chmod +x start-claudia.sh
./start-claudia.sh
```

**Script de Parada:**

Crie `stop-claudia.sh`:
```bash
#!/bin/bash
echo "⏹️ Parando Claudia.AI..."

# Parar processos Python (backend)
pkill -f "python src/main.py"

# Parar processos Node (frontend)
pkill -f "vite"

echo "✅ Claudia.AI parada!"
```

### Método 3: Docker (Avançado)

**Dockerfile para Backend:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "src/main.py"]
```

**Dockerfile para Frontend:**
```dockerfile
FROM node:20-alpine

WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install

COPY . .
EXPOSE 5173

CMD ["pnpm", "run", "dev", "--host"]
```

**Docker Compose:**
```yaml
version: '3.8'
services:
  backend:
    build: ./claudia-ai-backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
    volumes:
      - ./claudia-ai-backend:/app

  frontend:
    build: ./claudia-ai-frontend
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:5000
    volumes:
      - ./claudia-ai-frontend:/app
    depends_on:
      - backend
```

**Executar com Docker:**
```bash
docker-compose up -d
```

---


## ✅ Verificação

### Checklist de Verificação Completa

**1. Verificação do Backend:**
```bash
# Teste de saúde da API
curl http://localhost:5000/api/health
# Resposta esperada: {"status": "healthy", "timestamp": "..."}

# Teste de informações da API
curl http://localhost:5000/api/info
# Deve retornar informações sobre endpoints disponíveis

# Teste de status da IA
curl http://localhost:5000/api/ai/status
# Deve retornar status do sistema de IA
```

**2. Verificação do Frontend:**
- Acesse http://localhost:5173
- Verifique se a página carrega sem erros
- Teste a criação de nova conversa
- Envie uma mensagem de teste
- Verifique se recebe resposta da IA

**3. Verificação da Integração:**
```bash
# Teste de conversa via API
curl -X POST http://localhost:5000/api/ai/generate \
  -H "Content-Type: application/json" \
  -d '{"message": "Olá, como você está?"}'
```

**4. Verificação do Banco de Dados:**
```bash
# Verificar se o arquivo existe
ls -la claudia-ai-backend/src/database/app.db

# Explorar tabelas (opcional)
sqlite3 claudia-ai-backend/src/database/app.db ".tables"
```

**5. Logs e Monitoramento:**
```bash
# Ver logs do backend
tail -f claudia-ai-backend/logs/app.log

# Ver logs em tempo real
cd claudia-ai-backend
source venv/bin/activate
python src/main.py
# Observe os logs no terminal
```

### Indicadores de Sucesso

**Interface Funcionando:**
- ✅ Header verde com logo "Claudia.AI"
- ✅ Sidebar com opção "Nova Conversa"
- ✅ Área de chat central
- ✅ Campo de entrada responsivo
- ✅ Indicador de status da IA

**Backend Funcionando:**
- ✅ Servidor Flask rodando na porta 5000
- ✅ Banco de dados SQLite criado
- ✅ APIs respondendo corretamente
- ✅ Logs sem erros críticos

**Integração Funcionando:**
- ✅ Frontend conectando com backend
- ✅ Mensagens sendo enviadas e recebidas
- ✅ Conversas sendo salvas no banco
- ✅ IA respondendo (modo demo ou real)

---

## 🔧 Solução de Problemas

### Problemas Comuns do Backend

**Erro: "ModuleNotFoundError: No module named 'flask'"**
```bash
# Solução: Verificar se o ambiente virtual está ativo
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Reinstalar dependências
pip install -r requirements.txt
```

**Erro: "Permission denied" ao criar banco de dados**
```bash
# Solução: Criar diretório com permissões corretas
mkdir -p src/database
chmod 755 src/database

# Verificar permissões do diretório pai
ls -la src/
```

**Erro: "Port 5000 already in use"**
```bash
# Solução 1: Encontrar e parar processo
lsof -ti:5000 | xargs kill -9

# Solução 2: Usar porta diferente
export PORT=5001
python src/main.py
```

**Erro: "SQLAlchemy database locked"**
```bash
# Solução: Parar todos os processos e remover lock
pkill -f python
rm -f src/database/app.db-journal
```

**Erro: "CORS policy" no navegador**
```bash
# Verificar se CORS está configurado no backend
# Arquivo src/main.py deve conter:
from flask_cors import CORS
CORS(app, origins=['http://localhost:5173'])
```

### Problemas Comuns do Frontend

**Erro: "command not found: pnpm"**
```bash
# Solução: Instalar PNPM
npm install -g pnpm

# Ou usar npm diretamente
npm install
npm run dev
```

**Erro: "Network Error" ao conectar com backend**
```bash
# Verificar se backend está rodando
curl http://localhost:5000/api/health

# Verificar configuração da API no .env
cat .env
# VITE_API_URL deve apontar para o backend correto
```

**Erro: "Failed to resolve import"**
```bash
# Solução: Limpar cache e reinstalar
rm -rf node_modules
rm pnpm-lock.yaml
pnpm install
```

**Erro: "Port 5173 already in use"**
```bash
# Solução: Usar porta diferente
pnpm run dev --port 3000
```

### Problemas de Integração com IA

**IA não responde (modo OpenAI)**
```bash
# Verificar chave da API
echo $OPENAI_API_KEY

# Testar chave manualmente
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**IA não responde (modo Hugging Face)**
```bash
# Verificar chave do HF
echo $HUGGINGFACE_API_KEY

# Testar modelo
curl https://api-inference.huggingface.co/models/microsoft/DialoGPT-large \
  -H "Authorization: Bearer $HUGGINGFACE_API_KEY" \
  -d '{"inputs": "Hello"}'
```

**Modo demo não funciona**
```bash
# Verificar configuração
grep AI_MODEL_TYPE claudia-ai-backend/.env
# Deve ser: AI_MODEL_TYPE=demo

# Reiniciar backend
pkill -f python
cd claudia-ai-backend
source venv/bin/activate
python src/main.py
```

### Problemas de Performance

**Backend lento**
```bash
# Verificar recursos do sistema
htop
# ou
top

# Verificar logs de performance
tail -f claudia-ai-backend/logs/app.log | grep "slow"
```

**Frontend lento**
```bash
# Verificar build de desenvolvimento
pnpm run build
pnpm run preview

# Verificar tamanho dos bundles
pnpm run build -- --analyze
```

**Banco de dados lento**
```bash
# Verificar tamanho do banco
ls -lh src/database/app.db

# Limpar dados antigos (cuidado!)
sqlite3 src/database/app.db "DELETE FROM messages WHERE created_at < datetime('now', '-30 days');"
```

### Problemas de Conectividade

**Firewall bloqueando conexões**
```bash
# Linux: Permitir portas
sudo ufw allow 5000
sudo ufw allow 5173

# macOS: Verificar firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# Windows: Verificar Windows Defender
# Ir para Configurações > Rede e Internet > Firewall do Windows Defender
```

**Proxy corporativo**
```bash
# Configurar proxy para pip
pip install --proxy http://proxy:port -r requirements.txt

# Configurar proxy para npm/pnpm
npm config set proxy http://proxy:port
npm config set https-proxy http://proxy:port
```

### Logs e Debugging

**Ativar logs detalhados:**
```bash
# Backend: editar .env
LOG_LEVEL=DEBUG
FLASK_DEBUG=True

# Frontend: executar com debug
pnpm run dev -- --debug
```

**Localização dos logs:**
```bash
# Logs do backend
claudia-ai-backend/logs/app.log
claudia-ai-backend/logs/error.log

# Logs do frontend (console do navegador)
# Pressione F12 > Console
```

**Comandos úteis para debug:**
```bash
# Verificar processos rodando
ps aux | grep python
ps aux | grep node

# Verificar portas em uso
netstat -tulpn | grep :5000
netstat -tulpn | grep :5173

# Verificar conectividade
telnet localhost 5000
telnet localhost 5173
```

---

## 🎨 Personalização

### Personalização da Interface

**Mudança de Cores:**

Edite `claudia-ai-frontend/src/index.css`:
```css
:root {
  /* Tema Verde (padrão) */
  --primary-color: #2D5A27;
  --secondary-color: #4A7C59;
  --accent-color: #7FB069;
  
  /* Tema Azul (alternativo) */
  --primary-color: #1e40af;
  --secondary-color: #3b82f6;
  --accent-color: #60a5fa;
  
  /* Tema Roxo (alternativo) */
  --primary-color: #7c3aed;
  --secondary-color: #8b5cf6;
  --accent-color: #a78bfa;
}
```

**Personalização do Logo:**

Substitua o arquivo `claudia-ai-frontend/public/claudia-icon.svg`:
```svg
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Seu logo personalizado aqui -->
  <circle cx="50" cy="50" r="40" fill="#2D5A27"/>
  <text x="50" y="55" text-anchor="middle" fill="white" font-size="20">C</text>
</svg>
```

**Mudança de Fontes:**

Edite `claudia-ai-frontend/index.html`:
```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">

<!-- Ou fontes locais -->
<style>
@font-face {
  font-family: 'MinhaFonte';
  src: url('./assets/fonts/minha-fonte.woff2') format('woff2');
}
</style>
```

**Layout Responsivo:**

Edite `claudia-ai-frontend/src/App.jsx`:
```jsx
// Personalizar breakpoints
const isMobile = window.innerWidth < 768;
const isTablet = window.innerWidth >= 768 && window.innerWidth < 1024;
const isDesktop = window.innerWidth >= 1024;
```

### Personalização do Backend

**Adicionar Novos Endpoints:**

Crie `claudia-ai-backend/src/routes/custom.py`:
```python
from flask import Blueprint, jsonify, request
from src.models.user import db

custom_bp = Blueprint('custom', __name__)

@custom_bp.route('/api/custom/minha-funcao', methods=['POST'])
def minha_funcao():
    data = request.get_json()
    # Sua lógica personalizada aqui
    return jsonify({"resultado": "sucesso"})
```

Registre no `src/main.py`:
```python
from src.routes.custom import custom_bp
app.register_blueprint(custom_bp)
```

**Personalizar Respostas da IA:**

Edite `claudia-ai-backend/src/services/ai_service.py`:
```python
def personalizar_resposta(self, resposta_original, contexto_usuario):
    """Personaliza resposta baseada no perfil do usuário"""
    
    # Adicionar personalidade
    if contexto_usuario.get('preferencia') == 'formal':
        resposta_original = f"Prezado usuário, {resposta_original}"
    elif contexto_usuario.get('preferencia') == 'casual':
        resposta_original = f"Oi! {resposta_original} 😊"
    
    return resposta_original
```

**Adicionar Novos Modelos de IA:**

Edite `claudia-ai-backend/src/services/ai_service.py`:
```python
def _generate_with_custom_model(self, message, conversation_id=None):
    """Integração com modelo personalizado"""
    
    # Exemplo: Integração com Ollama local
    import requests
    
    response = requests.post('http://localhost:11434/api/generate', json={
        'model': 'llama2',
        'prompt': message,
        'stream': False
    })
    
    return response.json()['response']
```

### Personalização do Banco de Dados

**Adicionar Novas Tabelas:**

Crie `claudia-ai-backend/src/models/custom.py`:
```python
from src.models.user import db
from datetime import datetime

class MinhaTabela(db.Model):
    __tablename__ = 'minha_tabela'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dados = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'dados': self.dados,
            'created_at': self.created_at.isoformat()
        }
```

**Migração de Dados:**

Crie script `migrate.py`:
```python
from src.main import create_app
from src.models.user import db
from src.models.custom import MinhaTabela

app = create_app()
with app.app_context():
    # Criar novas tabelas
    db.create_all()
    
    # Migrar dados existentes
    # Sua lógica de migração aqui
    
    print("Migração concluída!")
```

### Integração com Modelos Locais

**Configurar Ollama:**
```bash
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Baixar modelo
ollama pull llama2

# Testar
ollama run llama2 "Olá, como você está?"
```

**Integrar no Backend:**
```python
# src/services/ai_service.py
def _generate_with_ollama(self, message, conversation_id=None):
    import requests
    
    response = requests.post('http://localhost:11434/api/generate', json={
        'model': 'llama2',
        'prompt': message,
        'stream': False
    })
    
    return response.json()['response']
```

**Configurar Hugging Face Transformers Local:**
```python
# src/services/ai_service.py
from transformers import AutoTokenizer, AutoModelForCausalLM

class LocalHuggingFaceService:
    def __init__(self, model_name="microsoft/DialoGPT-large"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
    
    def generate_response(self, message):
        inputs = self.tokenizer.encode(message, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
```

---

## 🔧 Manutenção

### Backup e Restauração

**Backup do Banco de Dados:**
```bash
# Backup completo
cp claudia-ai-backend/src/database/app.db backup_$(date +%Y%m%d_%H%M%S).db

# Backup com compressão
tar -czf backup_claudia_$(date +%Y%m%d).tar.gz claudia-ai-backend/src/database/

# Backup automático (crontab)
# 0 2 * * * /path/to/backup-script.sh
```

**Script de Backup Automático:**
```bash
#!/bin/bash
# backup-script.sh

BACKUP_DIR="/home/backup/claudia-ai"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Backup do banco
cp claudia-ai-backend/src/database/app.db $BACKUP_DIR/app_$DATE.db

# Backup dos logs
tar -czf $BACKUP_DIR/logs_$DATE.tar.gz claudia-ai-backend/logs/

# Limpar backups antigos (manter últimos 30 dias)
find $BACKUP_DIR -name "*.db" -mtime +30 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete

echo "Backup concluído: $DATE"
```

**Restauração:**
```bash
# Parar aplicação
./stop-claudia.sh

# Restaurar banco
cp backup_20240131_120000.db claudia-ai-backend/src/database/app.db

# Reiniciar aplicação
./start-claudia.sh
```

### Atualizações

**Atualizar Dependências Python:**
```bash
cd claudia-ai-backend
source venv/bin/activate

# Verificar atualizações disponíveis
pip list --outdated

# Atualizar todas
pip install --upgrade -r requirements.txt

# Ou atualizar específica
pip install --upgrade flask
```

**Atualizar Dependências Node.js:**
```bash
cd claudia-ai-frontend

# Verificar atualizações
pnpm outdated

# Atualizar todas
pnpm update

# Ou atualizar específica
pnpm add react@latest
```

**Atualizar Código:**
```bash
# Se usando Git
git pull origin main

# Reinstalar dependências se necessário
cd claudia-ai-backend && pip install -r requirements.txt
cd claudia-ai-frontend && pnpm install
```

### Monitoramento

**Monitoramento de Recursos:**
```bash
# CPU e Memória
htop

# Espaço em disco
df -h

# Processos da Claudia.AI
ps aux | grep -E "(python|node)" | grep -E "(claudia|5000|5173)"
```

**Monitoramento de Logs:**
```bash
# Logs em tempo real
tail -f claudia-ai-backend/logs/app.log

# Filtrar erros
tail -f claudia-ai-backend/logs/app.log | grep ERROR

# Estatísticas de uso
grep "POST /api/ai/generate" claudia-ai-backend/logs/app.log | wc -l
```

**Script de Monitoramento:**
```bash
#!/bin/bash
# monitor-claudia.sh

echo "=== Status da Claudia.AI ==="
echo "Data: $(date)"
echo ""

# Verificar processos
echo "Processos:"
ps aux | grep -E "(python.*main.py|node.*vite)" | grep -v grep

echo ""

# Verificar portas
echo "Portas:"
netstat -tulpn | grep -E ":5000|:5173"

echo ""

# Verificar saúde da API
echo "Saúde da API:"
curl -s http://localhost:5000/api/health | jq .

echo ""

# Verificar uso de recursos
echo "Recursos:"
free -h
df -h | grep -E "/$|/home"
```

### Otimização

**Otimização do Backend:**
```python
# src/main.py - Configurações de produção
app.config.update(
    # Cache
    SEND_FILE_MAX_AGE_DEFAULT=31536000,  # 1 ano
    
    # Compressão
    COMPRESS_MIMETYPES=[
        'text/html', 'text/css', 'text/xml',
        'application/json', 'application/javascript'
    ],
    
    # Segurança
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)
```

**Otimização do Frontend:**
```javascript
// vite.config.js - Build otimizado
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['lucide-react', '@radix-ui/react-scroll-area']
        }
      }
    },
    chunkSizeWarningLimit: 1000
  }
})
```

**Otimização do Banco:**
```sql
-- Índices para melhor performance
CREATE INDEX idx_messages_conversation_id ON messages(conversation_id);
CREATE INDEX idx_messages_created_at ON messages(created_at);
CREATE INDEX idx_conversations_user_id ON conversations(user_id);
```

### Segurança

**Configurações de Segurança:**
```bash
# .env - Configurações seguras
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
SESSION_COOKIE_SECURE=True
CSRF_ENABLED=True
```

**Firewall:**
```bash
# Configurar UFW (Linux)
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 5000  # Backend (apenas local)
sudo ufw allow 5173  # Frontend (apenas local)
```

**SSL/HTTPS (Produção):**
```bash
# Usando Certbot
sudo apt install certbot
sudo certbot certonly --standalone -d seu-dominio.com

# Configurar nginx
sudo nano /etc/nginx/sites-available/claudia-ai
```

---

## 📚 Referências e Recursos Adicionais

### Documentação Oficial

- **Flask**: https://flask.palletsprojects.com/
- **React**: https://react.dev/
- **Vite**: https://vitejs.dev/
- **Tailwind CSS**: https://tailwindcss.com/
- **SQLAlchemy**: https://sqlalchemy.org/
- **OpenAI API**: https://platform.openai.com/docs
- **Hugging Face**: https://huggingface.co/docs

### Tutoriais e Guias

- **Python Virtual Environments**: https://docs.python.org/3/tutorial/venv.html
- **Node.js Package Management**: https://docs.npmjs.com/
- **SQLite Tutorial**: https://www.sqlitetutorial.net/
- **React Hooks**: https://react.dev/reference/react
- **Flask-SQLAlchemy**: https://flask-sqlalchemy.palletsprojects.com/

### Comunidade e Suporte

- **Stack Overflow**: https://stackoverflow.com/
- **GitHub Issues**: Para reportar problemas
- **Discord/Slack**: Comunidades de desenvolvedores
- **Reddit**: r/flask, r/reactjs, r/MachineLearning

### Ferramentas Úteis

- **Postman**: Teste de APIs
- **SQLite Browser**: Visualizar banco de dados
- **React DevTools**: Debug do React
- **Flask-Admin**: Interface administrativa
- **Sentry**: Monitoramento de erros

---

## 🎯 Conclusão

Este guia fornece todas as informações necessárias para instalar, configurar e personalizar a Claudia.AI em seu ambiente local. A aplicação foi desenvolvida com foco em:

- **Facilidade de instalação** com scripts automatizados
- **Documentação completa** para todos os níveis de usuário
- **Arquitetura modular** permitindo fácil personalização
- **Suporte a múltiplos modelos** de IA
- **Interface moderna** e responsiva
- **Sistema de aprendizado** contínuo

Para suporte adicional ou contribuições, consulte a documentação do projeto ou entre em contato com a comunidade de desenvolvedores.

**Versão do Guia**: 1.0.0  
**Última Atualização**: Janeiro 2024  
**Autor**: Manus AI

---

*Este documento é parte do projeto Claudia.AI - Inteligência Artificial Generativa de código aberto.*

