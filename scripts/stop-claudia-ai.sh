#!/bin/bash

# ⏹️ Claudia.AI - Script de Parada
# Versão: 1.0.0
# Autor: Manus AI
# Data: Janeiro 2024

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
STOP="⏹️"

# Variáveis globais
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
LOG_FILE="$PROJECT_ROOT/claudia-ai.log"

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

# Função para parar processos por nome
stop_processes_by_name() {
    local process_pattern=$1
    local description=$2
    
    local pids=$(pgrep -f "$process_pattern" 2>/dev/null || true)
    
    if [ -n "$pids" ]; then
        print_status "$INFO" "Parando $description..." "$CYAN"
        
        for pid in $pids; do
            local process_info=$(ps -p $pid -o pid,comm,args --no-headers 2>/dev/null || echo "")
            if [ -n "$process_info" ]; then
                print_color "$GRAY" "  Parando PID $pid: $(echo $process_info | cut -d' ' -f2-)"
                
                # Tentar parada gentil primeiro
                kill -TERM $pid 2>/dev/null || true
                
                # Aguardar um pouco
                sleep 2
                
                # Verificar se ainda está rodando
                if kill -0 $pid 2>/dev/null; then
                    print_color "$YELLOW" "    Forçando parada do PID $pid..."
                    kill -KILL $pid 2>/dev/null || true
                fi
            fi
        done
        
        print_status "$CHECK" "$description parados" "$GREEN"
        log "✅ $description parados"
    else
        print_status "$INFO" "Nenhum processo $description encontrado" "$CYAN"
    fi
}

# Função para parar por porta
stop_processes_by_port() {
    local port=$1
    local description=$2
    
    local pids=$(lsof -ti:$port 2>/dev/null || true)
    
    if [ -n "$pids" ]; then
        print_status "$INFO" "Parando processos na porta $port ($description)..." "$CYAN"
        
        for pid in $pids; do
            local process_info=$(ps -p $pid -o pid,comm,args --no-headers 2>/dev/null || echo "")
            if [ -n "$process_info" ]; then
                print_color "$GRAY" "  Parando PID $pid na porta $port"
                
                # Tentar parada gentil primeiro
                kill -TERM $pid 2>/dev/null || true
                
                # Aguardar um pouco
                sleep 2
                
                # Verificar se ainda está rodando
                if kill -0 $pid 2>/dev/null; then
                    print_color "$YELLOW" "    Forçando parada do PID $pid..."
                    kill -KILL $pid 2>/dev/null || true
                fi
            fi
        done
        
        print_status "$CHECK" "Processos na porta $port parados" "$GREEN"
        log "✅ Processos na porta $port parados"
    else
        print_status "$INFO" "Nenhum processo na porta $port" "$CYAN"
    fi
}

# Função para limpar arquivos temporários
cleanup_temp_files() {
    print_status "$INFO" "Limpando arquivos temporários..." "$CYAN"
    
    # Remover arquivos de log temporários se existirem
    local temp_files=(
        "$PROJECT_ROOT/backend.log"
        "$PROJECT_ROOT/frontend.log"
        "$PROJECT_ROOT/nohup.out"
        "$PROJECT_ROOT/.claudia-ai.pid"
    )
    
    for file in "${temp_files[@]}"; do
        if [ -f "$file" ]; then
            rm -f "$file" 2>/dev/null || true
            print_color "$GRAY" "  Removido: $(basename $file)"
        fi
    done
    
    # Limpar cache do npm/pnpm se necessário
    if [ -d "$PROJECT_ROOT/claudia-ai-frontend/.vite" ]; then
        rm -rf "$PROJECT_ROOT/claudia-ai-frontend/.vite" 2>/dev/null || true
        print_color "$GRAY" "  Cache Vite limpo"
    fi
    
    print_status "$CHECK" "Arquivos temporários limpos" "$GREEN"
    log "✅ Arquivos temporários limpos"
}

# Função para verificar se processos foram realmente parados
verify_stop() {
    print_status "$INFO" "Verificando se todos os processos foram parados..." "$CYAN"
    
    local remaining_processes=false
    
    # Verificar processos do backend
    local backend_pids=$(pgrep -f "python.*src/main.py" 2>/dev/null || true)
    if [ -n "$backend_pids" ]; then
        print_status "$WARNING" "Ainda há processos backend rodando: $backend_pids" "$YELLOW"
        remaining_processes=true
    fi
    
    # Verificar processos do frontend
    local frontend_pids=$(pgrep -f "vite" 2>/dev/null || true)
    if [ -n "$frontend_pids" ]; then
        print_status "$WARNING" "Ainda há processos frontend rodando: $frontend_pids" "$YELLOW"
        remaining_processes=true
    fi
    
    # Verificar portas
    if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1; then
        print_status "$WARNING" "Porta 5000 ainda está em uso" "$YELLOW"
        remaining_processes=true
    fi
    
    if lsof -Pi :5173 -sTCP:LISTEN -t >/dev/null 2>&1; then
        print_status "$WARNING" "Porta 5173 ainda está em uso" "$YELLOW"
        remaining_processes=true
    fi
    
    if [ "$remaining_processes" = false ]; then
        print_status "$CHECK" "Todos os processos foram parados com sucesso" "$GREEN"
        log "✅ Verificação de parada bem-sucedida"
        return 0
    else
        print_status "$WARNING" "Alguns processos podem ainda estar rodando" "$YELLOW"
        log "⚠️ Alguns processos podem ainda estar rodando"
        return 1
    fi
}

