#!/usr/bin/env python3
"""
Arquivo principal para deploy da Claudia.AI
"""

import os
import sys

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importa a aplicação Flask
from src.main import app

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(host='0.0.0.0', port=5000, debug=False)
else:
    # Para deploy em produção
    application = app

