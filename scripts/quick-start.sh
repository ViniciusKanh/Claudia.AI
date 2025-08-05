#!/bin/bash

# 🚀 Claudia.AI - Script de Inicialização Rápida
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
STOP="⏹️"

# Variáveis globais
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BACKEND_DIR="$PROJECT_ROOT/claudia-ai-backend"
FRONTEND_DIR="$PROJECT_ROOT/claudia-ai-frontend"
LOG_FILE="$PROJECT_ROOT/claudia-ai.log"

# PIDs dos processos
BACKEND_PID=""
FRONTEND_PID=""

# Função para ativar venv multiplataforma
activate_venv() {
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    elif [ -f "venv/Scripts/activate" ]; then
        # Windows (MINGW ou Git Bash)
        source venv/Scripts/activate
    else
        echo "❌ Ambiente virtual não encontrado."
        return 1
    fi
}


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

# Função para cleanup na saída
cleanup() {
    print_color "$YELLOW" "\n$STOP Parando Claudia.AI..."
    log "Parando aplicação - cleanup iniciado"
    
    if [ -n "$BACKEND_PID" ] && kill -0 "$BACKEND_PID" 2>/dev/null; then
        print_status "$INFO" "Parando backend (PID: $BACKEND_PID)..." "$CYAN"
        kill "$BACKEND_PID" 2>/dev/null || true
        wait "$BACKEND_PID" 2>/dev/null || true
    fi
    
    if [ -n "$FRONTEND_PID" ] && kill -0 "$FRONTEND_PID" 2>/dev/null; then
        print_status "$INFO" "Parando frontend (PID: $FRONTEND_PID)..." "$CYAN"
        kill "$FRONTEND_PID" 2>/dev/null || true
        wait "$FRONTEND_PID" 2>/dev/null || true
    fi
    
    # Cleanup adicional
    pkill -f "python -m src.main" 2>/dev/null || true
    pkill -f "vite" 2>/dev/null || true
    
    print_status "$CHECK" "Claudia.AI parada com sucesso!" "$GREEN"
    log "Aplicação parada com sucesso"
    exit 0
}

# Configurar trap para cleanup
trap cleanup INT TERM EXIT

# Função para verificar se porta está em uso
check_port() {
    local port=$1
    local name=$2
    
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        print_status "$WARNING" "Porta $port ($name) já está em uso" "$YELLOW"
        
        # Tentar identificar o processo
        local process=$(lsof -Pi :$port -sTCP:LISTEN -t 2>/dev/null | head -1)
        if [ -n "$process" ]; then
            local process_name=$(ps -p $process -o comm= 2>/dev/null || echo "desconhecido")
            print_color "$YELLOW" "  Processo: $process_name (PID: $process)"
            
            read -p "Deseja parar o processo e continuar? (s/N): " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Ss]$ ]]; then
                kill $process 2>/dev/null || true
                sleep 2
                return 0
            else
                return 1
            fi
        fi
        return 1
    fi
    return 0
}

# Função para verificar pré-requisitos básicos
check_basic_requirements() {
    print_status "$INFO" "Verificando pré-requisitos básicos..." "$CYAN"
    log "Verificando pré-requisitos básicos"
    
    local all_good=true
    
    # Verificar estrutura do projeto
    if [ ! -d "$BACKEND_DIR" ]; then
        print_status "$ERROR" "Diretório do backend não encontrado: $BACKEND_DIR" "$RED"
        all_good=false
    fi
    
    if [ ! -d "$FRONTEND_DIR" ]; then
        print_status "$ERROR" "Diretório do frontend não encontrado: $FRONTEND_DIR" "$RED"
        all_good=false
    fi
    
    # Verificar se backend foi configurado
    if [ ! -d "$BACKEND_DIR/venv" ]; then
        print_status "$ERROR" "Ambiente virtual do backend não encontrado" "$RED"
        print_color "$YELLOW" "Execute primeiro: ./scripts/install-claudia-ai.sh"
        all_good=false
    fi
    
    # Verificar se frontend foi configurado
    if [ ! -d "$FRONTEND_DIR/node_modules" ]; then
        print_status "$ERROR" "Dependências do frontend não encontradas" "$RED"
        print_color "$YELLOW" "Execute primeiro: ./scripts/install-claudia-ai.sh"
        all_good=false
    fi
    
    # Verificar portas
    if ! check_port 5000 "Backend"; then
        all_good=false
    fi
    
    if ! check_port 5173 "Frontend"; then
        all_good=false
    fi
    
    if [ "$all_good" = true ]; then
        print_status "$CHECK" "Pré-requisitos básicos OK" "$GREEN"
        log "✅ Pré-requisitos básicos verificados"
        return 0
    else
        print_status "$ERROR" "Alguns pré-requisitos não foram atendidos" "$RED"
        log "❌ Pré-requisitos básicos falharam"
        return 1
    fi
}

