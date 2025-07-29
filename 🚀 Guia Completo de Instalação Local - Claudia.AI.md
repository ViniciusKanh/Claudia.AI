# 🚀 Guia Completo de Instalação Local - Claudia.AI

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Requisitos do Sistema](#requisitos-do-sistema)
3. [Instalação Passo a Passo](#instalação-passo-a-passo)
4. [Configuração do Backend](#configuração-do-backend)
5. [Configuração do Frontend](#configuração-do-frontend)
6. [Execução da Aplicação](#execução-da-aplicação)
7. [Solução de Problemas](#solução-de-problemas)
8. [Scripts Automatizados](#scripts-automatizados)
9. [Personalização e Expansão](#personalização-e-expansão)
10. [Referências](#referências)

---

## 🎯 Visão Geral

A Claudia.AI é uma inteligência artificial generativa completa desenvolvida com arquitetura moderna, utilizando React para o frontend e Flask para o backend. Este guia fornece instruções detalhadas para instalar e executar a aplicação em seu ambiente local de desenvolvimento.

### Arquitetura da Aplicação

A Claudia.AI foi projetada com uma arquitetura de microserviços separando claramente as responsabilidades entre frontend e backend. O frontend React oferece uma interface de usuário moderna e responsiva, enquanto o backend Flask fornece APIs RESTful robustas para processamento de dados e integração com modelos de inteligência artificial.

O sistema utiliza SQLite como banco de dados local para desenvolvimento, oferecendo simplicidade de configuração sem comprometer a funcionalidade. A aplicação está preparada para integração com modelos de linguagem avançados como o Llama 3.1 70B, proporcionando capacidades conversacionais sofisticadas.

### Funcionalidades Principais

A aplicação oferece um sistema completo de chat conversacional com interface intuitiva, sistema de histórico de conversas, feedback de usuários e métricas de qualidade. O design sustentável em tons de verde e branco reflete valores ecológicos, enquanto a arquitetura responsiva garante funcionamento perfeito em dispositivos móveis e desktop.

O sistema de aprendizado contínuo permite que a IA se adapte às preferências do usuário ao longo do tempo, oferecendo respostas cada vez mais personalizadas e relevantes. As APIs RESTful facilitam a integração com outros sistemas e permitem expansões futuras da funcionalidade.

---


## 💻 Requisitos do Sistema

### Requisitos Mínimos de Hardware

Para executar a Claudia.AI localmente, seu sistema deve atender aos seguintes requisitos mínimos de hardware. Estes requisitos garantem que a aplicação funcione adequadamente durante o desenvolvimento e testes locais.

**Processador**: CPU de 64 bits com pelo menos 2 núcleos e frequência mínima de 2.0 GHz. Processadores Intel Core i3 ou AMD Ryzen 3 de gerações recentes são adequados para desenvolvimento básico.

**Memória RAM**: Mínimo de 4 GB de RAM, sendo recomendados 8 GB ou mais para melhor performance. O Node.js e o Python podem consumir quantidades significativas de memória durante o desenvolvimento, especialmente ao executar ferramentas de build e hot-reload.

**Armazenamento**: Pelo menos 2 GB de espaço livre em disco para instalação das dependências e arquivos do projeto. Um SSD é altamente recomendado para melhor performance de I/O durante a instalação de pacotes e execução da aplicação.

**Conexão de Internet**: Conexão estável para download de dependências durante a instalação inicial. Após a instalação, a aplicação pode funcionar offline para desenvolvimento local.

### Requisitos Recomendados

Para uma experiência de desenvolvimento otimizada, especialmente ao trabalhar com modelos de IA mais complexos, recomendamos configurações superiores.

**Processador**: CPU de 64 bits com 4 ou mais núcleos, como Intel Core i5/i7 ou AMD Ryzen 5/7. Processadores mais potentes aceleram significativamente o processo de build e hot-reload durante o desenvolvimento.

**Memória RAM**: 16 GB ou mais para desenvolvimento confortável, especialmente se você planeja executar múltiplas instâncias da aplicação ou trabalhar com modelos de IA locais.

**Armazenamento**: SSD com pelo menos 10 GB de espaço livre. O desenvolvimento web moderno pode gerar muitos arquivos temporários e caches que se beneficiam da velocidade de um SSD.

**GPU**: Embora não seja obrigatória para a versão básica, uma GPU dedicada pode ser útil se você planeja integrar modelos de IA que se beneficiam de aceleração por GPU.

### Sistemas Operacionais Suportados

A Claudia.AI foi testada e é totalmente compatível com os seguintes sistemas operacionais:

**Windows**: Windows 10 versão 1903 ou superior, Windows 11. O Windows Subsystem for Linux (WSL2) é altamente recomendado para uma experiência de desenvolvimento mais próxima ao ambiente de produção Linux.

**macOS**: macOS 10.15 (Catalina) ou superior. O macOS oferece excelente compatibilidade com as ferramentas de desenvolvimento Node.js e Python utilizadas no projeto.

**Linux**: Distribuições baseadas em Ubuntu 18.04+, Debian 10+, CentOS 7+, Fedora 30+, ou equivalentes. Linux é o ambiente preferido para desenvolvimento, oferecendo melhor performance e compatibilidade com ferramentas de linha de comando.

### Software Pré-requisito

Antes de iniciar a instalação da Claudia.AI, você deve ter os seguintes softwares instalados em seu sistema:

**Node.js**: Versão 18.0.0 ou superior. O Node.js é essencial para executar o frontend React e suas ferramentas de build. Recomendamos usar a versão LTS mais recente para máxima estabilidade.

**Python**: Versão 3.8 ou superior, sendo recomendado Python 3.11 para melhor compatibilidade com as bibliotecas de machine learning. O Python é necessário para executar o backend Flask e suas dependências.

**Git**: Sistema de controle de versão para clonar o repositório e gerenciar alterações no código. Git 2.20 ou superior é recomendado.

**Editor de Código**: Embora não seja obrigatório, recomendamos Visual Studio Code, PyCharm, ou outro editor moderno com suporte a Python e JavaScript para melhor experiência de desenvolvimento.

### Gerenciadores de Pacotes

O projeto utiliza gerenciadores de pacotes específicos para cada tecnologia, garantindo instalação consistente e reproduzível das dependências.

**pnpm**: Gerenciador de pacotes para Node.js, oferecendo instalação mais rápida e eficiente que npm ou yarn. Se você não tiver pnpm instalado, pode usar npm como alternativa.

**pip**: Gerenciador de pacotes padrão do Python, usado para instalar as dependências do backend Flask. Vem incluído com instalações modernas do Python.

**venv**: Ferramenta de ambiente virtual do Python para isolar dependências do projeto. Essencial para evitar conflitos entre diferentes projetos Python.

---


## 🔧 Instalação Passo a Passo

### Passo 1: Preparação do Ambiente

Antes de iniciar a instalação da Claudia.AI, é fundamental preparar adequadamente seu ambiente de desenvolvimento. Este processo envolve a verificação e instalação dos softwares pré-requisitos, bem como a configuração de ferramentas essenciais.

Primeiro, verifique se você possui as versões corretas do Node.js e Python instaladas em seu sistema. Abra um terminal ou prompt de comando e execute os seguintes comandos para verificar as versões:

```bash
node --version
python --version
# ou python3 --version em sistemas Linux/macOS
```

Se o Node.js não estiver instalado ou estiver em uma versão inferior à 18.0.0, visite o site oficial do Node.js (https://nodejs.org) e baixe a versão LTS mais recente. Para Python, se não estiver instalado ou estiver em versão inferior à 3.8, visite python.org e baixe a versão mais recente.

Em sistemas Windows, recomendamos fortemente a instalação do Windows Subsystem for Linux (WSL2) para uma experiência de desenvolvimento mais consistente. O WSL2 pode ser instalado através do Microsoft Store ou seguindo a documentação oficial da Microsoft.

### Passo 2: Instalação do Git

O Git é essencial para clonar o repositório da Claudia.AI e gerenciar versões do código. Se você ainda não possui Git instalado, siga as instruções específicas para seu sistema operacional:

**Windows**: Baixe o Git for Windows do site oficial (https://git-scm.com/download/win) e execute o instalador. Durante a instalação, aceite as configurações padrão, que são adequadas para a maioria dos usuários.

**macOS**: O Git pode ser instalado através do Xcode Command Line Tools executando `xcode-select --install` no terminal, ou através do Homebrew com `brew install git`.

**Linux**: Use o gerenciador de pacotes da sua distribuição. No Ubuntu/Debian: `sudo apt update && sudo apt install git`. No CentOS/RHEL: `sudo yum install git` ou `sudo dnf install git`.

Após a instalação, configure seu nome de usuário e email do Git:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### Passo 3: Clonagem do Repositório

Com o Git configurado, você pode clonar o repositório da Claudia.AI para sua máquina local. Escolha um diretório apropriado para seus projetos e execute o comando de clonagem.

Navegue até o diretório onde deseja instalar o projeto e execute:

```bash
# Crie um diretório para o projeto (opcional)
mkdir claudia-ai-local
cd claudia-ai-local

# Clone os repositórios (você precisará dos arquivos do projeto)
# Como o projeto foi desenvolvido localmente, você precisará copiar os arquivos
# ou criar a estrutura manualmente seguindo a arquitetura descrita
```

Como a Claudia.AI foi desenvolvida como um projeto local, você precisará criar a estrutura de diretórios manualmente ou copiar os arquivos do projeto existente. A estrutura básica deve incluir dois diretórios principais: `claudia-ai-backend` para o servidor Flask e `claudia-ai-frontend` para a aplicação React.

### Passo 4: Instalação do pnpm (Opcional mas Recomendado)

O pnpm é um gerenciador de pacotes mais eficiente que o npm padrão, oferecendo instalação mais rápida e melhor gerenciamento de espaço em disco. Para instalar o pnpm globalmente:

```bash
npm install -g pnpm
```

Se você preferir usar npm em vez de pnpm, todas as instruções podem ser adaptadas substituindo `pnpm` por `npm` nos comandos.

### Passo 5: Verificação da Instalação

Após completar os passos anteriores, verifique se todas as ferramentas estão funcionando corretamente:

```bash
# Verificar versões instaladas
node --version    # Deve mostrar v18.0.0 ou superior
python --version  # Deve mostrar 3.8.0 ou superior
git --version     # Deve mostrar a versão do Git
pnpm --version    # Deve mostrar a versão do pnpm (se instalado)
```

Se todos os comandos retornarem as versões esperadas, seu ambiente está pronto para a instalação da Claudia.AI. Caso algum comando falhe, revise os passos de instalação correspondentes antes de prosseguir.

### Passo 6: Criação da Estrutura do Projeto

Para começar com a Claudia.AI, você precisará criar a estrutura básica do projeto. Crie os diretórios principais:

```bash
mkdir claudia-ai-project
cd claudia-ai-project
mkdir claudia-ai-backend claudia-ai-frontend
```

Esta estrutura separada permite desenvolvimento independente do frontend e backend, facilitando a manutenção e deploy da aplicação.

---


## ⚙️ Configuração do Backend

### Estrutura do Backend Flask

O backend da Claudia.AI é construído com Flask, um framework web minimalista e flexível para Python. A arquitetura do backend segue padrões modernos de desenvolvimento, com separação clara de responsabilidades entre modelos, rotas, serviços e configurações.

A estrutura de diretórios do backend é organizada da seguinte forma:

```
claudia-ai-backend/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Arquivo principal da aplicação
│   ├── models/                 # Modelos de dados
│   │   ├── __init__.py
│   │   ├── user.py            # Modelo de usuário
│   │   └── conversation.py    # Modelos de conversa e mensagem
│   ├── routes/                # Rotas da API
│   │   ├── __init__.py
│   │   ├── user.py           # Rotas de usuário
│   │   ├── conversation.py   # Rotas de conversa
│   │   ├── ai.py            # Rotas de IA
│   │   └── learning.py      # Rotas de aprendizado
│   ├── services/            # Serviços de negócio
│   │   ├── __init__.py
│   │   ├── ai_service.py    # Serviço de IA
│   │   └── learning_service.py # Serviço de aprendizado
│   ├── database/            # Banco de dados
│   │   └── app.db          # Arquivo SQLite
│   └── static/             # Arquivos estáticos (frontend build)
├── venv/                   # Ambiente virtual Python
├── requirements.txt        # Dependências Python
├── app.py                 # Ponto de entrada para deploy
└── .env                   # Variáveis de ambiente
```

### Passo 1: Criação do Ambiente Virtual

O primeiro passo para configurar o backend é criar um ambiente virtual Python isolado. Isso garante que as dependências do projeto não interfiram com outros projetos Python em seu sistema.

Navegue até o diretório do backend e crie o ambiente virtual:

```bash
cd claudia-ai-backend
python -m venv venv
```

Em sistemas Linux/macOS, ative o ambiente virtual com:

```bash
source venv/bin/activate
```

Em sistemas Windows, use:

```bash
venv\Scripts\activate
```

Quando o ambiente virtual estiver ativo, você verá `(venv)` no início do prompt do terminal, indicando que está trabalhando dentro do ambiente isolado.

### Passo 2: Instalação das Dependências

Com o ambiente virtual ativo, instale as dependências necessárias para o backend. Crie um arquivo `requirements.txt` com as seguintes dependências:

```txt
Flask==3.1.1
flask-cors==6.0.0
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.41
Werkzeug==3.1.3
```

Instale as dependências usando pip:

```bash
pip install -r requirements.txt
```

Para projetos que requerem funcionalidades de machine learning mais avançadas, você pode adicionar dependências adicionais:

```txt
scikit-learn==1.3.2
numpy==1.26.2
pandas==2.1.4
```

### Passo 3: Configuração do Banco de Dados

A Claudia.AI utiliza SQLite como banco de dados padrão para desenvolvimento local. SQLite é uma excelente escolha para desenvolvimento pois não requer instalação ou configuração de servidor de banco de dados separado.

Crie o diretório para o banco de dados:

```bash
mkdir -p src/database
```

O banco de dados será criado automaticamente quando a aplicação for executada pela primeira vez. Os modelos de dados incluem tabelas para usuários, conversas, mensagens, feedback e configurações do sistema.

### Passo 4: Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do diretório backend para configurar variáveis de ambiente:

```bash
# Configurações da aplicação
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///src/database/app.db

# Configurações de CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# Configurações de logging
LOG_LEVEL=INFO

# Configurações da IA (para futuras integrações)
AI_MODEL_PATH=models/
AI_MODEL_NAME=llama-3.1-70b
```

### Passo 5: Estrutura dos Modelos de Dados

Os modelos de dados definem a estrutura do banco de dados e as relações entre diferentes entidades. O arquivo `src/models/user.py` define o modelo de usuário:

```python
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
    conversations = db.relationship('Conversation', backref='user', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'is_active': self.is_active,
            'preferences': json.loads(self.preferences) if self.preferences else {}
        }
```

### Passo 6: Configuração das Rotas da API

As rotas da API definem os endpoints disponíveis para o frontend. O arquivo `src/routes/ai.py` contém as rotas relacionadas à funcionalidade de IA:

```python
from flask import Blueprint, request, jsonify
from src.services.ai_service import ai_service
import logging

ai_bp = Blueprint('ai', __name__)
logger = logging.getLogger(__name__)

@ai_bp.route('/ai/generate', methods=['POST'])
def generate_response():
    """Gera resposta da IA para uma mensagem"""
    try:
        data = request.get_json()
        message = data.get('message')
        conversation_id = data.get('conversation_id')
        user_id = data.get('user_id', 1)
        
        if not message:
            return jsonify({'error': 'Mensagem é obrigatória'}), 400
        
        # Gera resposta usando o serviço de IA
        response = ai_service.generate_response(
            message=message,
            conversation_id=conversation_id,
            user_id=user_id
        )
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Erro ao gerar resposta: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500

@ai_bp.route('/ai/status', methods=['GET'])
def get_ai_status():
    """Retorna status do serviço de IA"""
    try:
        status = ai_service.get_model_info()
        return jsonify(status), 200
    except Exception as e:
        logger.error(f"Erro ao obter status da IA: {str(e)}")
        return jsonify({'error': 'Erro interno do servidor'}), 500
```

### Passo 7: Configuração do Arquivo Principal

O arquivo `src/main.py` é o ponto de entrada da aplicação Flask, onde todas as configurações são inicializadas:

```python
import os
from flask import Flask, jsonify
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.conversation import conversation_bp
from src.routes.ai import ai_bp
from src.routes.learning import learning_bp
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///src/database/app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configuração CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://localhost:5173"],
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
    app.register_blueprint(learning_bp, url_prefix='/api')
    
    # Criação das tabelas
    with app.app_context():
        db.create_all()
        logger.info("Banco de dados inicializado")
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Passo 8: Teste da Configuração do Backend

Para verificar se o backend está configurado corretamente, execute a aplicação:

```bash
# Certifique-se de que o ambiente virtual está ativo
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Execute a aplicação
python src/main.py
```

Se tudo estiver configurado corretamente, você verá mensagens indicando que o servidor Flask está rodando na porta 5000. Você pode testar os endpoints acessando `http://localhost:5000/api/health` em seu navegador.

---


## 🎨 Configuração do Frontend

### Estrutura do Frontend React

O frontend da Claudia.AI é desenvolvido com React 18, utilizando Vite como ferramenta de build para desenvolvimento rápido e eficiente. A aplicação implementa um design moderno e responsivo com Tailwind CSS, oferecendo uma experiência de usuário excepcional em dispositivos móveis e desktop.

A estrutura de diretórios do frontend segue as melhores práticas do React moderno:

```
claudia-ai-frontend/
├── public/
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── components/          # Componentes reutilizáveis
│   │   ├── ui/             # Componentes de interface básicos
│   │   │   ├── badge.jsx
│   │   │   ├── scroll-area.jsx
│   │   │   └── textarea.jsx
│   │   ├── Header.jsx      # Cabeçalho da aplicação
│   │   ├── Sidebar.jsx     # Barra lateral
│   │   └── Chat.jsx        # Componente principal de chat
│   ├── App.jsx             # Componente principal
│   ├── App.css             # Estilos globais
│   └── main.jsx            # Ponto de entrada
├── package.json            # Dependências e scripts
├── vite.config.js          # Configuração do Vite
├── tailwind.config.js      # Configuração do Tailwind
├── components.json         # Configuração de componentes
└── .env                    # Variáveis de ambiente
```

### Passo 1: Inicialização do Projeto React

Para criar o projeto frontend, você pode usar o template pré-configurado ou inicializar manualmente. Se estiver criando do zero, navegue até o diretório frontend e inicialize um novo projeto React com Vite:

```bash
cd claudia-ai-frontend
npm create vite@latest . -- --template react
```

Alternativamente, se você tiver acesso ao utilitário `manus-create-react-app`, pode usar:

```bash
manus-create-react-app claudia-ai-frontend
```

### Passo 2: Instalação das Dependências

O projeto utiliza várias bibliotecas modernas para criar uma interface rica e interativa. Instale todas as dependências necessárias:

```bash
# Usando pnpm (recomendado)
pnpm install

# Ou usando npm
npm install
```

As principais dependências incluem:

**Dependências de Interface**:
- `@radix-ui/react-*`: Componentes de interface acessíveis e customizáveis
- `tailwindcss`: Framework CSS utilitário para estilização rápida
- `lucide-react`: Biblioteca de ícones moderna e consistente
- `framer-motion`: Biblioteca para animações fluidas

**Dependências de Funcionalidade**:
- `react-router-dom`: Roteamento para aplicações React
- `react-hook-form`: Gerenciamento de formulários eficiente
- `date-fns`: Manipulação de datas
- `clsx`: Utilitário para classes CSS condicionais

### Passo 3: Configuração do Tailwind CSS

O Tailwind CSS é configurado para usar o tema personalizado da Claudia.AI com cores sustentáveis. O arquivo `tailwind.config.js` deve conter:

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Paleta de cores vegana da Claudia.AI
        primary: {
          50: '#f0f9f0',
          100: '#dcf2dc',
          200: '#bce5bc',
          300: '#8dd18d',
          400: '#7fb069',
          500: '#4a7c59',
          600: '#2d5a27',
          700: '#1e3f1c',
          800: '#163016',
          900: '#0f2010',
        },
        secondary: {
          50: '#f8f9fa',
          100: '#e9ecef',
          200: '#dee2e6',
          300: '#ced4da',
          400: '#adb5bd',
          500: '#6c757d',
          600: '#495057',
          700: '#343a40',
          800: '#212529',
          900: '#000000',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'pulse-slow': 'pulse 3s infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
```

### Passo 4: Configuração do Vite

O Vite é configurado para otimizar o desenvolvimento e build da aplicação. O arquivo `vite.config.js` deve incluir:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5173,
    host: true,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@radix-ui/react-dialog', '@radix-ui/react-scroll-area'],
        },
      },
    },
  },
})
```

### Passo 5: Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do diretório frontend para configurar variáveis de ambiente:

```bash
# Configurações da aplicação
VITE_APP_NAME=Claudia.AI
VITE_APP_VERSION=1.0.0
VITE_APP_DESCRIPTION=Inteligência Artificial Generativa que cresce com você

# URL da API (ajuste conforme necessário)
VITE_API_URL=http://localhost:5000/api

# Configurações de desenvolvimento
VITE_DEV_MODE=true
VITE_LOG_LEVEL=info
```

### Passo 6: Componente Principal da Aplicação

O arquivo `src/App.jsx` é o componente principal que orquestra toda a aplicação:

```jsx
import { useState, useEffect } from 'react'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import Chat from './components/Chat'
import './App.css'

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)
  const [activeConversation, setActiveConversation] = useState(null)
  const [conversations, setConversations] = useState([])
  const [aiStatus, setAiStatus] = useState('demo_mode')
  const [isLoading, setIsLoading] = useState(false)

  // URL da API baseada na variável de ambiente
  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

  // Carrega status da IA na inicialização
  useEffect(() => {
    const checkAiStatus = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/ai/status`)
        if (response.ok) {
          const data = await response.json()
          setAiStatus(data.status || 'demo_mode')
        }
      } catch (error) {
        console.warn('Não foi possível conectar com o backend:', error)
        setAiStatus('offline')
      }
    }

    checkAiStatus()
  }, [API_BASE_URL])

  const handleNewConversation = () => {
    const newConversation = {
      id: Date.now(),
      title: 'Nova Conversa',
      messages: [],
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    }
    
    setConversations(prev => [newConversation, ...prev])
    setActiveConversation(newConversation)
    setIsSidebarOpen(false)
  }

  const handleSendMessage = async (messageContent) => {
    if (!activeConversation) {
      handleNewConversation()
      return
    }

    setIsLoading(true)

    // Adiciona mensagem do usuário
    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: messageContent,
      timestamp: new Date().toISOString()
    }

    const updatedConversation = {
      ...activeConversation,
      messages: [...(activeConversation.messages || []), userMessage],
      updated_at: new Date().toISOString()
    }
    
    setActiveConversation(updatedConversation)

    try {
      // Envia mensagem para o backend
      const response = await fetch(`${API_BASE_URL}/ai/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          conversation_id: activeConversation.id,
          message: messageContent,
          user_id: 1
        })
      })

      if (response.ok) {
        const data = await response.json()
        
        const aiMessage = {
          id: Date.now() + 1,
          role: 'assistant',
          content: data.response || data.message,
          timestamp: new Date().toISOString(),
          tokens: data.tokens || 0
        }

        const finalConversation = {
          ...updatedConversation,
          messages: [...updatedConversation.messages, aiMessage],
          updated_at: new Date().toISOString()
        }

        setActiveConversation(finalConversation)
        
        // Atualiza lista de conversas
        setConversations(prev => 
          prev.map(conv => 
            conv.id === activeConversation.id ? finalConversation : conv
          )
        )
      } else {
        throw new Error('Erro na resposta do servidor')
      }
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error)
      
      // Resposta de fallback em caso de erro
      const fallbackMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: 'Desculpe, não foi possível processar sua mensagem no momento. Verifique se o backend está rodando.',
        timestamp: new Date().toISOString(),
        tokens: 0
      }

      const finalConversation = {
        ...updatedConversation,
        messages: [...updatedConversation.messages, fallbackMessage],
        updated_at: new Date().toISOString()
      }

      setActiveConversation(finalConversation)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar
        isOpen={isSidebarOpen}
        onClose={() => setIsSidebarOpen(false)}
        conversations={conversations}
        activeConversation={activeConversation}
        onSelectConversation={setActiveConversation}
        onNewConversation={handleNewConversation}
      />
      
      <div className="flex-1 flex flex-col">
        <Header
          onToggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)}
          aiStatus={aiStatus}
        />
        
        <Chat
          conversation={activeConversation}
          onSendMessage={handleSendMessage}
          isLoading={isLoading}
          onNewConversation={handleNewConversation}
        />
      </div>
    </div>
  )
}

export default App
```

### Passo 7: Configuração dos Scripts de Desenvolvimento

O arquivo `package.json` deve incluir scripts para desenvolvimento, build e preview:

```json
{
  "name": "claudia-ai-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview",
    "start": "vite --host"
  }
}
```

### Passo 8: Teste da Configuração do Frontend

Para verificar se o frontend está configurado corretamente:

```bash
# Instale as dependências (se ainda não fez)
pnpm install

# Execute o servidor de desenvolvimento
pnpm run dev
```

O servidor de desenvolvimento será iniciado na porta 5173. Acesse `http://localhost:5173` em seu navegador para ver a aplicação funcionando.

---


## 🚀 Execução da Aplicação

### Execução em Modo de Desenvolvimento

Para executar a Claudia.AI em modo de desenvolvimento, você precisará iniciar tanto o backend quanto o frontend simultaneamente. Este processo permite hot-reload automático, facilitando o desenvolvimento e teste de novas funcionalidades.

### Passo 1: Iniciando o Backend

Abra um terminal e navegue até o diretório do backend. Certifique-se de que o ambiente virtual Python está ativo e execute o servidor Flask:

```bash
# Navegue até o diretório do backend
cd claudia-ai-backend

# Ative o ambiente virtual
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Execute o servidor backend
python src/main.py
```

O servidor Flask será iniciado na porta 5000. Você verá mensagens de log indicando que o servidor está rodando e que o banco de dados foi inicializado. O backend ficará disponível em `http://localhost:5000`.

Para verificar se o backend está funcionando corretamente, você pode acessar os seguintes endpoints em seu navegador:

- `http://localhost:5000/api/health` - Verifica o status de saúde da aplicação
- `http://localhost:5000/api/info` - Mostra informações sobre a aplicação e endpoints disponíveis
- `http://localhost:5000/api/ai/status` - Verifica o status do serviço de IA

### Passo 2: Iniciando o Frontend

Em um novo terminal (mantendo o backend rodando), navegue até o diretório do frontend e execute o servidor de desenvolvimento:

```bash
# Navegue até o diretório do frontend
cd claudia-ai-frontend

# Execute o servidor de desenvolvimento
pnpm run dev
# ou
npm run dev
```

O servidor de desenvolvimento Vite será iniciado na porta 5173. Você verá uma mensagem indicando que a aplicação está disponível em `http://localhost:5173`. O Vite oferece hot-reload automático, então qualquer alteração nos arquivos será refletida imediatamente no navegador.

### Passo 3: Acessando a Aplicação

Com ambos os servidores rodando, abra seu navegador e acesse `http://localhost:5173`. Você verá a interface da Claudia.AI com:

- **Header**: Mostra o logo da Claudia.AI e o status da conexão com o backend
- **Sidebar**: Lista de conversas (inicialmente vazia)
- **Área Principal**: Tela de boas-vindas com sugestões de perguntas
- **Campo de Entrada**: Para digitar mensagens e interagir com a IA

### Execução com Docker (Opcional)

Para uma experiência de desenvolvimento mais consistente, você pode usar Docker para containerizar a aplicação. Crie um arquivo `docker-compose.yml` na raiz do projeto:

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./claudia-ai-backend
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=sqlite:///src/database/app.db
    volumes:
      - ./claudia-ai-backend:/app
      - /app/venv
    command: python src/main.py

  frontend:
    build:
      context: ./claudia-ai-frontend
      dockerfile: Dockerfile
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:5000/api
    volumes:
      - ./claudia-ai-frontend:/app
      - /app/node_modules
    command: pnpm run dev --host
    depends_on:
      - backend
```

Para usar Docker, execute:

```bash
# Construa e execute os containers
docker-compose up --build

# Para parar os containers
docker-compose down
```

### Monitoramento e Logs

Durante o desenvolvimento, é importante monitorar os logs de ambos os serviços para identificar problemas e entender o comportamento da aplicação.

**Logs do Backend**: O Flask exibe logs detalhados no terminal, incluindo:
- Requisições HTTP recebidas
- Erros de aplicação
- Inicialização do banco de dados
- Status dos serviços de IA

**Logs do Frontend**: O Vite mostra informações sobre:
- Hot-reload de arquivos
- Erros de compilação
- Warnings de linting
- Performance de build

### Configuração de Proxy para Desenvolvimento

O Vite está configurado para fazer proxy das requisições da API para o backend Flask. Isso elimina problemas de CORS durante o desenvolvimento. A configuração no `vite.config.js` redireciona todas as requisições para `/api/*` para `http://localhost:5000`.

Se você precisar alterar a porta do backend, atualize a configuração do proxy no arquivo `vite.config.js`:

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:NOVA_PORTA',
      changeOrigin: true,
      secure: false,
    },
  },
}
```

### Testando a Integração

Para verificar se a integração entre frontend e backend está funcionando:

1. **Teste de Conectividade**: Acesse a aplicação e verifique se o status da IA aparece como "Online" ou "Demo" no header
2. **Teste de Conversa**: Clique em "Começar Nova Conversa" e envie uma mensagem
3. **Teste de Resposta**: Verifique se a IA responde adequadamente
4. **Teste de Persistência**: Recarregue a página e verifique se as conversas são mantidas

### Comandos Úteis para Desenvolvimento

**Backend**:
```bash
# Reinstalar dependências
pip install -r requirements.txt

# Limpar banco de dados
rm src/database/app.db

# Executar em modo debug
FLASK_DEBUG=True python src/main.py

# Verificar sintaxe Python
python -m py_compile src/main.py
```

**Frontend**:
```bash
# Reinstalar dependências
pnpm install

# Limpar cache
pnpm store prune

# Build para produção
pnpm run build

# Preview do build
pnpm run preview

# Verificar linting
pnpm run lint
```

### Configuração de IDE

Para uma melhor experiência de desenvolvimento, configure seu IDE com as seguintes extensões:

**Visual Studio Code**:
- Python (Microsoft)
- Pylance (Microsoft)
- ES7+ React/Redux/React-Native snippets
- Tailwind CSS IntelliSense
- Auto Rename Tag
- Bracket Pair Colorizer

**PyCharm**:
- JavaScript and TypeScript
- React
- Tailwind CSS

### Variáveis de Ambiente para Desenvolvimento

Crie arquivos `.env.local` para configurações específicas de desenvolvimento:

**Backend** (`.env.local`):
```bash
FLASK_ENV=development
FLASK_DEBUG=True
LOG_LEVEL=DEBUG
DATABASE_URL=sqlite:///src/database/dev.db
```

**Frontend** (`.env.local`):
```bash
VITE_API_URL=http://localhost:5000/api
VITE_DEV_MODE=true
VITE_LOG_LEVEL=debug
```

---


## 🔧 Solução de Problemas

### Problemas Comuns do Backend

**Erro: "ModuleNotFoundError: No module named 'flask'"**

Este erro indica que as dependências do Python não foram instaladas corretamente ou o ambiente virtual não está ativo.

*Solução*:
```bash
# Verifique se o ambiente virtual está ativo
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Reinstale as dependências
pip install -r requirements.txt

# Verifique a instalação
pip list | grep -i flask
```

**Erro: "sqlite3.OperationalError: database is locked"**

Este erro ocorre quando múltiplas instâncias da aplicação tentam acessar o banco SQLite simultaneamente.

*Solução*:
```bash
# Pare todas as instâncias da aplicação
pkill -f "python src/main.py"

# Remova o arquivo de lock (se existir)
rm src/database/app.db-journal

# Reinicie a aplicação
python src/main.py
```

**Erro: "Port 5000 is already in use"**

A porta 5000 já está sendo usada por outro processo.

*Solução*:
```bash
# Encontre o processo usando a porta
lsof -i :5000  # Linux/macOS
netstat -ano | findstr :5000  # Windows

# Mate o processo (substitua PID pelo ID do processo)
kill -9 PID  # Linux/macOS
taskkill /PID PID /F  # Windows

# Ou use uma porta diferente
export FLASK_RUN_PORT=5001
python src/main.py
```

**Erro: "CORS policy: No 'Access-Control-Allow-Origin' header"**

Problema de configuração CORS entre frontend e backend.

*Solução*:
```python
# Verifique a configuração CORS em src/main.py
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://localhost:5173"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

**Erro: "ImportError: cannot import name 'db' from 'src.models.user'"**

Problema de importação circular ou estrutura de módulos.

*Solução*:
```bash
# Verifique se todos os arquivos __init__.py existem
touch src/__init__.py
touch src/models/__init__.py
touch src/routes/__init__.py
touch src/services/__init__.py

# Verifique a estrutura de importações
python -c "from src.models.user import db; print('Import OK')"
```

### Problemas Comuns do Frontend

**Erro: "command not found: pnpm"**

O pnpm não está instalado no sistema.

*Solução*:
```bash
# Instale pnpm globalmente
npm install -g pnpm

# Ou use npm como alternativa
npm install
npm run dev
```

**Erro: "Module not found: Can't resolve '@/components/Header'"**

Problema com alias de importação ou estrutura de diretórios.

*Solução*:
```bash
# Verifique se o arquivo existe
ls -la src/components/Header.jsx

# Verifique a configuração do alias no vite.config.js
resolve: {
  alias: {
    '@': path.resolve(__dirname, './src'),
  },
}

# Use importação relativa como alternativa
import Header from './components/Header'
```

**Erro: "Failed to fetch" ao tentar conectar com a API**

O backend não está rodando ou há problema de conectividade.

*Solução*:
```bash
# Verifique se o backend está rodando
curl http://localhost:5000/api/health

# Verifique a configuração da URL da API
echo $VITE_API_URL

# Verifique a configuração do proxy no vite.config.js
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:5000',
      changeOrigin: true,
    },
  },
}
```

**Erro: "Tailwind CSS classes not working"**

Problema de configuração ou build do Tailwind CSS.

*Solução*:
```bash
# Reinstale as dependências do Tailwind
pnpm add -D tailwindcss postcss autoprefixer

# Regenere a configuração
npx tailwindcss init -p

# Verifique se o CSS está sendo importado
# Em src/main.jsx ou App.jsx
import './index.css'
```

**Erro: "Hydration failed" ou problemas de renderização**

Problemas de estado ou componentes React.

*Solução*:
```bash
# Limpe o cache do navegador
# Ctrl+Shift+R (Chrome/Firefox)

# Limpe o cache do Vite
rm -rf node_modules/.vite
pnpm run dev

# Verifique erros no console do navegador
# F12 -> Console
```

### Problemas de Integração

**Frontend não consegue se comunicar com Backend**

*Diagnóstico*:
```bash
# Teste o backend diretamente
curl -X GET http://localhost:5000/api/health

# Teste do frontend
curl -X GET http://localhost:5173/api/health
```

*Solução*:
1. Verifique se ambos os serviços estão rodando
2. Confirme as configurações de proxy no Vite
3. Verifique as configurações de CORS no Flask
4. Teste com ferramentas como Postman ou curl

**Banco de dados não inicializa**

*Solução*:
```bash
# Crie o diretório manualmente
mkdir -p src/database

# Verifique permissões
chmod 755 src/database

# Inicialize o banco manualmente
python -c "
from src.main import create_app
from src.models.user import db
app = create_app()
with app.app_context():
    db.create_all()
    print('Database created successfully')
"
```

**Dependências conflitantes**

*Solução*:
```bash
# Backend - crie um novo ambiente virtual
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend - limpe e reinstale
rm -rf node_modules package-lock.json
pnpm install
```

### Problemas de Performance

**Backend lento para responder**

*Diagnóstico*:
```bash
# Monitore o uso de CPU e memória
top -p $(pgrep -f "python src/main.py")

# Verifique logs de performance
tail -f logs/app.log
```

*Solução*:
1. Otimize consultas ao banco de dados
2. Implemente cache para respostas frequentes
3. Use profiling para identificar gargalos
4. Considere usar um banco de dados mais robusto

**Frontend carregando lentamente**

*Solução*:
```bash
# Analise o bundle
pnpm run build
pnpm run preview

# Use ferramentas de análise
npx vite-bundle-analyzer

# Otimize importações
# Use lazy loading para componentes grandes
const LazyComponent = lazy(() => import('./HeavyComponent'))
```

### Problemas de Ambiente

**Diferenças entre sistemas operacionais**

*Windows*:
```bash
# Use PowerShell ou Git Bash
# Instale Python via Microsoft Store
# Use WSL2 para melhor compatibilidade
```

*macOS*:
```bash
# Use Homebrew para instalações
brew install python node

# Verifique permissões do Xcode
xcode-select --install
```

*Linux*:
```bash
# Use o gerenciador de pacotes da distribuição
sudo apt update && sudo apt install python3 python3-pip nodejs npm

# Verifique versões
python3 --version
node --version
```

### Logs e Debugging

**Habilitando logs detalhados**

Backend:
```python
# Em src/main.py
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)
```

Frontend:
```javascript
// Em src/App.jsx
const DEBUG = import.meta.env.VITE_DEBUG === 'true'

if (DEBUG) {
  console.log('Debug mode enabled')
}
```

**Ferramentas de debugging**

1. **Backend**: Use o debugger do Python ou pdb
2. **Frontend**: Use React Developer Tools
3. **Network**: Use as ferramentas de desenvolvedor do navegador
4. **Database**: Use um visualizador SQLite como DB Browser

### Comandos de Diagnóstico

```bash
# Verificar versões
python --version
node --version
pnpm --version

# Verificar processos rodando
ps aux | grep python
ps aux | grep node

# Verificar portas em uso
netstat -tulpn | grep :5000
netstat -tulpn | grep :5173

# Verificar espaço em disco
df -h

# Verificar memória
free -h
```

---


## 🤖 Scripts Automatizados

### Scripts de Instalação Automática

Para facilitar a instalação e configuração da Claudia.AI, foram criados scripts automatizados que executam todos os passos necessários com comandos simples. Estes scripts detectam automaticamente o sistema operacional e instalam as dependências apropriadas.

### Script de Instalação Completa (install.sh)

Crie um arquivo `install.sh` na raiz do projeto com o seguinte conteúdo:

```bash
#!/bin/bash

# Script de instalação automática da Claudia.AI
# Compatível com Linux, macOS e Windows (via Git Bash/WSL)

set -e  # Para execução em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Detectar sistema operacional
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        OS="windows"
    else
        print_error "Sistema operacional não suportado: $OSTYPE"
        exit 1
    fi
    print_status "Sistema detectado: $OS"
}

# Verificar se comando existe
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Verificar pré-requisitos
check_prerequisites() {
    print_status "Verificando pré-requisitos..."
    
    # Verificar Python
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        print_success "Python encontrado: $PYTHON_VERSION"
    elif command_exists python; then
        PYTHON_VERSION=$(python --version | cut -d' ' -f2)
        print_success "Python encontrado: $PYTHON_VERSION"
    else
        print_error "Python não encontrado. Instale Python 3.8+ antes de continuar."
        exit 1
    fi
    
    # Verificar Node.js
    if command_exists node; then
        NODE_VERSION=$(node --version)
        print_success "Node.js encontrado: $NODE_VERSION"
    else
        print_error "Node.js não encontrado. Instale Node.js 18+ antes de continuar."
        exit 1
    fi
    
    # Verificar Git
    if command_exists git; then
        GIT_VERSION=$(git --version)
        print_success "Git encontrado: $GIT_VERSION"
    else
        print_error "Git não encontrado. Instale Git antes de continuar."
        exit 1
    fi
}

# Instalar pnpm se não existir
install_pnpm() {
    if ! command_exists pnpm; then
        print_status "Instalando pnpm..."
        npm install -g pnpm
        print_success "pnpm instalado com sucesso"
    else
        print_success "pnpm já está instalado"
    fi
}

# Configurar backend
setup_backend() {
    print_status "Configurando backend..."
    
    cd claudia-ai-backend
    
    # Criar ambiente virtual
    if [[ "$OS" == "windows" ]]; then
        python -m venv venv
        source venv/Scripts/activate
    else
        python3 -m venv venv
        source venv/bin/activate
    fi
    
    # Instalar dependências
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Criar arquivo .env se não existir
    if [ ! -f .env ]; then
        cat > .env << EOF
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=dev-secret-key-$(date +%s)
DATABASE_URL=sqlite:///src/database/app.db
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
LOG_LEVEL=INFO
EOF
        print_success "Arquivo .env criado"
    fi
    
    # Criar diretório do banco de dados
    mkdir -p src/database
    
    # Inicializar banco de dados
    python -c "
from src.main import create_app
from src.models.user import db
app = create_app()
with app.app_context():
    db.create_all()
    print('Database initialized successfully')
"
    
    cd ..
    print_success "Backend configurado com sucesso"
}

# Configurar frontend
setup_frontend() {
    print_status "Configurando frontend..."
    
    cd claudia-ai-frontend
    
    # Instalar dependências
    pnpm install
    
    # Criar arquivo .env se não existir
    if [ ! -f .env ]; then
        cat > .env << EOF
VITE_APP_NAME=Claudia.AI
VITE_APP_VERSION=1.0.0
VITE_APP_DESCRIPTION=Inteligência Artificial Generativa que cresce com você
VITE_API_URL=http://localhost:5000/api
VITE_DEV_MODE=true
VITE_LOG_LEVEL=info
EOF
        print_success "Arquivo .env criado"
    fi
    
    cd ..
    print_success "Frontend configurado com sucesso"
}

# Criar scripts de execução
create_run_scripts() {
    print_status "Criando scripts de execução..."
    
    # Script para iniciar backend
    cat > start-backend.sh << 'EOF'
#!/bin/bash
cd claudia-ai-backend
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate
echo "Iniciando backend na porta 5000..."
python src/main.py
EOF
    
    # Script para iniciar frontend
    cat > start-frontend.sh << 'EOF'
#!/bin/bash
cd claudia-ai-frontend
echo "Iniciando frontend na porta 5173..."
pnpm run dev
EOF
    
    # Script para iniciar ambos (requer tmux ou screen)
    cat > start-all.sh << 'EOF'
#!/bin/bash
echo "Iniciando Claudia.AI..."

# Verificar se tmux está disponível
if command -v tmux >/dev/null 2>&1; then
    echo "Usando tmux para gerenciar sessões..."
    
    # Criar sessão tmux
    tmux new-session -d -s claudia-ai
    
    # Janela para backend
    tmux rename-window -t claudia-ai:0 'backend'
    tmux send-keys -t claudia-ai:backend 'cd claudia-ai-backend && source venv/bin/activate && python src/main.py' C-m
    
    # Nova janela para frontend
    tmux new-window -t claudia-ai -n 'frontend'
    tmux send-keys -t claudia-ai:frontend 'cd claudia-ai-frontend && pnpm run dev' C-m
    
    echo "Claudia.AI iniciada em sessão tmux 'claudia-ai'"
    echo "Para acessar: tmux attach-session -t claudia-ai"
    echo "Para sair: Ctrl+B, depois D"
    
else
    echo "tmux não encontrado. Iniciando em terminais separados..."
    echo "Execute os seguintes comandos em terminais separados:"
    echo "1. ./start-backend.sh"
    echo "2. ./start-frontend.sh"
fi
EOF
    
    # Tornar scripts executáveis
    chmod +x start-backend.sh start-frontend.sh start-all.sh
    
    print_success "Scripts de execução criados"
}

# Função principal
main() {
    echo "=========================================="
    echo "    Instalação Automática Claudia.AI     "
    echo "=========================================="
    echo
    
    detect_os
    check_prerequisites
    install_pnpm
    setup_backend
    setup_frontend
    create_run_scripts
    
    echo
    echo "=========================================="
    print_success "Instalação concluída com sucesso!"
    echo "=========================================="
    echo
    echo "Para iniciar a aplicação:"
    echo "1. Backend: ./start-backend.sh"
    echo "2. Frontend: ./start-frontend.sh"
    echo "3. Ambos: ./start-all.sh (requer tmux)"
    echo
    echo "Acesse: http://localhost:5173"
    echo
}

# Executar função principal
main "$@"
```

### Script de Desenvolvimento (dev.sh)

Crie um script `dev.sh` para facilitar tarefas de desenvolvimento:

```bash
#!/bin/bash

# Script de desenvolvimento da Claudia.AI
# Fornece comandos úteis para desenvolvimento

set -e

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_help() {
    echo "Claudia.AI - Script de Desenvolvimento"
    echo
    echo "Uso: ./dev.sh [comando]"
    echo
    echo "Comandos disponíveis:"
    echo "  install     - Instala todas as dependências"
    echo "  start       - Inicia backend e frontend"
    echo "  backend     - Inicia apenas o backend"
    echo "  frontend    - Inicia apenas o frontend"
    echo "  test        - Executa testes"
    echo "  build       - Faz build do frontend"
    echo "  clean       - Limpa caches e dependências"
    echo "  reset       - Reset completo (limpa banco de dados)"
    echo "  logs        - Mostra logs da aplicação"
    echo "  status      - Verifica status dos serviços"
    echo "  help        - Mostra esta ajuda"
}

install_deps() {
    echo -e "${BLUE}Instalando dependências...${NC}"
    
    # Backend
    cd claudia-ai-backend
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    source venv/bin/activate
    pip install -r requirements.txt
    cd ..
    
    # Frontend
    cd claudia-ai-frontend
    pnpm install
    cd ..
    
    echo -e "${GREEN}Dependências instaladas!${NC}"
}

start_backend() {
    echo -e "${BLUE}Iniciando backend...${NC}"
    cd claudia-ai-backend
    source venv/bin/activate
    python src/main.py &
    BACKEND_PID=$!
    echo $BACKEND_PID > ../backend.pid
    cd ..
    echo -e "${GREEN}Backend iniciado (PID: $BACKEND_PID)${NC}"
}

start_frontend() {
    echo -e "${BLUE}Iniciando frontend...${NC}"
    cd claudia-ai-frontend
    pnpm run dev &
    FRONTEND_PID=$!
    echo $FRONTEND_PID > ../frontend.pid
    cd ..
    echo -e "${GREEN}Frontend iniciado (PID: $FRONTEND_PID)${NC}"
}

start_all() {
    start_backend
    sleep 3
    start_frontend
    echo -e "${GREEN}Claudia.AI iniciada!${NC}"
    echo "Backend: http://localhost:5000"
    echo "Frontend: http://localhost:5173"
}

run_tests() {
    echo -e "${BLUE}Executando testes...${NC}"
    
    # Testes do backend
    cd claudia-ai-backend
    source venv/bin/activate
    python -m pytest tests/ -v 2>/dev/null || echo "Testes do backend não configurados"
    cd ..
    
    # Testes do frontend
    cd claudia-ai-frontend
    pnpm run test 2>/dev/null || echo "Testes do frontend não configurados"
    cd ..
}

build_frontend() {
    echo -e "${BLUE}Fazendo build do frontend...${NC}"
    cd claudia-ai-frontend
    pnpm run build
    cd ..
    echo -e "${GREEN}Build concluído!${NC}"
}

clean_all() {
    echo -e "${YELLOW}Limpando caches e dependências...${NC}"
    
    # Parar processos
    stop_services
    
    # Limpar backend
    cd claudia-ai-backend
    rm -rf __pycache__ src/__pycache__ src/*/__pycache__
    rm -rf .pytest_cache
    cd ..
    
    # Limpar frontend
    cd claudia-ai-frontend
    rm -rf node_modules/.vite
    rm -rf dist
    cd ..
    
    echo -e "${GREEN}Limpeza concluída!${NC}"
}

reset_all() {
    echo -e "${YELLOW}Reset completo...${NC}"
    
    stop_services
    
    # Remover banco de dados
    rm -f claudia-ai-backend/src/database/app.db
    
    # Limpar tudo
    clean_all
    
    # Reinstalar
    install_deps
    
    echo -e "${GREEN}Reset concluído!${NC}"
}

show_logs() {
    echo -e "${BLUE}Logs da aplicação:${NC}"
    
    if [ -f "claudia-ai-backend/app.log" ]; then
        echo "=== Backend Logs ==="
        tail -n 20 claudia-ai-backend/app.log
    fi
    
    echo "=== System Logs ==="
    if [ -f "backend.pid" ]; then
        PID=$(cat backend.pid)
        ps -p $PID -o pid,ppid,cmd || echo "Backend não está rodando"
    fi
    
    if [ -f "frontend.pid" ]; then
        PID=$(cat frontend.pid)
        ps -p $PID -o pid,ppid,cmd || echo "Frontend não está rodando"
    fi
}

check_status() {
    echo -e "${BLUE}Status dos serviços:${NC}"
    
    # Verificar backend
    if curl -s http://localhost:5000/api/health >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Backend: Online${NC}"
    else
        echo -e "${YELLOW}✗ Backend: Offline${NC}"
    fi
    
    # Verificar frontend
    if curl -s http://localhost:5173 >/dev/null 2>&1; then
        echo -e "${GREEN}✓ Frontend: Online${NC}"
    else
        echo -e "${YELLOW}✗ Frontend: Offline${NC}"
    fi
}

stop_services() {
    echo -e "${YELLOW}Parando serviços...${NC}"
    
    if [ -f "backend.pid" ]; then
        PID=$(cat backend.pid)
        kill $PID 2>/dev/null || true
        rm backend.pid
    fi
    
    if [ -f "frontend.pid" ]; then
        PID=$(cat frontend.pid)
        kill $PID 2>/dev/null || true
        rm frontend.pid
    fi
    
    # Matar processos por nome como backup
    pkill -f "python src/main.py" 2>/dev/null || true
    pkill -f "vite" 2>/dev/null || true
}

# Processar comando
case "$1" in
    install)
        install_deps
        ;;
    start)
        start_all
        ;;
    backend)
        start_backend
        ;;
    frontend)
        start_frontend
        ;;
    test)
        run_tests
        ;;
    build)
        build_frontend
        ;;
    clean)
        clean_all
        ;;
    reset)
        reset_all
        ;;
    logs)
        show_logs
        ;;
    status)
        check_status
        ;;
    stop)
        stop_services
        ;;
    help|*)
        print_help
        ;;
