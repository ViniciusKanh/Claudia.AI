#!/bin/bash

# Script de instalação automática da Claudia.AI
# Compatível com Linux, macOS e Windows (via Git Bash/WSL)

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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
    
    if command_exists node; then
        NODE_VERSION=$(node --version)
        print_success "Node.js encontrado: $NODE_VERSION"
    else
        print_error "Node.js não encontrado. Instale Node.js 18+ antes de continuar."
        exit 1
    fi
    
    if command_exists git; then
        GIT_VERSION=$(git --version)
        print_success "Git encontrado: $GIT_VERSION"
    else
        print_error "Git não encontrado. Instale Git antes de continuar."
        exit 1
    fi
}

echo "=========================================="
echo "    Instalação Automática Claudia.AI     "
echo "=========================================="
echo

detect_os
check_prerequisites

print_success "Pré-requisitos verificados! Pronto para instalação."
print_status "Use este script junto com os arquivos do projeto Claudia.AI"

