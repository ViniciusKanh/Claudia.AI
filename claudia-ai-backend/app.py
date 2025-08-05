#!/usr/bin/env python3
"""
Ponto de entrada para deploy da Claudia.AI
Este arquivo é usado por serviços de deploy como Gunicorn, uWSGI, etc.
"""

from src.main import create_app

# Criar instância da aplicação
app = create_app()

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(host='0.0.0.0', port=5000, debug=True)

