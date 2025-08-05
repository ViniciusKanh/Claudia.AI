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