esac
```

### Script para Windows (install.bat)

Para usuários Windows, crie um arquivo `install.bat`:

```batch
@echo off
setlocal enabledelayedexpansion

echo ==========================================
echo     Instalacao Automatica Claudia.AI     
echo ==========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado. Instale Python 3.8+ antes de continuar.
    pause
    exit /b 1
)
echo [OK] Python encontrado

REM Verificar Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Node.js nao encontrado. Instale Node.js 18+ antes de continuar.
    pause
    exit /b 1
)
echo [OK] Node.js encontrado

REM Instalar pnpm
echo [INFO] Instalando pnpm...
npm install -g pnpm

REM Configurar backend
echo [INFO] Configurando backend...
cd claudia-ai-backend
python -m venv venv
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

REM Criar arquivo .env
if not exist .env (
    echo FLASK_ENV=development > .env
    echo FLASK_DEBUG=True >> .env
    echo SECRET_KEY=dev-secret-key >> .env
    echo DATABASE_URL=sqlite:///src/database/app.db >> .env
    echo CORS_ORIGINS=http://localhost:3000,http://localhost:5173 >> .env
    echo [OK] Arquivo .env criado
)

REM Criar diretorio do banco
if not exist src\database mkdir src\database

REM Inicializar banco de dados
python -c "from src.main import create_app; from src.models.user import db; app = create_app(); app.app_context().push(); db.create_all(); print('Database initialized')"

