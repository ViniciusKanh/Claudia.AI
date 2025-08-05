#!/bin/bash

# 🤖 Claudia.AI - Script de Instalação Automática
# Versão: 1.0.0
# Autor: Manus AI
# Data: Janeiro 2024

set -e  # Parar em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Símbolos
CHECK="✅"
ERROR="❌"
WARNING="⚠️"
INFO="ℹ️"
ROCKET="🚀"
GEAR="⚙️"

# Variáveis globais
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BACKEND_DIR="$PROJECT_ROOT/claudia-ai-backend"
FRONTEND_DIR="$PROJECT_ROOT/claudia-ai-frontend"
LOG_FILE="$PROJECT_ROOT/install.log"

# Função para logging
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Função para print colorido
print_color() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Função para print com símbolo
print_status() {
    local symbol=$1
    local message=$2
    local color=$3
    echo -e "${color}${symbol} ${message}${NC}"
}

# Função para verificar comando
check_command() {
    local cmd=$1
    local name=$2
    local install_msg=$3
    
    if command -v "$cmd" &> /dev/null; then
        local version=$($cmd --version 2>&1 | head -n1)
        print_status "$CHECK" "$name encontrado: $version" "$GREEN"
        log "✅ $name encontrado: $version"
        return 0
    else
        print_status "$ERROR" "$name não encontrado" "$RED"
        if [ -n "$install_msg" ]; then
            print_color "$YELLOW" "$install_msg"
        fi
        log "❌ $name não encontrado"
        return 1
    fi
}

# Função para detectar sistema operacional
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            echo "debian"
        elif [ -f /etc/redhat-release ]; then
            echo "redhat"
        else
            echo "linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        echo "windows"
    else
        echo "unknown"
    fi
}

# Função para instalar dependências do sistema
install_system_deps() {
    local os=$(detect_os)
    
    print_status "$GEAR" "Detectado sistema operacional: $os" "$BLUE"
    log "Sistema operacional detectado: $os"
    
    case $os in
        "debian")
            print_status "$INFO" "Atualizando repositórios..." "$CYAN"
            sudo apt update
            
            print_status "$INFO" "Instalando dependências do sistema..." "$CYAN"
            sudo apt install -y python3 python3-pip python3-venv nodejs npm git curl wget
            
            # Instalar Node.js mais recente se necessário
            if ! node --version | grep -q "v1[8-9]\|v[2-9][0-9]"; then
                print_status "$INFO" "Instalando Node.js 20..." "$CYAN"
                curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
                sudo apt install -y nodejs
            fi
            ;;
        "redhat")
            print_status "$INFO" "Instalando dependências do sistema..." "$CYAN"
            sudo yum install -y python3 python3-pip nodejs npm git curl wget
            ;;
        "macos")
            if ! command -v brew &> /dev/null; then
                print_status "$WARNING" "Homebrew não encontrado. Instale em: https://brew.sh/" "$YELLOW"
                return 1
            fi
            
            print_status "$INFO" "Instalando dependências via Homebrew..." "$CYAN"
            brew install python@3.11 node git
            ;;
        "windows")
            print_status "$WARNING" "Sistema Windows detectado. Use WSL ou instale manualmente:" "$YELLOW"
            echo "  - Python 3.11+: https://python.org/downloads/"
            echo "  - Node.js 18+: https://nodejs.org/"
            echo "  - Git: https://git-scm.com/"
            return 1
            ;;
        *)
            print_status "$WARNING" "Sistema operacional não suportado automaticamente" "$YELLOW"
            print_color "$YELLOW" "Instale manualmente: Python 3.11+, Node.js 18+, Git"
            return 1
            ;;
    esac
}

