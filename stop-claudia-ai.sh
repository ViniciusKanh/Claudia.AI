#!/bin/bash

# Script para parar a Claudia.AI
# Para todos os processos da aplicação de forma segura

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

echo -e "${BLUE}"
echo "=========================================="
echo "         Parando Claudia.AI              "
echo "=========================================="
echo -e "${NC}"

# Parar backend usando PID file
if [ -f "backend.pid" ]; then
    BACKEND_PID=$(cat backend.pid)
    if kill -0 $BACKEND_PID 2>/dev/null; then
        print_status "Parando backend (PID: $BACKEND_PID)..."
        kill $BACKEND_PID
        print_success "Backend parado"
    else
        print_warning "Backend já estava parado"
    fi
    rm -f backend.pid
else
    print_warning "Arquivo backend.pid não encontrado"
fi

# Parar frontend usando PID file
if [ -f "frontend.pid" ]; then
    FRONTEND_PID=$(cat frontend.pid)
    if kill -0 $FRONTEND_PID 2>/dev/null; then
        print_status "Parando frontend (PID: $FRONTEND_PID)..."
        kill $FRONTEND_PID
        print_success "Frontend parado"
    else
        print_warning "Frontend já estava parado"
    fi
    rm -f frontend.pid
else
    print_warning "Arquivo frontend.pid não encontrado"
fi

# Backup: matar processos por nome
print_status "Verificando processos restantes..."

# Matar processos Python do backend
PYTHON_PIDS=$(pgrep -f "python.*src/main.py" 2>/dev/null || true)
if [ ! -z "$PYTHON_PIDS" ]; then
    print_status "Parando processos Python restantes..."
    echo $PYTHON_PIDS | xargs kill 2>/dev/null || true
fi

# Matar processos Vite do frontend
VITE_PIDS=$(pgrep -f "vite.*dev" 2>/dev/null || true)
if [ ! -z "$VITE_PIDS" ]; then
    print_status "Parando processos Vite restantes..."
    echo $VITE_PIDS | xargs kill 2>/dev/null || true
fi

# Aguardar um momento
sleep 2

# Verificar se ainda há processos rodando
REMAINING_PYTHON=$(pgrep -f "python.*src/main.py" 2>/dev/null || true)
REMAINING_VITE=$(pgrep -f "vite.*dev" 2>/dev/null || true)

if [ -z "$REMAINING_PYTHON" ] && [ -z "$REMAINING_VITE" ]; then
    print_success "Todos os processos da Claudia.AI foram parados"
else
    print_warning "Alguns processos podem ainda estar rodando"
    if [ ! -z "$REMAINING_PYTHON" ]; then
        print_warning "Processos Python restantes: $REMAINING_PYTHON"
    fi
    if [ ! -z "$REMAINING_VITE" ]; then
        print_warning "Processos Vite restantes: $REMAINING_VITE"
    fi
fi

echo
print_success "Claudia.AI parada com sucesso!"
echo "Para iniciar novamente, execute: ./quick-start.sh"