# Função para inicializar banco de dados se necessário
init_database() {
    if [ ! -f "$BACKEND_DIR/src/database/app.db" ]; then
        print_status "$INFO" "Inicializando banco de dados..." "$CYAN"
        log "Inicializando banco de dados"
        
        cd "$BACKEND_DIR"
        activate_venv

        python -c "
from src.main import create_app
from src.models.user import db
import os

try:
    # Criar diretório se não existir
    os.makedirs('src/database', exist_ok=True)
    
    app = create_app()
    with app.app_context():
        db.create_all()
        print('✅ Banco de dados inicializado!')
except Exception as e:
    print(f'❌ Erro ao inicializar banco: {e}')
    exit(1)
" || {
            print_status "$ERROR" "Erro ao inicializar banco de dados" "$RED"
            return 1
        }
        
        print_status "$CHECK" "Banco de dados inicializado" "$GREEN"
        log "✅ Banco de dados inicializado"
        cd "$PROJECT_ROOT"
    else
        print_status "$INFO" "Banco de dados já existe" "$CYAN"
    fi
}

# Função para iniciar backend
start_backend() {
    print_status "$GEAR" "Iniciando backend..." "$BLUE"
    log "Iniciando backend"
    
    cd "$BACKEND_DIR"
    
    # Verificar se ambiente virtual existe
    if [ ! -d "venv" ]; then
        print_status "$ERROR" "Ambiente virtual não encontrado. Execute install-claudia-ai.sh primeiro" "$RED"
        return 1
    fi
    
    # Ativar ambiente virtual
    activate_venv
    
    # Verificar se dependências estão instaladas
    if ! python -c "import flask" 2>/dev/null; then
        print_status "$ERROR" "Dependências não instaladas. Execute install-claudia-ai.sh primeiro" "$RED"
        return 1
    fi
    
    # Criar diretórios necessários
    mkdir -p src/database logs
    
    # Iniciar aplicação em background
    print_status "$INFO" "Executando: python -m src.main" "$CYAN"
    python -m src.main > ../backend.log 2>&1 &
    BACKEND_PID=$!
    
    # Aguardar inicialização
    print_status "$INFO" "Aguardando backend inicializar..." "$CYAN"
    local max_wait=30
    local count=0
    
    while [ $count -lt $max_wait ]; do
        if curl -s http://localhost:5000/api/health >/dev/null 2>&1; then
            print_status "$CHECK" "Backend iniciado com sucesso! (PID: $BACKEND_PID)" "$GREEN"
            log "✅ Backend iniciado com sucesso (PID: $BACKEND_PID)"
            cd "$PROJECT_ROOT"
            return 0
        fi
        
        # Verificar se processo ainda está rodando
        if ! kill -0 "$BACKEND_PID" 2>/dev/null; then
            print_status "$ERROR" "Backend falhou ao iniciar" "$RED"
            print_color "$YELLOW" "Verifique o log: backend.log"
            log "❌ Backend falhou ao iniciar"
            return 1
        fi
        
        sleep 1
        count=$((count + 1))
        
        # Mostrar progresso
        if [ $((count % 5)) -eq 0 ]; then
            print_status "$INFO" "Ainda aguardando... ($count/${max_wait}s)" "$CYAN"
        fi
    done
    
    print_status "$ERROR" "Timeout aguardando backend inicializar" "$RED"
    log "❌ Timeout aguardando backend"
    return 1
}