# Função para verificar pré-requisitos
check_prerequisites() {
    print_color "$BLUE" "\n🔍 Verificando pré-requisitos..."
    log "Iniciando verificação de pré-requisitos"
    
    local all_good=true
    
    # Verificar Python
    if ! check_command "python3" "Python 3" "Instale Python 3.11+: https://python.org/downloads/"; then
        all_good=false
    else
        # Verificar versão do Python
        local py_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        local py_major=$(echo $py_version | cut -d. -f1)
        local py_minor=$(echo $py_version | cut -d. -f2)
        
        if [ "$py_major" -lt 3 ] || ([ "$py_major" -eq 3 ] && [ "$py_minor" -lt 8 ]); then
            print_status "$ERROR" "Python $py_version é muito antigo. Necessário Python 3.8+" "$RED"
            all_good=false
        else
            print_status "$CHECK" "Versão do Python OK: $py_version" "$GREEN"
        fi
    fi
    
    # Verificar pip
    if ! check_command "pip3" "pip" "Instale pip: python3 -m ensurepip --upgrade"; then
        all_good=false
    fi
    
    # Verificar Node.js
    if ! check_command "node" "Node.js" "Instale Node.js 18+: https://nodejs.org/"; then
        all_good=false
    else
        # Verificar versão do Node.js
        local node_version=$(node --version | sed 's/v//')
        local node_major=$(echo $node_version | cut -d. -f1)
        
        if [ "$node_major" -lt 16 ]; then
            print_status "$ERROR" "Node.js $node_version é muito antigo. Necessário Node.js 16+" "$RED"
            all_good=false
        else
            print_status "$CHECK" "Versão do Node.js OK: $node_version" "$GREEN"
        fi
    fi
    
    # Verificar npm
    if ! check_command "npm" "npm" "npm vem com Node.js"; then
        all_good=false
    fi
    
    # Verificar Git
    if ! check_command "git" "Git" "Instale Git: https://git-scm.com/"; then
        all_good=false
    fi
    
    # Verificar pnpm (opcional)
    if ! check_command "pnpm" "pnpm (opcional)" ""; then
        print_status "$INFO" "Instalando pnpm..." "$CYAN"
        npm install -g pnpm 2>/dev/null || true
    fi
    
    if [ "$all_good" = true ]; then
        print_status "$CHECK" "Todos os pré-requisitos estão OK!" "$GREEN"
        log "✅ Todos os pré-requisitos verificados com sucesso"
        return 0
    else
        print_status "$ERROR" "Alguns pré-requisitos estão faltando" "$RED"
        log "❌ Pré-requisitos faltando"
        
        # Perguntar se quer tentar instalar automaticamente
        echo ""
        read -p "Deseja tentar instalar as dependências automaticamente? (s/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
            install_system_deps
            return $?
        else
            return 1
        fi
    fi
}