cd ..

REM Configurar frontend
echo [INFO] Configurando frontend...
cd claudia-ai-frontend
call pnpm install

REM Criar arquivo .env
if not exist .env (
    echo VITE_APP_NAME=Claudia.AI > .env
    echo VITE_APP_VERSION=1.0.0 >> .env
    echo VITE_API_URL=http://localhost:5000/api >> .env
    echo [OK] Arquivo .env criado
)

cd ..

REM Criar scripts de execucao
echo [INFO] Criando scripts de execucao...

echo @echo off > start-backend.bat
echo cd claudia-ai-backend >> start-backend.bat
echo call venv\Scripts\activate.bat >> start-backend.bat
echo python src\main.py >> start-backend.bat

echo @echo off > start-frontend.bat
echo cd claudia-ai-frontend >> start-frontend.bat
echo call pnpm run dev >> start-frontend.bat

echo.
echo ==========================================
echo [SUCESSO] Instalacao concluida!
echo ==========================================
echo.
echo Para iniciar a aplicacao:
echo 1. Backend: start-backend.bat
echo 2. Frontend: start-frontend.bat
echo.
echo Acesse: http://localhost:5173
echo.
pause
```

### Makefile para Desenvolvimento

Crie um `Makefile` para comandos rápidos:

```makefile
.PHONY: help install start backend frontend test build clean reset