# Função para iniciar frontend
start_frontend() {
    print_status "$GEAR" "Iniciando frontend..." "$BLUE"
    log "Iniciando frontend"
    
    cd "$FRONTEND_DIR"
    
    # Verificar se node_modules existe
    if [ ! -d "node_modules" ]; then
        print_status "$ERROR" "Dependências não instaladas. Execute install-claudia-ai.sh primeiro" "$RED"
        return 1
    fi
    
    # Escolher gerenciador de pacotes
    local pkg_manager="npm"
    if command -v pnpm &> /dev/null && [ -f "pnpm-lock.yaml" ]; then
        pkg_manager="pnpm"
        print_status "$INFO" "Usando pnpm" "$CYAN"
    else
        print_status "$INFO" "Usando npm" "$CYAN"
    fi
    
    # Iniciar aplicação em background
    print_status "$INFO" "Executando: $pkg_manager run dev" "$CYAN"
    $pkg_manager run dev > ../frontend.log 2>&1 &
    FRONTEND_PID=$!
    
    # Aguardar inicialização
    print_status "$INFO" "Aguardando frontend inicializar..." "$CYAN"
    local max_wait=60  # Frontend pode demorar mais
    local count=0
    
    while [ $count -lt $max_wait ]; do
        if curl -s http://localhost:5173 >/dev/null 2>&1; then
            print_status "$CHECK" "Frontend iniciado com sucesso! (PID: $FRONTEND_PID)" "$GREEN"
            log "✅ Frontend iniciado com sucesso (PID: $FRONTEND_PID)"
            cd "$PROJECT_ROOT"
            return 0
        fi
        
        # Verificar se processo ainda está rodando
        if ! kill -0 "$FRONTEND_PID" 2>/dev/null; then
            print_status "$ERROR" "Frontend falhou ao iniciar" "$RED"
            print_color "$YELLOW" "Verifique o log: frontend.log"
            log "❌ Frontend falhou ao iniciar"
            return 1
        fi
        
        sleep 1
        count=$((count + 1))
        
        # Mostrar progresso
        if [ $((count % 10)) -eq 0 ]; then
            print_status "$INFO" "Ainda aguardando... ($count/${max_wait}s)" "$CYAN"
        fi
    done
    
    print_status "$ERROR" "Timeout aguardando frontend inicializar" "$RED"
    log "❌ Timeout aguardando frontend"
    return 1
}