# Função para configurar backend
setup_backend() {
    print_color "$BLUE" "\n🔧 Configurando Backend..."
    log "Iniciando configuração do backend"
    
    if [ ! -d "$BACKEND_DIR" ]; then
        print_status "$ERROR" "Diretório do backend não encontrado: $BACKEND_DIR" "$RED"
        return 1
    fi
    
    cd "$BACKEND_DIR"
    
    # Criar ambiente virtual
    print_status "$INFO" "Criando ambiente virtual Python..." "$CYAN"
    python3 -m venv venv
    
    # Ativar ambiente virtual
    print_status "$INFO" "Ativando ambiente virtual..." "$CYAN"
    source venv/bin/activate
    
    # Atualizar pip
    print_status "$INFO" "Atualizando pip..." "$CYAN"
    python -m pip install --upgrade pip
    
    # Instalar dependências
    print_status "$INFO" "Instalando dependências Python..." "$CYAN"
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        print_status "$CHECK" "Dependências Python instaladas" "$GREEN"
        log "✅ Dependências Python instaladas"
    else
        print_status "$ERROR" "Arquivo requirements.txt não encontrado" "$RED"
        return 1
    fi
    
    # Criar diretório do banco de dados
    print_status "$INFO" "Criando diretório do banco de dados..." "$CYAN"
    mkdir -p src/database
    mkdir -p logs
    
    # Configurar arquivo .env se não existir
    if [ ! -f ".env" ]; then
        print_status "$INFO" "Criando arquivo .env..." "$CYAN"
        cat > .env << EOF
# Configurações da Claudia.AI
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

# Configurações do banco de dados
DATABASE_URL=sqlite:///src/database/app.db

# Configurações da IA (opcional - modo demo por padrão)
AI_MODEL_TYPE=demo
AI_MODEL_NAME=demo
# Para usar Llama localmente, descomente as linhas abaixo
# AI_MODEL_TYPE=llama
# AI_MODEL_NAME=Llama3.3-70B-Instruct
# LLAMA_MODEL_PATH=./src/models/Llama3.3-70B-Instruct
# OPENAI_API_KEY=sua-chave-openai-aqui
# HUGGINGFACE_API_KEY=sua-chave-huggingface-aqui

# Configurações do servidor
HOST=0.0.0.0
PORT=5000

# Configurações de log
LOG_LEVEL=INFO
EOF
        print_status "$CHECK" "Arquivo .env criado" "$GREEN"
    else
        print_status "$INFO" "Arquivo .env já existe" "$CYAN"
    fi
    
    # Inicializar banco de dados
    print_status "$INFO" "Inicializando banco de dados..." "$CYAN"
    python -c "
from src.main import create_app
from src.models.user import db
import os

try:
    app = create_app()
    with app.app_context():
        db.create_all()
        print('✅ Banco de dados inicializado com sucesso!')
except Exception as e:
    print(f'❌ Erro ao inicializar banco: {e}')
    exit(1)
" 2>/dev/null || {
        print_status "$ERROR" "Erro ao inicializar banco de dados" "$RED"
        return 1
    }
    
    print_status "$CHECK" "Backend configurado com sucesso!" "$GREEN"
    log "✅ Backend configurado com sucesso"
    
    cd "$PROJECT_ROOT"
}

# Função para configurar frontend
setup_frontend() {
    print_color "$BLUE" "\n🎨 Configurando Frontend..."
    log "Iniciando configuração do frontend"
    
    if [ ! -d "$FRONTEND_DIR" ]; then
        print_status "$ERROR" "Diretório do frontend não encontrado: $FRONTEND_DIR" "$RED"
        return 1
    fi
    
    cd "$FRONTEND_DIR"
    
    # Escolher gerenciador de pacotes
    local pkg_manager="npm"
    if command -v pnpm &> /dev/null; then
        pkg_manager="pnpm"
        print_status "$INFO" "Usando pnpm como gerenciador de pacotes" "$CYAN"
    else
        print_status "$INFO" "Usando npm como gerenciador de pacotes" "$CYAN"
    fi
    
    # Instalar dependências
    print_status "$INFO" "Instalando dependências Node.js..." "$CYAN"
    if [ -f "package.json" ]; then
        $pkg_manager install
        print_status "$CHECK" "Dependências Node.js instaladas" "$GREEN"
        log "✅ Dependências Node.js instaladas"
    else
        print_status "$ERROR" "Arquivo package.json não encontrado" "$RED"
        return 1
    fi
    
    # Configurar arquivo .env se não existir
    if [ ! -f ".env" ]; then
        print_status "$INFO" "Criando arquivo .env..." "$CYAN"
        cat > .env << EOF
# URL da API backend
VITE_API_URL=http://localhost:5000

# Configurações da aplicação
VITE_APP_NAME=Claudia.AI
VITE_APP_VERSION=1.0.0
VITE_APP_DESCRIPTION=Inteligência Artificial Generativa

# Configurações de desenvolvimento
VITE_DEV_MODE=true
EOF
        print_status "$CHECK" "Arquivo .env criado" "$GREEN"
    else
        print_status "$INFO" "Arquivo .env já existe" "$CYAN"
    fi
    
    print_status "$CHECK" "Frontend configurado com sucesso!" "$GREEN"
    log "✅ Frontend configurado com sucesso"
    
    cd "$PROJECT_ROOT"
}

