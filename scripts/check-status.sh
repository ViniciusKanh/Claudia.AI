#!/bin/bash

# 🔍 Claudia.AI - Script de Verificação de Status
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
GRAY='\033[0;37m'
NC='\033[0m' # No Color

# Símbolos
CHECK="✅"
ERROR="❌"
WARNING="⚠️"
INFO="ℹ️"
SEARCH="🔍"
GEAR="⚙️"

# Variáveis globais
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BACKEND_DIR="$PROJECT_ROOT/claudia-ai-backend"
FRONTEND_DIR="$PROJECT_ROOT/claudia-ai-frontend"

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

# Função para verificar conectividade HTTP
check_http() {
    local url=$1
    local timeout=${2:-5}
    
    if curl -s --max-time $timeout "$url" >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Função para obter resposta HTTP
get_http_response() {
    local url=$1
    local timeout=${2:-5}
    
    curl -s --max-time $timeout "$url" 2>/dev/null || echo "N/A"
}

# Função para verificar processos
check_processes() {
    print_color "$BLUE" "\n🔍 Verificando Processos..."
    
    # Verificar processos do backend
    local backend_pids=$(pgrep -f "python.*src/main.py" 2>/dev/null || true)
    if [ -n "$backend_pids" ]; then
        print_status "$CHECK" "Backend Python: Rodando" "$GREEN"
        for pid in $backend_pids; do
            local process_info=$(ps -p $pid -o pid,ppid,etime,cmd --no-headers 2>/dev/null || echo "")
            if [ -n "$process_info" ]; then
                print_color "$GRAY" "  PID $pid: $(echo $process_info | awk '{print $3}') - $(echo $process_info | awk '{for(i=4;i<=NF;i++) printf "%s ", $i; print ""}')"
            fi
        done
    else
        print_status "$ERROR" "Backend Python: Não encontrado" "$RED"
    fi
    
    # Verificar processos do frontend
    local frontend_pids=$(pgrep -f "vite" 2>/dev/null || true)
    if [ -n "$frontend_pids" ]; then
        print_status "$CHECK" "Frontend Vite: Rodando" "$GREEN"
        for pid in $frontend_pids; do
            local process_info=$(ps -p $pid -o pid,ppid,etime,cmd --no-headers 2>/dev/null || echo "")
            if [ -n "$process_info" ]; then
                print_color "$GRAY" "  PID $pid: $(echo $process_info | awk '{print $3}') - vite dev server"
            fi
        done
    else
        print_status "$ERROR" "Frontend Vite: Não encontrado" "$RED"
    fi
    
    # Verificar outros processos relacionados
    local other_pids=$(pgrep -f "claudia" 2>/dev/null | grep -v $$ || true)
    if [ -n "$other_pids" ]; then
        print_status "$INFO" "Outros processos Claudia.AI:" "$CYAN"
        for pid in $other_pids; do
            local process_info=$(ps -p $pid -o pid,comm,args --no-headers 2>/dev/null || echo "")
            if [ -n "$process_info" ]; then
                print_color "$GRAY" "  $process_info"
            fi
        done
    fi
}

# Função para verificar portas
check_ports() {
    print_color "$BLUE" "\n🌐 Verificando Portas..."
    
    # Verificar porta 5000 (Backend)
    if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1; then
        local process=$(lsof -Pi :5000 -sTCP:LISTEN -t 2>/dev/null | head -1)
        local process_name=$(ps -p $process -o comm= 2>/dev/null || echo "desconhecido")
        print_status "$CHECK" "Porta 5000 (Backend): Em uso" "$GREEN"
        print_color "$GRAY" "  Processo: $process_name (PID: $process)"
    else
        print_status "$ERROR" "Porta 5000 (Backend): Livre" "$RED"
    fi
    
    # Verificar porta 5173 (Frontend)
    if lsof -Pi :5173 -sTCP:LISTEN -t >/dev/null 2>&1; then
        local process=$(lsof -Pi :5173 -sTCP:LISTEN -t 2>/dev/null | head -1)
        local process_name=$(ps -p $process -o comm= 2>/dev/null || echo "desconhecido")
        print_status "$CHECK" "Porta 5173 (Frontend): Em uso" "$GREEN"
        print_color "$GRAY" "  Processo: $process_name (PID: $process)"
    else
        print_status "$ERROR" "Porta 5173 (Frontend): Livre" "$RED"
    fi
    
    # Verificar outras portas comuns
    local common_ports=(3000 8000 8080 3001 5001)
    local found_ports=()
    
    for port in "${common_ports[@]}"; do
        if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
            found_ports+=($port)
        fi
    done
    
    if [ ${#found_ports[@]} -gt 0 ]; then
        print_status "$INFO" "Outras portas em uso: ${found_ports[*]}" "$CYAN"
    fi
}

# Função para verificar conectividade
check_connectivity() {
    print_color "$BLUE" "\n🌐 Verificando Conectividade..."
    
    # Verificar backend
    print_status "$INFO" "Testando backend (http://localhost:5000)..." "$CYAN"
    if check_http "http://localhost:5000"; then
        print_status "$CHECK" "Backend: Acessível" "$GREEN"
        
        # Testar health check
        local health_response=$(get_http_response "http://localhost:5000/api/health")
        if [ "$health_response" != "N/A" ]; then
            print_color "$GRAY" "  Health: $health_response"
        fi
        
        # Testar status da IA
        local ai_status=$(get_http_response "http://localhost:5000/api/ai/status")
        if [ "$ai_status" != "N/A" ]; then
            print_color "$GRAY" "  IA Status: $ai_status"
        fi
        
        # Testar info da API
        local api_info=$(get_http_response "http://localhost:5000/api/info")
        if [ "$api_info" != "N/A" ]; then
            local endpoint_count=$(echo "$api_info" | grep -o '"/' | wc -l 2>/dev/null || echo "N/A")
            print_color "$GRAY" "  Endpoints disponíveis: $endpoint_count"
        fi
    else
        print_status "$ERROR" "Backend: Inacessível" "$RED"
    fi
    
    # Verificar frontend
    print_status "$INFO" "Testando frontend (http://localhost:5173)..." "$CYAN"
    if check_http "http://localhost:5173"; then
        print_status "$CHECK" "Frontend: Acessível" "$GREEN"
        
        # Verificar se é uma página válida
        local response=$(curl -s --max-time 5 "http://localhost:5173" 2>/dev/null || echo "")
        if echo "$response" | grep -q "Claudia.AI" 2>/dev/null; then
            print_color "$GRAY" "  Página: Claudia.AI carregada corretamente"
        elif echo "$response" | grep -q "<!DOCTYPE html>" 2>/dev/null; then
            print_color "$GRAY" "  Página: HTML válido detectado"
        else
            print_color "$YELLOW" "  Página: Resposta inesperada"
        fi
    else
        print_status "$ERROR" "Frontend: Inacessível" "$RED"
    fi
}

# Função para verificar arquivos e configuração
check_files() {
    print_color "$BLUE" "\n📁 Verificando Arquivos e Configuração..."
    
    # Verificar estrutura do projeto
    local required_dirs=(
        "$BACKEND_DIR"
        "$FRONTEND_DIR"
        "$BACKEND_DIR/src"
        "$FRONTEND_DIR/src"
    )
    
    for dir in "${required_dirs[@]}"; do
        if [ -d "$dir" ]; then
            print_status "$CHECK" "Diretório: $(basename $dir)" "$GREEN"
        else
            print_status "$ERROR" "Diretório: $(basename $dir) - Não encontrado" "$RED"
        fi
    done
    
    # Verificar arquivos importantes do backend
    local backend_files=(
        "$BACKEND_DIR/requirements.txt"
        "$BACKEND_DIR/.env"
        "$BACKEND_DIR/src/main.py"
        "$BACKEND_DIR/venv"
    )
    
    print_color "$CYAN" "\n  Backend:"
    for file in "${backend_files[@]}"; do
        if [ -e "$file" ]; then
            if [ -d "$file" ]; then
                print_status "$CHECK" "$(basename $file)/ (diretório)" "$GREEN"
            else
                local size=$(du -h "$file" 2>/dev/null | cut -f1 || echo "N/A")
                print_status "$CHECK" "$(basename $file) ($size)" "$GREEN"
            fi
        else
            print_status "$ERROR" "$(basename $file) - Não encontrado" "$RED"
        fi
    done
    
    # Verificar arquivos importantes do frontend
    local frontend_files=(
        "$FRONTEND_DIR/package.json"
        "$FRONTEND_DIR/.env"
        "$FRONTEND_DIR/src/App.jsx"
        "$FRONTEND_DIR/node_modules"
    )
    
    print_color "$CYAN" "\n  Frontend:"
    for file in "${frontend_files[@]}"; do
        if [ -e "$file" ]; then
            if [ -d "$file" ]; then
                local count=$(find "$file" -type f 2>/dev/null | wc -l || echo "N/A")
                print_status "$CHECK" "$(basename $file)/ ($count arquivos)" "$GREEN"
            else
                local size=$(du -h "$file" 2>/dev/null | cut -f1 || echo "N/A")
                print_status "$CHECK" "$(basename $file) ($size)" "$GREEN"
            fi
        else
            print_status "$ERROR" "$(basename $file) - Não encontrado" "$RED"
        fi
    done
    
    # Verificar banco de dados
    if [ -f "$BACKEND_DIR/src/database/app.db" ]; then
        local db_size=$(du -h "$BACKEND_DIR/src/database/app.db" 2>/dev/null | cut -f1 || echo "N/A")
        print_status "$CHECK" "Banco de dados: app.db ($db_size)" "$GREEN"
    else
        print_status "$WARNING" "Banco de dados: Não criado ainda" "$YELLOW"
    fi
}

# Função para verificar logs
check_logs() {
    print_color "$BLUE" "\n📋 Verificando Logs..."
    
    local log_files=(
        "$PROJECT_ROOT/claudia-ai.log"
        "$PROJECT_ROOT/install.log"
        "$BACKEND_DIR/logs/app.log"
        "$BACKEND_DIR/logs/error.log"
        "$PROJECT_ROOT/backend.log"
        "$PROJECT_ROOT/frontend.log"
    )
    
    local found_logs=false
    
    for log_file in "${log_files[@]}"; do
        if [ -f "$log_file" ]; then
            local size=$(du -h "$log_file" 2>/dev/null | cut -f1 || echo "N/A")
            local lines=$(wc -l < "$log_file" 2>/dev/null || echo "N/A")
            print_status "$CHECK" "$(basename $log_file): $size ($lines linhas)" "$GREEN"
            
            # Mostrar últimas linhas se houver erros recentes
            if grep -q "ERROR\|CRITICAL" "$log_file" 2>/dev/null; then
                local error_count=$(grep -c "ERROR\|CRITICAL" "$log_file" 2>/dev/null || echo "0")
                print_color "$YELLOW" "    ⚠️ $error_count erro(s) encontrado(s)"
            fi
            
            found_logs=true
        fi
    done
    
    if [ "$found_logs" = false ]; then
        print_status "$INFO" "Nenhum arquivo de log encontrado" "$CYAN"
    fi
}

# Função para verificar recursos do sistema
check_system_resources() {
    print_color "$BLUE" "\n💻 Verificando Recursos do Sistema..."
    
    # Verificar CPU
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1 2>/dev/null || echo "N/A")
    print_status "$INFO" "CPU: ${cpu_usage}% em uso" "$CYAN"
    
    # Verificar memória
    local mem_info=$(free -h | grep "Mem:" 2>/dev/null || echo "N/A N/A N/A")
    local mem_total=$(echo $mem_info | awk '{print $2}')
    local mem_used=$(echo $mem_info | awk '{print $3}')
    local mem_available=$(echo $mem_info | awk '{print $7}')
    print_status "$INFO" "Memória: $mem_used/$mem_total usado ($mem_available disponível)" "$CYAN"
    
    # Verificar espaço em disco
    local disk_info=$(df -h . | tail -1 2>/dev/null || echo "N/A N/A N/A N/A")
    local disk_size=$(echo $disk_info | awk '{print $2}')
    local disk_used=$(echo $disk_info | awk '{print $3}')
    local disk_available=$(echo $disk_info | awk '{print $4}')
    local disk_percent=$(echo $disk_info | awk '{print $5}')
    print_status "$INFO" "Disco: $disk_used/$disk_size usado ($disk_available disponível, $disk_percent)" "$CYAN"
    
    # Verificar carga do sistema
    local load_avg=$(uptime | awk -F'load average:' '{print $2}' | sed 's/^[ \t]*//' 2>/dev/null || echo "N/A")
    print_status "$INFO" "Carga média: $load_avg" "$CYAN"
}

# Função para mostrar resumo
show_summary() {
    print_color "$GREEN" "\n📊 Resumo do Status:"
    
    local backend_running=false
    local frontend_running=false
    local backend_accessible=false
    local frontend_accessible=false
    
    # Verificar status dos serviços
    if pgrep -f "python.*src/main.py" >/dev/null 2>&1; then
        backend_running=true
    fi
    
    if pgrep -f "vite" >/dev/null 2>&1; then
        frontend_running=true
    fi
    
    if check_http "http://localhost:5000"; then
        backend_accessible=true
    fi
    
    if check_http "http://localhost:5173"; then
        frontend_accessible=true
    fi
    
    # Mostrar status
    echo ""
    if [ "$backend_running" = true ] && [ "$backend_accessible" = true ]; then
        print_status "$CHECK" "Backend: Funcionando corretamente" "$GREEN"
    elif [ "$backend_running" = true ]; then
        print_status "$WARNING" "Backend: Rodando mas inacessível" "$YELLOW"
    else
        print_status "$ERROR" "Backend: Não está rodando" "$RED"
    fi
    
    if [ "$frontend_running" = true ] && [ "$frontend_accessible" = true ]; then
        print_status "$CHECK" "Frontend: Funcionando corretamente" "$GREEN"
    elif [ "$frontend_running" = true ]; then
        print_status "$WARNING" "Frontend: Rodando mas inacessível" "$YELLOW"
    else
        print_status "$ERROR" "Frontend: Não está rodando" "$RED"
    fi
    
    # Status geral
    if [ "$backend_running" = true ] && [ "$frontend_running" = true ] && [ "$backend_accessible" = true ] && [ "$frontend_accessible" = true ]; then
        print_color "$GREEN" "\n🎉 Claudia.AI está funcionando perfeitamente!"
        print_color "$CYAN" "\n🌐 Acesse: http://localhost:5173"
    elif [ "$backend_running" = true ] || [ "$frontend_running" = true ]; then
        print_color "$YELLOW" "\n⚠️ Claudia.AI está parcialmente funcionando"
        print_color "$CYAN" "\nPara iniciar completamente: ./scripts/quick-start.sh"
    else
        print_color "$RED" "\n❌ Claudia.AI não está rodando"
        print_color "$CYAN" "\nPara iniciar: ./scripts/quick-start.sh"
    fi
    
    print_color "$BLUE" "\n🛠️ Comandos úteis:"
    echo "  • Iniciar: ./scripts/quick-start.sh"
    echo "  • Parar: ./scripts/stop-claudia-ai.sh"
    echo "  • Status: ./scripts/check-status.sh"
    echo "  • Logs: tail -f claudia-ai.log"
}

# Função principal
main() {
    # Cabeçalho
    print_color "$PURPLE" "╔══════════════════════════════════════════════════════════════╗"
    print_color "$PURPLE" "║                    🔍 CLAUDIA.AI                            ║"
    print_color "$PURPLE" "║               Verificação de Status v1.0.0                  ║"
    print_color "$PURPLE" "║                                                              ║"
    print_color "$PURPLE" "║              Diagnóstico Completo do Sistema                ║"
    print_color "$PURPLE" "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    
    print_color "$CYAN" "Diretório do projeto: $PROJECT_ROOT"
    print_color "$CYAN" "Verificação iniciada em: $(date)"
    
    # Executar verificações
    check_processes
    check_ports
    check_connectivity
    check_files
    check_logs
    check_system_resources
    show_summary
    
    echo ""
}

# Verificar argumentos
case "${1:-}" in
    --help|-h)
        print_color "$BLUE" "📖 Uso: $0 [opções]"
        echo ""
        echo "Opções:"
        echo "  --help, -h     Mostrar esta ajuda"
        echo ""
        echo "Este script verifica o status completo da Claudia.AI:"
        echo "  • Processos em execução"
        echo "  • Portas de rede"
        echo "  • Conectividade HTTP"
        echo "  • Arquivos e configuração"
        echo "  • Logs do sistema"
        echo "  • Recursos do sistema"
        ;;
    *)
        # Verificar se está sendo executado diretamente
        if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
            main "$@"
        fi
        ;;
esac