# Função para parada forçada
force_stop() {
    print_status "$WARNING" "Executando parada forçada..." "$YELLOW"
    log "Executando parada forçada"
    
    # Parar todos os processos Python relacionados
    pkill -9 -f "python.*claudia" 2>/dev/null || true
    pkill -9 -f "python.*main.py" 2>/dev/null || true
    pkill -9 -f "flask" 2>/dev/null || true
    
    # Parar todos os processos Node relacionados
    pkill -9 -f "vite" 2>/dev/null || true
    pkill -9 -f "node.*claudia" 2>/dev/null || true
    
    # Parar por porta
    fuser -k 5000/tcp 2>/dev/null || true
    fuser -k 5173/tcp 2>/dev/null || true
    
    sleep 3
    
    print_status "$CHECK" "Parada forçada concluída" "$GREEN"
    log "✅ Parada forçada concluída"
}

# Função para mostrar status final
show_final_status() {
    print_color "$GREEN" "\n$STOP Claudia.AI parada com sucesso!"
    
    # Mostrar resumo
    print_color "$CYAN" "\n📊 Resumo:"
    print_status "$CHECK" "Backend parado" "$GREEN"
    print_status "$CHECK" "Frontend parado" "$GREEN"
    print_status "$CHECK" "Portas liberadas (5000, 5173)" "$GREEN"
    print_status "$CHECK" "Arquivos temporários limpos" "$GREEN"
    
    print_color "$BLUE" "\n🔄 Para reiniciar:"
    echo "  ./scripts/quick-start.sh"
    
    print_color "$YELLOW" "\n📋 Logs salvos em:"
    echo "  $LOG_FILE"
    
    if [ -f "$PROJECT_ROOT/claudia-ai-backend/logs/app.log" ]; then
        echo "  $PROJECT_ROOT/claudia-ai-backend/logs/app.log"
    fi
    
    log "✅ Claudia.AI parada com sucesso"
}

# Função principal
main() {
    # Cabeçalho
    print_color "$PURPLE" "╔══════════════════════════════════════════════════════════════╗"
    print_color "$PURPLE" "║                    ⏹️ CLAUDIA.AI                            ║"
    print_color "$PURPLE" "║                  Script de Parada v1.0.0                    ║"
    print_color "$PURPLE" "║                                                              ║"
    print_color "$PURPLE" "║            Parando todos os serviços com segurança          ║"
    print_color "$PURPLE" "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    
    log "$STOP Claudia.AI - Parada iniciada em $(date)"
    
    print_color "$CYAN" "Diretório do projeto: $PROJECT_ROOT"
    echo ""
    
    # Parar processos específicos do backend
    stop_processes_by_name "python.*src/main.py" "Backend Python"
    stop_processes_by_name "python.*claudia" "Processos Python da Claudia.AI"
    
    # Parar processos específicos do frontend
    stop_processes_by_name "vite" "Frontend Vite"
    stop_processes_by_name "node.*claudia" "Processos Node da Claudia.AI"
    
    # Parar por porta como backup
    stop_processes_by_port 5000 "Backend"
    stop_processes_by_port 5173 "Frontend"
    
    # Aguardar um pouco para os processos terminarem
    print_status "$INFO" "Aguardando processos terminarem..." "$CYAN"
    sleep 3
    
    # Verificar se parada foi bem-sucedida
    if ! verify_stop; then
        print_color "$YELLOW" "\nAlguns processos ainda estão rodando."
        read -p "Deseja forçar a parada? (s/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Ss]$ ]]; then
            force_stop
        else
            print_status "$WARNING" "Parada parcial. Alguns processos podem ainda estar rodando" "$YELLOW"
        fi
    fi
    
    # Limpar arquivos temporários
    cleanup_temp_files
    
    # Mostrar status final
    show_final_status
}

# Verificar argumentos
case "${1:-}" in
    --force|-f)
        print_color "$YELLOW" "🔥 Modo forçado ativado"
        echo ""
        log "Parada forçada solicitada"
        force_stop
        cleanup_temp_files
        show_final_status
        ;;
    --help|-h)
        print_color "$BLUE" "📖 Uso: $0 [opções]"
        echo ""
        echo "Opções:"
        echo "  --force, -f    Parada forçada (kill -9)"
        echo "  --help, -h     Mostrar esta ajuda"
        echo ""
        echo "Exemplos:"
        echo "  $0             Parada normal"
        echo "  $0 --force     Parada forçada"
        ;;
    *)
        # Verificar se está sendo executado diretamente
        if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
            main "$@"
        fi
        ;;
esac