# Função para verificar status dos serviços
check_services_status() {
    print_color "$BLUE" "\n🔍 Verificando status dos serviços..."
    log "Verificando status dos serviços"
    
    # Verificar backend
    if curl -s http://localhost:5000/api/health >/dev/null 2>&1; then
        local health_response=$(curl -s http://localhost:5000/api/health)
        print_status "$CHECK" "Backend: Online" "$GREEN"
        print_color "$CYAN" "  Health: $health_response"
        
        # Verificar status da IA
        local ai_status=$(curl -s http://localhost:5000/api/ai/status 2>/dev/null || echo "N/A")
        print_color "$CYAN" "  IA Status: $ai_status"
    else
        print_status "$ERROR" "Backend: Offline" "$RED"
    fi
    
    # Verificar frontend
    if curl -s http://localhost:5173 >/dev/null 2>&1; then
        print_status "$CHECK" "Frontend: Online" "$GREEN"
    else
        print_status "$ERROR" "Frontend: Offline" "$RED"
    fi
    
    # Verificar processos
    if [ -n "$BACKEND_PID" ] && kill -0 "$BACKEND_PID" 2>/dev/null; then
        print_status "$CHECK" "Processo Backend: Rodando (PID: $BACKEND_PID)" "$GREEN"
    else
        print_status "$WARNING" "Processo Backend: Não encontrado" "$YELLOW"
    fi
    
    if [ -n "$FRONTEND_PID" ] && kill -0 "$FRONTEND_PID" 2>/dev/null; then
        print_status "$CHECK" "Processo Frontend: Rodando (PID: $FRONTEND_PID)" "$GREEN"
    else
        print_status "$WARNING" "Processo Frontend: Não encontrado" "$YELLOW"
    fi
    
    log "Status dos serviços verificado"
}

# Função para mostrar informações de acesso
show_access_info() {
    print_color "$GREEN" "\n🎉 Claudia.AI iniciada com sucesso!"
    print_color "$CYAN" "\n🌐 Informações de acesso:"
    
    echo ""
    print_color "$BLUE" "  Frontend (Interface do usuário):"
    print_color "$WHITE" "    🔗 http://localhost:5173"
    print_color "$GRAY" "    📱 Interface responsiva para desktop e mobile"
    
    echo ""
    print_color "$BLUE" "  Backend (API):"
    print_color "$WHITE" "    🔗 http://localhost:5000"
    print_color "$GRAY" "    📊 Health check: http://localhost:5000/api/health"
    print_color "$GRAY" "    🤖 Status da IA: http://localhost:5000/api/ai/status"
    
    echo ""
    print_color "$YELLOW" "📋 Como usar:"
    echo "  1. Abra o navegador e acesse: http://localhost:5173"
    echo "  2. Clique em 'Nova Conversa' para começar"
    echo "  3. Digite sua mensagem e pressione Enter"
    echo "  4. A Claudia.AI responderá em tempo real"
    
    echo ""
    print_color "$PURPLE" "🛠️ Comandos úteis:"
    echo "  • Parar aplicação: Ctrl+C (neste terminal)"
    echo "  • Parar via script: ./scripts/stop-claudia-ai.sh"
    echo "  • Ver logs: tail -f backend.log frontend.log"
    echo "  • Reiniciar: ./scripts/quick-start.sh"
    
    echo ""
    print_color "$CYAN" "📚 Documentação:"
    echo "  • Guia completo: docs/GUIA_COMPLETO_INSTALACAO_CLAUDIA_AI.md"
    echo "  • Manual do usuário: docs/USER_GUIDE.md"
    echo "  • Estrutura: ESTRUTURA_PROJETO.md"
    
    echo ""
    print_color "$GREEN" "✨ A Claudia.AI está pronta para uso!"
    print_color "$YELLOW" "\nPressione Ctrl+C para parar a aplicação"
    
    log "Informações de acesso exibidas"
}

# Função para monitorar aplicação
monitor_application() {
    print_color "$BLUE" "\n👁️ Monitorando aplicação..."
    print_color "$GRAY" "Pressione Ctrl+C para parar"
    
    local check_interval=30  # Verificar a cada 30 segundos
    local last_check=0
    
    while true; do
        sleep 5
        
        # Verificação periódica
        local current_time=$(date +%s)
        if [ $((current_time - last_check)) -ge $check_interval ]; then
            # Verificar se processos ainda estão rodando
            if [ -n "$BACKEND_PID" ] && ! kill -0 "$BACKEND_PID" 2>/dev/null; then
                print_status "$ERROR" "Backend parou inesperadamente!" "$RED"
                log "❌ Backend parou inesperadamente"
                break
            fi
            
            if [ -n "$FRONTEND_PID" ] && ! kill -0 "$FRONTEND_PID" 2>/dev/null; then
                print_status "$ERROR" "Frontend parou inesperadamente!" "$RED"
                log "❌ Frontend parou inesperadamente"
                break
            fi
            
            # Verificar conectividade
            if ! curl -s http://localhost:5000/api/health >/dev/null 2>&1; then
                print_status "$WARNING" "Backend não está respondendo" "$YELLOW"
                log "⚠️ Backend não está respondendo"
            fi
            
            last_check=$current_time
        fi
    done
}

# Função principal
main() {
    # Cabeçalho
    print_color "$PURPLE" "╔══════════════════════════════════════════════════════════════╗"
    print_color "$PURPLE" "║                    🚀 CLAUDIA.AI                            ║"
    print_color "$PURPLE" "║                Inicialização Rápida v1.0.0                  ║"
    print_color "$PURPLE" "║                                                              ║"
    print_color "$PURPLE" "║        Inteligência Artificial Generativa Pronta!           ║"
    print_color "$PURPLE" "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    
    # Inicializar log
    echo "🚀 Claudia.AI - Inicialização iniciada em $(date)" > "$LOG_FILE"
    log "Iniciando aplicação Claudia.AI"
    
    print_color "$CYAN" "Diretório do projeto: $PROJECT_ROOT"
    print_color "$CYAN" "Log da aplicação: $LOG_FILE"
    echo ""
    
    # Verificar pré-requisitos
    if ! check_basic_requirements; then
        print_status "$ERROR" "Pré-requisitos não atendidos" "$RED"
        print_color "$YELLOW" "Execute primeiro: ./scripts/install-claudia-ai.sh"
        exit 1
    fi
    
    # Inicializar banco de dados se necessário
    if ! init_database; then
        print_status "$ERROR" "Erro ao inicializar banco de dados" "$RED"
        exit 1
    fi
    
    # Iniciar serviços
    if start_backend && start_frontend; then
        # Aguardar um pouco para estabilizar
        sleep 3
        
        # Verificar status
        check_services_status
        
        # Mostrar informações de acesso
        show_access_info
        
        # Monitorar aplicação
        monitor_application
    else
        print_status "$ERROR" "Erro ao iniciar serviços" "$RED"
        print_color "$YELLOW" "Verifique os logs: backend.log e frontend.log"
        exit 1
    fi
}

# Verificar se está sendo executado diretamente
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi

