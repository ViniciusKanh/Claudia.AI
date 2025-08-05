# 🤖 Claudia.AI - Inteligência Artificial Generativa

![Claudia.AI Logo](docs/claudia-logo.png)

## 🌟 Visão Geral

**Claudia.AI** é uma inteligência artificial generativa, desenvolvida com tecnologias de ponta para oferecer uma experiência conversacional avançada. O projeto combina um backend em Python/Flask com uma interface em React, proporcionando uma solução completa para IA conversacional.

### ✨ Características Principais

- 🧠 **IA Avançada**: Suporte a múltiplos modelos (OpenAI GPT, Hugging Face, Llama, modo demo)
- 🎨 **Interface Moderna**: Design responsivo com tema verde e branco (vegano)
- 📚 **Aprendizado Contínuo**: Sistema de machine learning integrado
- 🔒 **Segurança**: Autenticação e autorização robustas
- 📊 **Analytics**: Métricas e feedback em tempo real
- 🌐 **Multiplataforma**: Compatível com Linux, macOS e Windows
- 🚀 **Performance**: Otimizado para alta performance e escalabilidade

## 🏗️ Arquitetura

```
Claudia.AI
├── Frontend (React + Vite)
│   ├── Interface responsiva
│   ├── Sistema de chat
│   └── Componentes reutilizáveis
├── Backend (Flask + Python)
│   ├── APIs RESTful
│   ├── Sistema de IA
│   └── Banco de dados SQLite
└── Sistema de Aprendizado
    ├── Machine Learning
    ├── Análise de feedback
    └── Personalização
```

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- Git

### Instalação Automática

```bash
# 1. Extrair o projeto
unzip claudia-ai-complete.zip
cd claudia-ai-complete-export

# 2. Executar script de instalação
chmod +x scripts/install-claudia-ai.sh
./scripts/install-claudia-ai.sh

# 3. Iniciar a aplicação
chmod +x scripts/quick-start.sh
./scripts/quick-start.sh
```

### Acesso

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000
- **Documentação**: Pasta `docs/`

## 📁 Estrutura do Projeto

```
claudia-ai-complete-export/
├── claudia-ai-backend/          # Backend Flask
│   ├── src/
│   │   ├── models/             # Modelos de dados
│   │   ├── routes/             # APIs RESTful
│   │   ├── services/           # Serviços de IA
│   │   └── main.py            # Aplicação principal
│   ├── requirements.txt        # Dependências Python
│   ├── .env                   # Configurações
│   └── app.py                 # Ponto de entrada
├── claudia-ai-frontend/         # Frontend React
│   ├── src/
│   │   ├── components/        # Componentes React
│   │   └── App.jsx           # Aplicação principal
│   ├── package.json          # Dependências Node.js
│   └── .env                  # Configurações frontend
├── docs/                       # Documentação completa
│   ├── GUIA_COMPLETO_INSTALACAO_CLAUDIA_AI.md
│   ├── INSTALLATION_GUIDE.md
│   ├── USER_GUIDE.md
│   ├── arquitetura_claudia_ai.md
│   └── design_visual_claudia_ai.md
├── scripts/                    # Scripts de automação
│   ├── install-claudia-ai.sh
│   ├── quick-start.sh
│   └── stop-claudia-ai.sh
└── README.md                   # Este arquivo
```

## 📖 Documentação

### Guias Principais

- **[Guia Completo de Instalação](docs/GUIA_COMPLETO_INSTALACAO_CLAUDIA_AI.md)** - Instalação detalhada passo a passo
- **[Installation Guide](docs/INSTALLATION_GUIDE.md)** - Guia de instalação em inglês
- **[User Guide](docs/USER_GUIDE.md)** - Manual do usuário
- **[Arquitetura](docs/arquitetura_claudia_ai.md)** - Documentação técnica da arquitetura
- **[Design Visual](docs/design_visual_claudia_ai.md)** - Especificações de design

### Guias Rápidos

#### Instalação Manual

**Backend:**
```bash
cd claudia-ai-backend
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
python src/main.py
```

**Frontend:**
```bash
cd claudia-ai-frontend
npm install  # ou pnpm install
npm run dev  # ou pnpm run dev
```

#### Configuração de IA

**Modo Demo (Padrão):**
```bash
# No arquivo claudia-ai-backend/.env
AI_MODEL_TYPE=demo
AI_MODEL_NAME=demo
```

**OpenAI:**
```bash
AI_MODEL_TYPE=openai
OPENAI_API_KEY=sua-chave-aqui
```

**Hugging Face:**
```bash
AI_MODEL_TYPE=huggingface
HUGGINGFACE_API_KEY=sua-chave-aqui
```

**Llama Local:**
```bash
AI_MODEL_TYPE=llama
AI_MODEL_NAME=Llama3.3-70B-Instruct
LLAMA_MODEL_PATH=./src/models/Llama3.3-70B-Instruct
```

## 🛠️ Desenvolvimento

### Comandos Úteis

```bash
# Iniciar desenvolvimento
./scripts/quick-start.sh

# Parar aplicação
./scripts/stop-claudia-ai.sh

# Verificar status
curl http://localhost:5000/api/health

# Logs do backend
tail -f claudia-ai-backend/logs/app.log

# Build do frontend
cd claudia-ai-frontend && npm run build
```

### Estrutura de Desenvolvimento

**Backend (Flask):**
- `src/models/` - Modelos SQLAlchemy
- `src/routes/` - Endpoints da API
- `src/services/` - Lógica de negócio
- `src/main.py` - Aplicação principal

**Frontend (React):**
- `src/components/` - Componentes React
- `src/App.jsx` - Aplicação principal
- `src/index.css` - Estilos globais

## 🔧 Configuração

### Variáveis de Ambiente

**Backend (.env):**
```bash
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta
DATABASE_URL=sqlite:///src/database/app.db
AI_MODEL_TYPE=demo
AI_MODEL_NAME=demo
# LLAMA_MODEL_PATH=./src/models/Llama3.3-70B-Instruct
OPENAI_API_KEY=opcional
HUGGINGFACE_API_KEY=opcional
```

**Frontend (.env):**
```bash
VITE_API_URL=http://localhost:5000
VITE_APP_NAME=Claudia.AI
```

### Personalização

- **Cores**: Editar `claudia-ai-frontend/src/index.css`
- **Logo**: Substituir `claudia-ai-frontend/public/claudia-icon.svg`
- **Modelos de IA**: Configurar em `claudia-ai-backend/src/services/ai_service.py`

## 🧪 Testes

```bash
# Testes do backend
cd claudia-ai-backend
python -m pytest tests/

# Testes do frontend
cd claudia-ai-frontend
npm test

# Teste de integração
python test_claudia_ai.py
```

## 🚀 Deploy

### Desenvolvimento Local
```bash
./scripts/quick-start.sh
```

### Produção
```bash
# Build do frontend
cd claudia-ai-frontend
npm run build

# Deploy do backend
cd claudia-ai-backend
gunicorn app:app
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🆘 Suporte

### Problemas Comuns

- **Erro de porta em uso**: Verificar se as portas 5000 e 5173 estão livres
- **Módulo não encontrado**: Verificar se o ambiente virtual está ativo
- **CORS error**: Verificar configuração do backend

### Onde Buscar Ajuda

- 📖 **Documentação**: Pasta `docs/`
- 🐛 **Issues**: Reportar problemas no GitHub
- 💬 **Discussões**: Fórum da comunidade
- 📧 **Contato**: suporte@claudia-ai.com

## 🏆 Créditos

**Desenvolvido por**: Manus AI  
**Versão**: 1.0.0  
**Data**: Janeiro 2024

### Tecnologias Utilizadas

- **Backend**: Flask, SQLAlchemy, OpenAI, Transformers
- **Frontend**: React, Vite, Tailwind CSS, Lucide Icons
- **IA**: OpenAI GPT, Hugging Face Transformers, Scikit-learn
- **Banco**: SQLite, PostgreSQL (opcional)
- **Deploy**: Docker, Nginx, Gunicorn

## 🌟 Roadmap

- [ ] Suporte a mais modelos de IA
- [ ] Interface mobile nativa
- [ ] Sistema de plugins
- [ ] API pública
- [ ] Integração com Discord/Slack
- [ ] Análise de sentimento avançada
- [ ] Suporte multilíngue
- [ ] Dashboard administrativo

---

**Claudia.AI** - Inteligência Artificial Generativa de Nova Geração 🚀

*Transformando conversas em experiências inteligentes*

