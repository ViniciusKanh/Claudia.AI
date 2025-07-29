# Claudia.AI - Inteligência Artificial Generativa

![Claudia.AI Logo](https://img.shields.io/badge/Claudia.AI-v1.0.0-green?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react)
![Flask](https://img.shields.io/badge/Flask-2.3+-000000?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3+-003B57?style=flat-square&logo=sqlite)

## 🌟 Visão Geral

Claudia.AI é uma inteligência artificial generativa completa e inovadora, desenvolvida com foco em aprendizado contínuo e sustentabilidade. Baseada no modelo Llama 3.1 70B do Hugging Face, ela oferece conversas inteligentes em português com um sistema avançado de personalização e melhoria contínua.

### ✨ Características Principais

- **🧠 IA Avançada**: Baseada no modelo Llama 3.1 70B para respostas precisas e contextuais
- **📚 Aprendizado Contínuo**: Sistema de machine learning que se adapta ao estilo do usuário
- **🌱 Design Sustentável**: Interface eco-friendly em verde e branco
- **💬 Conversas Inteligentes**: Suporte completo ao português com streaming de respostas
- **📊 Métricas Avançadas**: Sistema de feedback e análise de qualidade
- **🔧 API Completa**: Backend robusto com endpoints RESTful
- **📱 Interface Responsiva**: Frontend React moderno e intuitivo

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.11+
- Node.js 20+
- Git

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/claudia-ai.git
cd claudia-ai
```

2. **Configure o Backend**
```bash
cd claudia-ai-backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. **Configure o Frontend**
```bash
cd ../claudia-ai-frontend
npm install
# ou
pnpm install
```

4. **Inicie os Serviços**

Backend:
```bash
cd claudia-ai-backend
source venv/bin/activate
python src/main.py
```

Frontend:
```bash
cd claudia-ai-frontend
npm run dev
# ou
pnpm run dev
```

5. **Acesse a Aplicação**
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000/api
- Health Check: http://localhost:5000/api/health

## 🏗️ Arquitetura

### Stack Tecnológico

**Backend:**
- **Flask**: Framework web Python
- **SQLAlchemy**: ORM para banco de dados
- **SQLite**: Banco de dados local
- **Scikit-learn**: Machine learning
- **Flask-CORS**: Suporte a CORS

**Frontend:**
- **React 18**: Framework JavaScript
- **Vite**: Build tool moderna
- **Tailwind CSS**: Framework CSS
- **Lucide React**: Ícones

**IA e ML:**
- **Llama 3.1 70B**: Modelo de linguagem
- **TF-IDF**: Análise de texto
- **Análise de Sentimento**: Processamento de feedback

### Estrutura do Projeto

```
claudia-ai/
├── claudia-ai-backend/          # Backend Flask
│   ├── src/
│   │   ├── models/              # Modelos de dados
│   │   ├── routes/              # Endpoints da API
│   │   ├── services/            # Lógica de negócio
│   │   └── database/            # Configuração do BD
│   ├── venv/                    # Ambiente virtual
│   └── requirements.txt         # Dependências Python
├── claudia-ai-frontend/         # Frontend React
│   ├── src/
│   │   ├── components/          # Componentes React
│   │   └── assets/              # Recursos estáticos
│   ├── public/                  # Arquivos públicos
│   └── package.json             # Dependências Node.js
└── docs/                        # Documentação
```

## 🔧 API Reference

### Endpoints Principais

#### Saúde do Sistema
```http
GET /api/health
```

#### Informações da API
```http
GET /api/info
```

#### Geração de Resposta IA
```http
POST /api/ai/generate
Content-Type: application/json

{
  "conversation_id": 1,
  "message": "Sua mensagem aqui",
  "user_id": 1
}
```

#### Métricas de Aprendizado
```http
GET /api/learning/metrics
```

#### Análise de Padrões do Usuário
```http
GET /api/learning/user-patterns/{user_id}?days=30
```

### Códigos de Status

- `200` - Sucesso
- `201` - Criado com sucesso
- `400` - Erro na requisição
- `404` - Não encontrado
- `500` - Erro interno do servidor

## 🧠 Sistema de Aprendizado

### Funcionalidades de ML

1. **Análise de Feedback**
   - Processamento de avaliações dos usuários
   - Análise de sentimento em comentários
   - Métricas de satisfação

2. **Padrões de Conversação**
   - Identificação de tópicos preferidos
   - Análise de estilo de comunicação
   - Personalização de respostas

3. **Melhoria Contínua**
   - Ajuste automático de tom
   - Otimização de comprimento das respostas
   - Adaptação a preferências individuais

### Métricas Disponíveis

- Taxa de satisfação dos usuários
- Tempo médio de resposta
- Cobertura de feedback
- Distribuição de avaliações
- Padrões de uso por usuário

## 🎨 Design e UX

### Paleta de Cores Vegana

- **Verde Primário**: #2D5A27
- **Verde Secundário**: #4A7C59
- **Verde Claro**: #7FB069
- **Branco**: #FFFFFF
- **Cinza Claro**: #F8F9FA

### Princípios de Design

1. **Sustentabilidade**: Cores e elementos que remetem à natureza
2. **Acessibilidade**: Contraste adequado e navegação intuitiva
3. **Responsividade**: Funciona perfeitamente em desktop e mobile
4. **Minimalismo**: Interface limpa e focada na experiência

## 📊 Monitoramento e Métricas

### Dashboard de Métricas

A Claudia.AI inclui um sistema completo de monitoramento:

- **Métricas de Performance**: Tempo de resposta, throughput
- **Qualidade das Respostas**: Avaliações, feedback dos usuários
- **Uso do Sistema**: Usuários ativos, conversas por dia
- **Aprendizado**: Modelos treinados, padrões identificados

### Logs e Debugging

- Logs estruturados em JSON
- Níveis de log configuráveis
- Rastreamento de erros
- Métricas de performance

## 🔒 Segurança

### Medidas Implementadas

- **CORS**: Configurado para permitir apenas origens autorizadas
- **Validação de Entrada**: Sanitização de dados de entrada
- **Rate Limiting**: Proteção contra abuso da API
- **Logs de Auditoria**: Rastreamento de ações importantes

### Boas Práticas

- Senhas não são armazenadas em texto plano
- Validação de dados em todas as camadas
- Tratamento seguro de erros
- Configurações sensíveis em variáveis de ambiente

## 🚀 Deploy e Produção

### Opções de Deploy

1. **Local Development**
   - Ideal para desenvolvimento e testes
   - Banco SQLite local
   - Servidor de desenvolvimento

2. **Produção**
   - Servidor web robusto (Gunicorn/uWSGI)
   - Banco de dados PostgreSQL/MySQL
   - Proxy reverso (Nginx)
   - SSL/TLS configurado

### Variáveis de Ambiente

```bash
# Backend
FLASK_ENV=production
DATABASE_URL=sqlite:///app.db
SECRET_KEY=sua-chave-secreta

# Frontend
VITE_API_URL=http://localhost:5000/api
```

## 🧪 Testes

### Testes Automatizados

O projeto inclui um sistema completo de testes:

```bash
# Executar todos os testes
python test_claudia_ai.py
```

### Cobertura de Testes

- ✅ Health checks
- ✅ Endpoints da API
- ✅ Sistema de IA
- ✅ Funcionalidades de aprendizado
- ✅ Interface do usuário

## 📈 Roadmap

### Versão 1.1 (Próxima)
- [ ] Integração com modelos locais
- [ ] Sistema de plugins
- [ ] API de webhooks
- [ ] Dashboard administrativo

### Versão 1.2 (Futuro)
- [ ] Suporte a múltiplos idiomas
- [ ] Integração com APIs externas
- [ ] Sistema de templates
- [ ] Análise avançada de dados

## 🤝 Contribuição

### Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes

- Siga os padrões de código existentes
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Use mensagens de commit descritivas

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe

- **Desenvolvedor Principal**: Manus AI
- **Arquitetura**: Sistema modular e escalável
- **Design**: Interface sustentável e acessível
- **IA/ML**: Integração com Llama 3.1 70B

## 📞 Suporte

### Documentação Adicional

- [Guia de Instalação Detalhado](docs/installation.md)
- [Manual do Usuário](docs/user-guide.md)
- [Documentação da API](docs/api-reference.md)
- [Guia de Desenvolvimento](docs/development.md)

### Contato

- **Issues**: Use o sistema de issues do GitHub
- **Discussões**: Participe das discussões da comunidade
- **Email**: suporte@claudia-ai.com (exemplo)

## 🙏 Agradecimentos

- **Hugging Face**: Pelo modelo Llama 3.1 70B
- **Meta**: Pelo desenvolvimento do Llama
- **Comunidade Open Source**: Pelas ferramentas e bibliotecas
- **Usuários Beta**: Pelo feedback valioso

---

**Claudia.AI** - Inteligência que cresce com você 🌱

*Desenvolvido com ❤️ e sustentabilidade em mente*

