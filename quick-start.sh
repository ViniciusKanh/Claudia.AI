#!/bin/bash

# Script de início rápido da Claudia.AI
# Execute este script para iniciar rapidamente a aplicação

set -e

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_header() {
    echo -e "${BLUE}"
    echo "=========================================="
    echo "         Claudia.AI - Início Rápido      "
    echo "=========================================="
    echo -e "${NC}"
}

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se os diretórios existem
check_directories() {
    if [ ! -d "claudia-ai-backend" ]; then
        print_error "Diretório 'claudia-ai-backend' não encontrado!"
        print_status "Certifique-se de que você está no diretório correto do projeto."
        exit 1
    fi
    
    if [ ! -d "claudia-ai-frontend" ]; then
        print_error "Diretório 'claudia-ai-frontend' não encontrado!"
        print_status "Certifique-se de que você está no diretório correto do projeto."
        exit 1
    fi
    
    print_success "Estrutura do projeto verificada"
}

# Iniciar backend
start_backend() {
    print_status "Iniciando backend..."
    
    cd claudia-ai-backend
    
    # Verificar se ambiente virtual existe
    if [ ! -d "venv" ]; then
        print_status "Criando ambiente virtual Python..."
        python3 -m venv venv
    fi
    
	# Ativar ambiente virtual corretamente para diferentes sistemas
	if [ -f "venv/Scripts/activate" ]; then
		source venv/Scripts/activate  # Windows (Git Bash)
	elif [ -f "venv/bin/activate" ]; then
		source venv/bin/activate      # Linux/macOS
	else
		print_error "Ambiente virtual não encontrado!"
		exit 1
	fi

    
    # Instalar dependências se necessário
    if [ ! -f "venv/.deps_installed" ]; then
        print_status "Instalando dependências do backend..."
        pip install -r requirements.txt
        touch venv/.deps_installed
    fi
    
    # Iniciar servidor
    print_status "Servidor backend iniciando na porta 5000..."
    PYTHONPATH=src python src/main.py &
    BACKEND_PID=$!
    echo $BACKEND_PID > ../backend.pid
    
    cd ..
    print_success "Backend iniciado (PID: $BACKEND_PID)"
}

# Iniciar frontend
start_frontend() {
    print_status "Iniciando frontend..."
    
    cd claudia-ai-frontend
    
    # Verificar se dependências estão instaladas
    if [ ! -d "node_modules" ]; then
        print_status "Instalando dependências do frontend..."
        if command -v pnpm >/dev/null 2>&1; then
            pnpm install
        else
            npm install
        fi
    fi
    
    # Iniciar servidor de desenvolvimento
    print_status "Servidor frontend iniciando na porta 5173..."
    if command -v pnpm >/dev/null 2>&1; then
        pnpm run dev --host &
    else
        npm run dev -- --host &
    fi
    FRONTEND_PID=$!
    echo $FRONTEND_PID > ../frontend.pid
    
    cd ..
    print_success "Frontend iniciado (PID: $FRONTEND_PID)"
}

# Aguardar serviços iniciarem
wait_for_services() {
    print_status "Aguardando serviços iniciarem..."
    sleep 5
    
    # Verificar backend
    if curl -s http://localhost:5000/api/health >/dev/null 2>&1; then
        print_success "✓ Backend: Online (http://localhost:5000)"
    else
        print_error "✗ Backend: Falha ao iniciar"
    fi
    
    # Verificar frontend
    if curl -s http://localhost:5173 >/dev/null 2>&1; then
        print_success "✓ Frontend: Online (http://localhost:5173)"
    else
        print_error "✗ Frontend: Falha ao iniciar"
    fi
}

# Mostrar informações finais
show_info() {
    echo
    echo -e "${GREEN}=========================================="
    echo "         Claudia.AI está rodando!         "
    echo "==========================================${NC}"
    echo
    echo "🌐 Acesse a aplicação em:"
    echo "   http://localhost:5173"
    echo
    echo "🔧 API Backend disponível em:"
    echo "   http://localhost:5000/api"
    echo
    echo "📊 Status dos serviços:"
    echo "   http://localhost:5000/api/health"
    echo
    echo "⏹️  Para parar os serviços:"
    echo "   ./stop-claudia-ai.sh"
    echo
    echo "📝 Logs em tempo real:"
    echo "   tail -f claudia-ai-backend/app.log"
    echo
}

# Função principal
main() {
    print_header
    check_directories
    start_backend
    sleep 3
    start_frontend
    wait_for_services
    show_info
}

# Executar função principal
main "$@"