# Função para testar instalação
test_installation() {
    print_color "$BLUE" "\n🧪 Testando instalação..."
    log "Iniciando testes de instalação"
    
    # Testar backend
    print_status "$INFO" "Testando backend..." "$CYAN"
    cd "$BACKEND_DIR"
    source venv/bin/activate
    
    # Teste básico de importação
    python -c "
try:
    from src.main import create_app
    from src.models.user import db
    print('✅ Importações do backend OK')
except Exception as e:
    print(f'❌ Erro nas importações: {e}')
    exit(1)
" || {
        print_status "$ERROR" "Teste do backend falhou" "$RED"
        return 1
    }
    
    print_status "$CHECK" "Backend testado com sucesso" "$GREEN"
    
    # Testar frontend
    print_status "$INFO" "Testando frontend..." "$CYAN"
    cd "$FRONTEND_DIR"
    
    # Verificar se build funciona
    local pkg_manager="npm"
    if command -v pnpm &> /dev/null && [ -f "pnpm-lock.yaml" ]; then
        pkg_manager="pnpm"
    fi
    
    # Teste de build (rápido)
    timeout 30s $pkg_manager run build > /dev/null 2>&1 || {
        print_status "$WARNING" "Build do frontend demorou muito ou falhou" "$YELLOW"
        print_color "$YELLOW" "Isso pode ser normal na primeira execução"
    }
    
    print_status "$CHECK" "Frontend testado com sucesso" "$GREEN"
    log "✅ Testes de instalação concluídos"
    
    cd "$PROJECT_ROOT"
}

# Função para criar scripts de conveniência
create_convenience_scripts() {
    print_color "$BLUE" "\n📝 Criando scripts de conveniência..."
    log "Criando scripts de conveniência"
    
    # Script de inicialização rápida
    if [ ! -f "$PROJECT_ROOT/start-claudia.sh" ]; then
        cat > "$PROJECT_ROOT/start-claudia.sh" << 'EOF'
#!/bin/bash
# Script de inicialização rápida da Claudia.AI

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$SCRIPT_DIR/claudia-ai-backend"
FRONTEND_DIR="$SCRIPT_DIR/claudia-ai-frontend"

echo "🚀 Iniciando Claudia.AI..."

# Iniciar backend
echo "🔧 Iniciando backend..."
cd "$BACKEND_DIR"
source venv/bin/activate
python src/main.py &
BACKEND_PID=$!

# Aguardar backend inicializar
sleep 5

# Iniciar frontend
echo "🎨 Iniciando frontend..."
cd "$FRONTEND_DIR"
if command -v pnpm &> /dev/null && [ -f "pnpm-lock.yaml" ]; then
    pnpm run dev &
else
    npm run dev &
fi
FRONTEND_PID=$!

echo ""
echo "✅ Claudia.AI iniciada com sucesso!"
echo "🌐 Frontend: http://localhost:5173"
echo "🔧 Backend: http://localhost:5000"
echo ""
echo "Para parar, pressione Ctrl+C"

# Aguardar sinal de interrupção
trap "echo '⏹️ Parando Claudia.AI...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT TERM
wait
EOF
        chmod +x "$PROJECT_ROOT/start-claudia.sh"
        print_status "$CHECK" "Script start-claudia.sh criado" "$GREEN"
    fi
    
    # Script de parada
    if [ ! -f "$PROJECT_ROOT/stop-claudia.sh" ]; then
        cat > "$PROJECT_ROOT/stop-claudia.sh" << 'EOF'
#!/bin/bash
# Script para parar a Claudia.AI

echo "⏹️ Parando Claudia.AI..."

# Parar processos Python (backend)
pkill -f "python src/main.py" 2>/dev/null || true
pkill -f "python.*claudia" 2>/dev/null || true

# Parar processos Node (frontend)
pkill -f "vite" 2>/dev/null || true
pkill -f "node.*claudia" 2>/dev/null || true

# Aguardar um pouco
sleep 2

echo "✅ Claudia.AI parada com sucesso!"
EOF
        chmod +x "$PROJECT_ROOT/stop-claudia.sh"
        print_status "$CHECK" "Script stop-claudia.sh criado" "$GREEN"
    fi
    
    log "✅ Scripts de conveniência criados"
}

