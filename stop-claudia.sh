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