# Variáveis
PYTHON = python3
NODE = node
PNPM = pnpm

help: ## Mostra esta ajuda
	@echo "Claudia.AI - Comandos de Desenvolvimento"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instala todas as dependências
	@echo "Instalando dependências..."
	cd claudia-ai-backend && $(PYTHON) -m venv venv && source venv/bin/activate && pip install -r requirements.txt
	cd claudia-ai-frontend && $(PNPM) install
	@echo "Dependências instaladas!"

start: ## Inicia backend e frontend
	@echo "Iniciando Claudia.AI..."
	make backend &
	sleep 3
	make frontend &
	@echo "Claudia.AI iniciada!"

backend: ## Inicia apenas o backend
	@echo "Iniciando backend..."
	cd claudia-ai-backend && source venv/bin/activate && $(PYTHON) src/main.py

frontend: ## Inicia apenas o frontend
	@echo "Iniciando frontend..."
	cd claudia-ai-frontend && $(PNPM) run dev

test: ## Executa testes
	@echo "Executando testes..."
	cd claudia-ai-backend && source venv/bin/activate && $(PYTHON) -m pytest tests/ -v || echo "Testes não configurados"
	cd claudia-ai-frontend && $(PNPM) run test || echo "Testes não configurados"

build: ## Faz build do frontend
	@echo "Fazendo build..."
	cd claudia-ai-frontend && $(PNPM) run build