# Função para exibir resumo final
show_summary() {
    print_color "$GREEN" "\n🎉 Instalação concluída com sucesso!"
    print_color "$CYAN" "\n📋 Resumo da instalação:"
    
    echo ""
    print_status "$CHECK" "Backend Python configurado" "$GREEN"
    print_status "$CHECK" "Frontend React configurado" "$GREEN"
    print_status "$CHECK" "Banco de dados inicializado" "$GREEN"
    print_status "$CHECK" "Scripts de conveniência criados" "$GREEN"
    
    print_color "$BLUE" "\n🚀 Como usar:"
    echo ""
    echo "  1. Iniciar a aplicação:"
    echo "     ./start-claudia.sh"
    echo ""
    echo "  2. Acessar no navegador:"
    echo "     Frontend: http://localhost:5173"
    echo "     Backend:  http://localhost:5000"
    echo ""
    echo "  3. Parar a aplicação:"
    echo "     ./stop-claudia.sh"
    echo "     ou pressione Ctrl+C"
    echo ""
    
    print_color "$YELLOW" "📚 Documentação:"
    echo "  - Guia completo: docs/GUIA_COMPLETO_INSTALACAO_CLAUDIA_AI.md"
    echo "  - Manual do usuário: docs/USER_GUIDE.md"
    echo "  - Estrutura do projeto: ESTRUTURA_PROJETO.md"
    echo ""
    
    print_color "$PURPLE" "⚙️ Configuração avançada:"
    echo "  - Backend: claudia-ai-backend/.env"
    echo "  - Frontend: claudia-ai-frontend/.env"
    echo "  - Logs: claudia-ai-backend/logs/"
    echo ""
    
    print_color "$CYAN" "🆘 Suporte:"
    echo "  - Documentação completa na pasta docs/"
    echo "  - Log de instalação: install.log"
    echo ""
    
    log "✅ Instalação concluída com sucesso"
}

# Função principal
main() {
    # Cabeçalho
    print_color "$PURPLE" "╔══════════════════════════════════════════════════════════════╗"
    print_color "$PURPLE" "║                    🤖 CLAUDIA.AI                            ║"
    print_color "$PURPLE" "║              Instalação Automática v1.0.0                   ║"
    print_color "$PURPLE" "║                                                              ║"
    print_color "$PURPLE" "║  Inteligência Artificial Generativa de Nova Geração         ║"
    print_color "$PURPLE" "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    
    # Inicializar log
    echo "🤖 Claudia.AI - Instalação iniciada em $(date)" > "$LOG_FILE"
    log "Iniciando instalação da Claudia.AI"
    
    # Verificar se estamos no diretório correto
    if [ ! -f "$PROJECT_ROOT/README.md" ] || [ ! -d "$BACKEND_DIR" ] || [ ! -d "$FRONTEND_DIR" ]; then
        print_status "$ERROR" "Execute este script a partir do diretório raiz do projeto Claudia.AI" "$RED"
        print_color "$YELLOW" "Estrutura esperada:"
        echo "  claudia-ai-complete-export/"
        echo "  ├── claudia-ai-backend/"
        echo "  ├── claudia-ai-frontend/"
        echo "  └── scripts/install-claudia-ai.sh"
        exit 1
    fi
    
    print_color "$CYAN" "Diretório do projeto: $PROJECT_ROOT"
    print_color "$CYAN" "Log de instalação: $LOG_FILE"
    echo ""
    
    # Executar etapas de instalação
    if check_prerequisites; then
        setup_backend && setup_frontend && test_installation && create_convenience_scripts
        
        if [ $? -eq 0 ]; then
            show_summary
            exit 0
        else
            print_status "$ERROR" "Erro durante a instalação" "$RED"
            print_color "$YELLOW" "Verifique o log: $LOG_FILE"
            exit 1
        fi
    else
        print_status "$ERROR" "Pré-requisitos não atendidos" "$RED"
        print_color "$YELLOW" "Instale as dependências necessárias e tente novamente"
        exit 1
    fi
}

# Verificar se está sendo executado diretamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