clean: ## Limpa caches
	@echo "Limpando caches..."
	cd claudia-ai-backend && rm -rf __pycache__ src/__pycache__ src/*/__pycache__
	cd claudia-ai-frontend && rm -rf node_modules/.vite dist

reset: ## Reset completo
	@echo "Reset completo..."
	rm -f claudia-ai-backend/src/database/app.db
	make clean
	make install

status: ## Verifica status dos serviços
	@echo "Verificando status..."
	@curl -s http://localhost:5000/api/health >/dev/null && echo "✓ Backend: Online" || echo "✗ Backend: Offline"
	@curl -s http://localhost:5173 >/dev/null && echo "✓ Frontend: Online" || echo "✗ Frontend: Offline"
```

### Docker Compose para Desenvolvimento

Crie um `docker-compose.dev.yml` para desenvolvimento com Docker:

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./claudia-ai-backend
      dockerfile: Dockerfile.dev
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - FLASK_DEBUG=True
      - DATABASE_URL=sqlite:///src/database/app.db
    volumes:
      - ./claudia-ai-backend:/app
      - /app/venv
    command: python src/main.py
    restart: unless-stopped

  frontend:
    build:
      context: ./claudia-ai-frontend
      dockerfile: Dockerfile.dev
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:5000/api
    volumes:
      - ./claudia-ai-frontend:/app
      - /app/node_modules
    command: pnpm run dev --host
    depends_on:
      - backend
    restart: unless-stopped

  # Opcional: Banco de dados PostgreSQL para produção
  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=claudia_ai
      - POSTGRES_USER=claudia
      - POSTGRES_PASSWORD=claudia123
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    profiles:
      - production

volumes:
  postgres_data:
```

### Uso dos Scripts

Para usar os scripts automatizados:

```bash
# Tornar executáveis (Linux/macOS)
chmod +x install.sh dev.sh start-*.sh

# Instalação completa
./install.sh

# Comandos de desenvolvimento
./dev.sh install    # Instalar dependências
./dev.sh start      # Iniciar aplicação
./dev.sh status     # Verificar status
./dev.sh clean      # Limpar caches

# Usando Makefile
make install        # Instalar dependências
make start          # Iniciar aplicação
make test           # Executar testes
make build          # Build do frontend

# Usando Docker
docker-compose -f docker-compose.dev.yml up --build
```

---


## 🎨 Personalização e Expansão

### Personalização da Interface

A Claudia.AI foi projetada com flexibilidade em mente, permitindo extensas personalizações da interface e funcionalidades. O sistema de design baseado em Tailwind CSS facilita modificações visuais, enquanto a arquitetura modular permite adição de novos recursos.

### Customização de Cores e Tema

Para personalizar as cores da aplicação, edite o arquivo `tailwind.config.js` no frontend:

```javascript
// claudia-ai-frontend/tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        // Defina sua paleta personalizada
        primary: {
          50: '#f0f9ff',   // Azul muito claro
          100: '#e0f2fe',  // Azul claro
          500: '#0ea5e9',  // Azul médio
          600: '#0284c7',  // Azul escuro
          900: '#0c4a6e',  // Azul muito escuro
        },
        // Ou use cores completamente diferentes
        brand: {
          light: '#fef3c7',    // Amarelo claro
          DEFAULT: '#f59e0b',  // Amarelo
          dark: '#92400e',     // Amarelo escuro
        }
      }
    }
  }
}
```

Para aplicar as novas cores, atualize os componentes React:

```jsx
// Exemplo: src/components/Header.jsx
const Header = ({ onToggleSidebar, aiStatus }) => {
  return (
    <header className="bg-brand text-white shadow-lg">
      <div className="flex items-center justify-between px-4 py-3">
        <div className="flex items-center space-x-3">
          <button 
            onClick={onToggleSidebar}
            className="p-2 rounded-lg hover:bg-brand-dark transition-colors"
          >
            <Menu className="w-5 h-5" />
          </button>
          <h1 className="text-xl font-bold">Sua IA Personalizada</h1>
        </div>
      </div>
    </header>
  )
}
```

### Adicionando Novos Componentes

Para criar novos componentes de interface, siga a estrutura modular existente:

```jsx
// src/components/CustomWidget.jsx
import { useState } from 'react'
import { Badge } from './ui/badge'

const CustomWidget = ({ title, data, onAction }) => {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div className="bg-white rounded-lg shadow-md p-4 border border-gray-200">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-lg font-semibold text-gray-800">{title}</h3>
        <Badge variant="secondary">{data.length} items</Badge>
      </div>
      
      <div className={`transition-all duration-300 ${isExpanded ? 'max-h-96' : 'max-h-20'} overflow-hidden`}>
        {data.map((item, index) => (
          <div key={index} className="py-2 border-b border-gray-100 last:border-b-0">
            <p className="text-sm text-gray-600">{item.description}</p>
            <span className="text-xs text-gray-400">{item.timestamp}</span>
          </div>
        ))}
      </div>
      
      <button 
        onClick={() => setIsExpanded(!isExpanded)}
        className="mt-3 text-sm text-primary-600 hover:text-primary-800 transition-colors"
      >
        {isExpanded ? 'Mostrar menos' : 'Mostrar mais'}
      </button>
    </div>
  )
}

export default CustomWidget
```

### Integração com Modelos de IA Reais

Para integrar modelos de IA reais como Llama, GPT ou outros, modifique o serviço de IA no backend:

```python
# claudia-ai-backend/src/services/ai_service.py
import openai
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class AIService:
    def __init__(self):
        self.model_type = os.getenv('AI_MODEL_TYPE', 'demo')
        self.model = None
        self.tokenizer = None
        self.initialize_model()
    
    def initialize_model(self):
        """Inicializa o modelo de IA baseado na configuração"""
        if self.model_type == 'openai':
            self.initialize_openai()
        elif self.model_type == 'huggingface':
            self.initialize_huggingface()
        elif self.model_type == 'llama':
            self.initialize_llama()
        else:
            logger.info("Usando modo demonstração")
    
    def initialize_openai(self):
        """Configura integração com OpenAI"""
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.model_name = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        logger.info(f"OpenAI configurado com modelo: {self.model_name}")
    
    def initialize_huggingface(self):
        """Configura modelo do Hugging Face"""
        model_name = os.getenv('HF_MODEL_NAME', 'microsoft/DialoGPT-medium')
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
            
            # Configurar para GPU se disponível
            if torch.cuda.is_available():
                self.model = self.model.cuda()
                logger.info("Modelo carregado na GPU")
            
            logger.info(f"Modelo Hugging Face carregado: {model_name}")
        except Exception as e:
            logger.error(f"Erro ao carregar modelo: {e}")
            self.model_type = 'demo'
    
    def initialize_llama(self):
        """Configura modelo Llama local"""
        model_path = os.getenv('LLAMA_MODEL_PATH', './models/llama-2-7b-chat')
        
        try:
            # Implementar carregamento do Llama
            # Isso requer bibliotecas específicas como llama-cpp-python
            from llama_cpp import Llama
            
            self.model = Llama(
                model_path=model_path,
                n_ctx=2048,
                n_threads=8,
                verbose=False
            )
            logger.info("Modelo Llama carregado com sucesso")
        except ImportError:
            logger.error("llama-cpp-python não instalado")
            self.model_type = 'demo'
        except Exception as e:
            logger.error(f"Erro ao carregar Llama: {e}")
            self.model_type = 'demo'
    
    def generate_response(self, message, conversation_id=None, user_id=None):
        """Gera resposta usando o modelo configurado"""
        if self.model_type == 'openai':
            return self.generate_openai_response(message)
        elif self.model_type == 'huggingface':
            return self.generate_hf_response(message)
        elif self.model_type == 'llama':
            return self.generate_llama_response(message)
        else:
            return self.generate_demo_response(message)
    
    def generate_openai_response(self, message):
        """Gera resposta usando OpenAI"""
        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "Você é Claudia, uma assistente IA amigável e prestativa."},
                    {"role": "user", "content": message}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return {
                'response': response.choices[0].message.content,
                'tokens': response.usage.total_tokens,
                'model': self.model_name,
                'timestamp': datetime.utcnow().isoformat()
            }
        except Exception as e:
            logger.error(f"Erro OpenAI: {e}")
            return self.generate_demo_response(message)
    
    def generate_llama_response(self, message):
        """Gera resposta usando Llama"""
        try:
            prompt = f"<s>[INST] {message} [/INST]"
            
            response = self.model(
                prompt,
                max_tokens=500,
                temperature=0.7,
                top_p=0.9,
                echo=False
            )
            
            return {
                'response': response['choices'][0]['text'].strip(),
                'tokens': len(response['choices'][0]['text'].split()),
                'model': 'llama-local',
                'timestamp': datetime.utcnow().isoformat()
            }
        except Exception as e:
            logger.error(f"Erro Llama: {e}")
            return self.generate_demo_response(message)
```

### Adicionando Funcionalidades de Análise

Para adicionar análise avançada de conversas:

```python
# claudia-ai-backend/src/services/analytics_service.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from collections import Counter
import re

class AnalyticsService:
    def __init__(self):
        self.sentiment_analyzer = None
        self.initialize_analytics()
    
    def initialize_analytics(self):
        """Inicializa ferramentas de análise"""
        try:
            from textblob import TextBlob
            self.sentiment_analyzer = TextBlob
            logger.info("Análise de sentimento inicializada")
        except ImportError:
            logger.warning("TextBlob não instalado - análise de sentimento desabilitada")
    
    def analyze_conversation_trends(self, user_id, days=30):
        """Analisa tendências de conversação do usuário"""
        # Buscar conversas do usuário
        conversations = Conversation.query.filter(
            Conversation.user_id == user_id,
            Conversation.created_at >= datetime.utcnow() - timedelta(days=days)
        ).all()
        
        if not conversations:
            return {'error': 'Nenhuma conversa encontrada'}
        
        # Análise de frequência
        daily_counts = {}
        topics = []
        sentiments = []
        
        for conv in conversations:
            date = conv.created_at.date()
            daily_counts[date] = daily_counts.get(date, 0) + 1
            
            # Extrair tópicos das mensagens
            for message in conv.messages:
                if message.role == 'user':
                    topics.extend(self.extract_topics(message.content))
                    if self.sentiment_analyzer:
                        sentiment = self.sentiment_analyzer(message.content).sentiment.polarity
                        sentiments.append(sentiment)
        
        # Análise de tópicos mais frequentes
        topic_frequency = Counter(topics)
        
        # Análise de sentimento médio
        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        
        return {
            'daily_conversation_counts': daily_counts,
            'top_topics': topic_frequency.most_common(10),
            'average_sentiment': avg_sentiment,
            'total_conversations': len(conversations),
            'analysis_period': days
        }
    
    def extract_topics(self, text):
        """Extrai tópicos principais do texto"""
        # Implementação simples - pode ser melhorada com NLP avançado
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Filtrar palavras irrelevantes
        stop_words = {'o', 'a', 'de', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'suas', 'numa', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'pelas', 'só', 'nós', 'você', 'vocês', 'eles', 'elas'}
        
        topics = [word for word in words if len(word) > 3 and word not in stop_words]
        return topics[:5]  # Retorna até 5 tópicos por mensagem
    
    def generate_usage_report(self, user_id):
        """Gera relatório de uso detalhado"""
        user = User.query.get(user_id)
        if not user:
            return {'error': 'Usuário não encontrado'}
        
        # Estatísticas gerais
        total_conversations = Conversation.query.filter_by(user_id=user_id).count()
        total_messages = Message.query.join(Conversation).filter(Conversation.user_id == user_id).count()
        
        # Análise temporal
        trends = self.analyze_conversation_trends(user_id, days=90)
        
        # Feedback analysis
        feedbacks = Feedback.query.join(Message).join(Conversation).filter(Conversation.user_id == user_id).all()
        avg_rating = sum(f.rating for f in feedbacks) / len(feedbacks) if feedbacks else 0
        
        return {
            'user_info': {
                'username': user.username,
                'member_since': user.created_at.isoformat(),
                'total_conversations': total_conversations,
                'total_messages': total_messages,
                'average_rating': round(avg_rating, 2)
            },
            'trends': trends,
            'recommendations': self.generate_recommendations(user_id, trends)
        }
    
    def generate_recommendations(self, user_id, trends):
        """Gera recomendações personalizadas"""
        recommendations = []
        
        if trends.get('average_sentiment', 0) < -0.1:
            recommendations.append("Considere fazer perguntas mais positivas para melhorar a experiência")
        
        if len(trends.get('top_topics', [])) < 3:
            recommendations.append("Explore diferentes tópicos para aproveitar melhor a IA")
        
        daily_counts = trends.get('daily_conversation_counts', {})
        if len(daily_counts) > 7:
            avg_daily = sum(daily_counts.values()) / len(daily_counts)
            if avg_daily < 1:
                recommendations.append("Interaja mais frequentemente para melhor personalização")
        
        return recommendations
```

### Sistema de Plugins

Para permitir extensões modulares, implemente um sistema de plugins:

```python
# claudia-ai-backend/src/plugins/base_plugin.py
from abc import ABC, abstractmethod

class BasePlugin(ABC):
    """Classe base para plugins da Claudia.AI"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.name = self.__class__.__name__
        self.version = "1.0.0"
        self.enabled = True
    
    @abstractmethod
    def initialize(self):
        """Inicializa o plugin"""
        pass
    
    @abstractmethod
    def process_message(self, message, context):
        """Processa uma mensagem"""
        pass
    
    def get_info(self):
        """Retorna informações do plugin"""
        return {
            'name': self.name,
            'version': self.version,
            'enabled': self.enabled,
            'config': self.config
        }

# Exemplo de plugin para tradução
class TranslationPlugin(BasePlugin):
    def initialize(self):
        try:
            from googletrans import Translator
            self.translator = Translator()
            logger.info("Plugin de tradução inicializado")
        except ImportError:
            logger.error("googletrans não instalado")
            self.enabled = False
    
    def process_message(self, message, context):
        if not self.enabled:
            return message
        
        # Detectar idioma
        detection = self.translator.detect(message)
        
        if detection.lang != 'pt':
            # Traduzir para português
            translated = self.translator.translate(message, dest='pt')
            return {
                'original': message,
                'translated': translated.text,
                'detected_language': detection.lang,
                'confidence': detection.confidence
            }
        
        return message

# Sistema de gerenciamento de plugins
class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()
    
    def load_plugins(self):
        """Carrega todos os plugins disponíveis"""
        plugin_classes = [TranslationPlugin]  # Adicione mais plugins aqui
        
        for plugin_class in plugin_classes:
            try:
                plugin = plugin_class()
                plugin.initialize()
                self.plugins[plugin.name] = plugin
                logger.info(f"Plugin carregado: {plugin.name}")
            except Exception as e:
                logger.error(f"Erro ao carregar plugin {plugin_class.__name__}: {e}")
    
    def process_with_plugins(self, message, context):
        """Processa mensagem através de todos os plugins"""
        result = message
        
        for plugin in self.plugins.values():
            if plugin.enabled:
                try:
                    result = plugin.process_message(result, context)
                except Exception as e:
                    logger.error(f"Erro no plugin {plugin.name}: {e}")
        
        return result
```

### Configuração Avançada

Para configurações mais avançadas, crie um sistema de configuração flexível:

```python
# claudia-ai-backend/src/config/settings.py
import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class DatabaseConfig:
    url: str = "sqlite:///src/database/app.db"
    echo: bool = False
    pool_size: int = 5
    max_overflow: int = 10

@dataclass
class AIConfig:
    model_type: str = "demo"
    model_name: str = "gpt-3.5-turbo"
    max_tokens: int = 500
    temperature: float = 0.7
    api_key: str = ""

@dataclass
class SecurityConfig:
    secret_key: str = "dev-secret-key"
    jwt_expiration: int = 3600
    rate_limit: int = 100
    cors_origins: list = None

@dataclass
class AppConfig:
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 5000
    log_level: str = "INFO"
    
    database: DatabaseConfig = None
    ai: AIConfig = None
    security: SecurityConfig = None
    
    def __post_init__(self):
        if self.database is None:
            self.database = DatabaseConfig()
        if self.ai is None:
            self.ai = AIConfig()
        if self.security is None:
            self.security = SecurityConfig()
        
        # Carregar de variáveis de ambiente
        self.load_from_env()
    
    def load_from_env(self):
        """Carrega configurações de variáveis de ambiente"""
        self.debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
        self.host = os.getenv('HOST', self.host)
        self.port = int(os.getenv('PORT', self.port))
        self.log_level = os.getenv('LOG_LEVEL', self.log_level)
        
        # Database
        self.database.url = os.getenv('DATABASE_URL', self.database.url)
        
        # AI
        self.ai.model_type = os.getenv('AI_MODEL_TYPE', self.ai.model_type)
        self.ai.api_key = os.getenv('OPENAI_API_KEY', self.ai.api_key)
        
        # Security
        self.security.secret_key = os.getenv('SECRET_KEY', self.security.secret_key)
        cors_origins = os.getenv('CORS_ORIGINS', '')
        if cors_origins:
            self.security.cors_origins = cors_origins.split(',')

# Instância global de configuração
config = AppConfig()
```

---


## 📚 Referências

### Documentação Oficial

Este guia foi desenvolvido com base nas melhores práticas e documentações oficiais das tecnologias utilizadas na Claudia.AI. As referências a seguir fornecem informações detalhadas sobre cada componente do sistema.

**Flask Framework** [1]: O Flask é um microframework web para Python que oferece flexibilidade e simplicidade para desenvolvimento de APIs. A documentação oficial está disponível em https://flask.palletsprojects.com/, fornecendo guias completos sobre roteamento, templates, extensões e deployment.

**React Framework** [2]: React é uma biblioteca JavaScript para construção de interfaces de usuário, desenvolvida pelo Facebook. A documentação oficial em https://react.dev/ oferece tutoriais abrangentes, guias de conceitos e referências de API para desenvolvimento moderno com React 18.

**Vite Build Tool** [3]: Vite é uma ferramenta de build moderna que oferece desenvolvimento rápido e builds otimizados. A documentação em https://vitejs.dev/ explica configurações, plugins e otimizações para projetos React e outras frameworks.

**Tailwind CSS** [4]: Framework CSS utilitário que permite estilização rápida e consistente. A documentação em https://tailwindcss.com/ fornece guias completos sobre classes utilitárias, customização e integração com diferentes frameworks.

**SQLAlchemy ORM** [5]: Object-Relational Mapping para Python que facilita interações com bancos de dados. A documentação em https://docs.sqlalchemy.org/ oferece tutoriais sobre modelos, relacionamentos e consultas avançadas.

### Recursos de Inteligência Artificial

**Hugging Face Transformers** [6]: Biblioteca Python para modelos de linguagem pré-treinados. A documentação em https://huggingface.co/docs/transformers/ explica como carregar, usar e fine-tunar modelos como BERT, GPT e Llama.

**OpenAI API** [7]: Interface para modelos de linguagem da OpenAI, incluindo GPT-3.5 e GPT-4. A documentação em https://platform.openai.com/docs/ fornece guias sobre autenticação, endpoints e melhores práticas.

**Llama Models** [8]: Modelos de linguagem open-source desenvolvidos pela Meta. Informações sobre download, licenciamento e uso estão disponíveis em https://ai.meta.com/llama/.

### Ferramentas de Desenvolvimento

**Node.js Runtime** [9]: Ambiente de execução JavaScript server-side. A documentação em https://nodejs.org/docs/ oferece guias sobre instalação, APIs e melhores práticas para desenvolvimento.

**Python Programming** [10]: Linguagem de programação versátil usada no backend. A documentação oficial em https://docs.python.org/ fornece tutoriais completos e referências de biblioteca padrão.

**Git Version Control** [11]: Sistema de controle de versão distribuído. O livro Pro Git disponível em https://git-scm.com/book oferece conhecimento abrangente sobre workflows e comandos avançados.

### Recursos de Deploy e DevOps

**Docker Containerization** [12]: Plataforma de containerização para aplicações. A documentação em https://docs.docker.com/ explica conceitos de containers, Dockerfiles e orquestração.

**Nginx Web Server** [13]: Servidor web de alta performance para proxy reverso e serving de arquivos estáticos. A documentação em https://nginx.org/en/docs/ oferece guias de configuração e otimização.

**PM2 Process Manager** [14]: Gerenciador de processos para aplicações Node.js em produção. A documentação em https://pm2.keymetrics.io/docs/ explica monitoramento, clustering e deployment.

### Segurança e Melhores Práticas

**OWASP Security Guidelines** [15]: Projeto aberto para segurança de aplicações web. Os guias em https://owasp.org/ fornecem práticas essenciais para desenvolvimento seguro.

**Flask Security Best Practices** [16]: Guias específicos para segurança em aplicações Flask, incluindo autenticação, autorização e proteção contra vulnerabilidades comuns.

**React Security Considerations** [17]: Práticas de segurança para aplicações React, incluindo sanitização de dados, proteção XSS e gerenciamento de estado seguro.

---

## 🎯 Conclusão

### Resumo do Guia

Este guia completo forneceu instruções detalhadas para instalação, configuração e execução local da Claudia.AI, uma aplicação de inteligência artificial conversacional moderna e extensível. Através de explicações passo a passo, scripts automatizados e exemplos práticos, você agora possui todo o conhecimento necessário para executar e personalizar a aplicação em seu ambiente de desenvolvimento.

### Arquitetura Robusta e Escalável

A Claudia.AI foi projetada com uma arquitetura moderna que separa claramente as responsabilidades entre frontend e backend. O frontend React oferece uma interface de usuário responsiva e intuitiva, enquanto o backend Flask fornece APIs RESTful robustas e extensíveis. Esta separação permite desenvolvimento independente, facilita manutenção e possibilita escalabilidade horizontal quando necessário.

O uso de tecnologias modernas como Vite para build, Tailwind CSS para estilização e SQLAlchemy para persistência de dados garante que a aplicação esteja alinhada com as melhores práticas atuais de desenvolvimento web. A integração com modelos de inteligência artificial através de APIs padronizadas permite fácil substituição e upgrade de modelos conforme novas tecnologias se tornem disponíveis.

### Flexibilidade e Personalização

Um dos pontos fortes da Claudia.AI é sua flexibilidade para personalização e extensão. O sistema de plugins permite adicionar funcionalidades específicas sem modificar o código core, enquanto o sistema de configuração baseado em variáveis de ambiente facilita adaptação para diferentes ambientes de deployment.

A interface pode ser completamente personalizada através do sistema de design baseado em Tailwind CSS, permitindo adaptação para diferentes marcas, temas e necessidades visuais. O backend modular facilita adição de novos endpoints, serviços e integrações com sistemas externos.

### Preparação para Produção

Embora este guia foque no desenvolvimento local, a arquitetura da Claudia.AI está preparada para deployment em produção. Os scripts automatizados, configurações de Docker e exemplos de configuração de servidor web fornecem uma base sólida para transição do desenvolvimento para produção.

As práticas de segurança implementadas, incluindo configuração CORS adequada, validação de entrada e estrutura de logs, seguem padrões industriais para aplicações web modernas. O sistema de monitoramento e métricas permite acompanhamento de performance e identificação proativa de problemas.

### Evolução Contínua

A Claudia.AI foi projetada para evolução contínua. A arquitetura modular facilita adição de novas funcionalidades, enquanto o sistema de versionamento de API garante compatibilidade com integrações existentes. O sistema de feedback integrado permite coleta de dados para melhoria contínua da experiência do usuário.

A integração com modelos de IA modernos através de APIs padronizadas garante que a aplicação possa se beneficiar de avanços futuros em inteligência artificial sem necessidade de reestruturação significativa do código base.

### Próximos Passos Recomendados

Após completar a instalação e configuração básica, recomendamos os seguintes passos para maximizar o potencial da Claudia.AI:

**Integração com Modelos Reais**: Configure integração com modelos de IA reais como GPT-4, Llama ou modelos locais do Hugging Face para funcionalidade completa de conversação.

**Implementação de Autenticação**: Adicione sistema de autenticação robusto para suporte a múltiplos usuários e personalização individual.

**Otimização de Performance**: Implemente cache, otimização de consultas de banco de dados e compressão de assets para melhor performance.

**Monitoramento e Analytics**: Configure ferramentas de monitoramento como Prometheus, Grafana ou serviços de APM para acompanhamento de performance em produção.

**Testes Automatizados**: Desenvolva suíte completa de testes unitários, de integração e end-to-end para garantir qualidade e facilitar manutenção.

### Suporte e Comunidade

Para suporte adicional e contribuições para o projeto, considere:

- Documentar problemas encontrados e soluções desenvolvidas
- Contribuir com melhorias e novas funcionalidades
- Compartilhar personalizações e extensões úteis
- Participar de discussões sobre melhores práticas e evolução da plataforma

### Agradecimentos

Este guia foi desenvolvido com dedicação para fornecer uma experiência de instalação e desenvolvimento excepcional. A Claudia.AI representa o estado da arte em aplicações de IA conversacional, combinando tecnologias modernas com design centrado no usuário.

Esperamos que este guia tenha fornecido todas as informações necessárias para você começar sua jornada com a Claudia.AI. A aplicação está pronta para ser personalizada, estendida e adaptada para suas necessidades específicas, oferecendo uma base sólida para desenvolvimento de soluções de inteligência artificial inovadoras.

---

**Desenvolvido com excelência por Manus AI**  
*Data de criação: 28 de Julho de 2025*  
*Versão do guia: 1.0.0*

---

### Lista de Referências

[1] Flask Documentation. "Flask Web Development Framework." https://flask.palletsprojects.com/

[2] React Documentation. "React - A JavaScript Library for Building User Interfaces." https://react.dev/

[3] Vite Documentation. "Vite - Next Generation Frontend Tooling." https://vitejs.dev/

[4] Tailwind CSS Documentation. "Tailwind CSS - Utility-First CSS Framework." https://tailwindcss.com/

[5] SQLAlchemy Documentation. "SQLAlchemy - Python SQL Toolkit and ORM." https://docs.sqlalchemy.org/

[6] Hugging Face Transformers. "Transformers - State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX." https://huggingface.co/docs/transformers/

[7] OpenAI API Documentation. "OpenAI API Reference." https://platform.openai.com/docs/

[8] Meta AI Llama. "Llama - Large Language Model Meta AI." https://ai.meta.com/llama/

[9] Node.js Documentation. "Node.js JavaScript Runtime." https://nodejs.org/docs/

[10] Python Documentation. "Python Programming Language." https://docs.python.org/

[11] Git Documentation. "Git - Distributed Version Control System." https://git-scm.com/book

[12] Docker Documentation. "Docker - Container Platform." https://docs.docker.com/

[13] Nginx Documentation. "Nginx - HTTP and Reverse Proxy Server." https://nginx.org/en/docs/

[14] PM2 Documentation. "PM2 - Advanced Process Manager for Node.js." https://pm2.keymetrics.io/docs/

[15] OWASP Foundation. "Open Web Application Security Project." https://owasp.org/

[16] Flask Security. "Flask Security Best Practices." https://flask.palletsprojects.com/security/

[17] React Security. "React Security Considerations." https://react.dev/learn/security

