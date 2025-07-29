# 🤖 Scripts Automatizados - Claudia.AI

## 📋 Visão Geral

Este documento descreve os scripts automatizados criados para facilitar a instalação, execução e manutenção da Claudia.AI. Os scripts foram desenvolvidos para funcionar em sistemas Linux, macOS e Windows (via Git Bash/WSL), oferecendo uma experiência de desenvolvimento simplificada e eficiente.

## 📁 Scripts Disponíveis

### 1. install-claudia-ai.sh
**Propósito**: Verificação automática de pré-requisitos do sistema
**Uso**: `./install-claudia-ai.sh`

Este script verifica se todos os pré-requisitos necessários estão instalados no sistema:
- Python 3.8+
- Node.js 18+
- Git
- Detecta automaticamente o sistema operacional

### 2. quick-start.sh
**Propósito**: Início rápido da aplicação completa
**Uso**: `./quick-start.sh`

Script principal para iniciar a Claudia.AI com um único comando:
- Verifica estrutura do projeto
- Cria ambiente virtual Python (se necessário)
- Instala dependências automaticamente
- Inicia backend e frontend
- Verifica status dos serviços
- Exibe informações de acesso

### 3. stop-claudia-ai.sh
**Propósito**: Parada segura de todos os serviços
**Uso**: `./stop-claudia-ai.sh`

Para todos os processos da Claudia.AI de forma segura:
- Para backend usando PID files
- Para frontend usando PID files
- Verifica processos restantes
- Limpeza de arquivos temporários

## 🚀 Uso Rápido

### Primeira Execução
```bash
# 1. Verificar pré-requisitos
./install-claudia-ai.sh

# 2. Iniciar aplicação
./quick-start.sh

# 3. Acessar no navegador
# http://localhost:5173
```

### Uso Diário
```bash
# Iniciar
./quick-start.sh

# Parar
./stop-claudia-ai.sh
```

## 🔧 Funcionalidades dos Scripts

### Detecção Automática de Sistema
Os scripts detectam automaticamente:
- Linux (Ubuntu, Debian, CentOS, etc.)
- macOS
- Windows (Git Bash, WSL)

### Gerenciamento de Dependências
- **Backend**: Criação automática de ambiente virtual Python
- **Frontend**: Detecção e uso de pnpm ou npm
- **Instalação inteligente**: Só instala se necessário

### Monitoramento de Processos
- **PID Files**: Rastreamento seguro de processos
- **Health Checks**: Verificação automática de status
- **Cleanup**: Limpeza automática ao parar

### Feedback Visual
- **Cores**: Output colorido para melhor legibilidade
- **Status**: Indicadores claros de progresso
- **Erros**: Mensagens de erro detalhadas

## 📊 Saída dos Scripts

### install-claudia-ai.sh
```
==========================================
    Instalação Automática Claudia.AI     
==========================================

[INFO] Sistema detectado: linux
[INFO] Verificando pré-requisitos...
[SUCCESS] Python encontrado: 3.11.0
[SUCCESS] Node.js encontrado: v20.18.0
[SUCCESS] Git encontrado: git version 2.34.1
[SUCCESS] Pré-requisitos verificados! Pronto para instalação.
```

### quick-start.sh
```
==========================================
         Claudia.AI - Início Rápido      
==========================================

[SUCCESS] Estrutura do projeto verificada
[INFO] Iniciando backend...
[SUCCESS] Backend iniciado (PID: 12345)
[INFO] Iniciando frontend...
[SUCCESS] Frontend iniciado (PID: 12346)
[SUCCESS] ✓ Backend: Online (http://localhost:5000)
[SUCCESS] ✓ Frontend: Online (http://localhost:5173)

==========================================
         Claudia.AI está rodando!         
==========================================

🌐 Acesse a aplicação em:
   http://localhost:5173

🔧 API Backend disponível em:
   http://localhost:5000/api
```

### stop-claudia-ai.sh
```
==========================================
         Parando Claudia.AI              
==========================================

[INFO] Parando backend (PID: 12345)...
[SUCCESS] Backend parado
[INFO] Parando frontend (PID: 12346)...
[SUCCESS] Frontend parado
[SUCCESS] Todos os processos da Claudia.AI foram parados

Claudia.AI parada com sucesso!
Para iniciar novamente, execute: ./quick-start.sh
```

## 🛠️ Personalização dos Scripts

### Modificar Portas
Para alterar as portas padrão, edite as variáveis nos scripts:

```bash
# Em quick-start.sh
BACKEND_PORT=5000
FRONTEND_PORT=5173

# Em stop-claudia-ai.sh
# Atualize as verificações de porta correspondentes
```

### Adicionar Verificações
Para adicionar novas verificações de pré-requisitos:

```bash
# Em install-claudia-ai.sh
check_custom_tool() {
    if command_exists custom-tool; then
        print_success "Custom tool encontrado"
    else
        print_warning "Custom tool não encontrado (opcional)"
    fi
}

# Adicione à função check_prerequisites
check_custom_tool
```

### Configurar Ambiente
Para configurações específicas de ambiente:

```bash
# Criar arquivo .env automaticamente
create_env_files() {
    if [ ! -f "claudia-ai-backend/.env" ]; then
        cat > claudia-ai-backend/.env << EOF
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=auto-generated-key-$(date +%s)
EOF
    fi
}
```

## 🔍 Solução de Problemas

### Script não executa
```bash
# Verificar permissões
ls -la *.sh

# Tornar executável
chmod +x *.sh
```

### Erro de dependências
```bash
# Forçar reinstalação
rm -rf claudia-ai-backend/venv
rm -rf claudia-ai-frontend/node_modules
./quick-start.sh
```

### Processos não param
```bash
# Força parada de todos os processos
pkill -f "python.*claudia"
pkill -f "vite.*dev"
```

### Portas em uso
```bash
# Verificar processos usando as portas
lsof -i :5000
lsof -i :5173

# Matar processo específico
kill -9 PID
```

## 📈 Melhorias Futuras

### Funcionalidades Planejadas
- **Docker Support**: Scripts para execução com Docker
- **Production Mode**: Scripts para deploy em produção
- **Backup/Restore**: Scripts para backup de dados
- **Update System**: Scripts para atualização automática
- **Health Monitoring**: Monitoramento contínuo de saúde

### Contribuições
Para contribuir com melhorias nos scripts:
1. Teste em diferentes sistemas operacionais
2. Adicione verificações de erro mais robustas
3. Implemente funcionalidades de logging
4. Crie testes automatizados para os scripts

## 📝 Notas Importantes

### Compatibilidade
- **Linux**: Testado em Ubuntu 20.04+, Debian 10+
- **macOS**: Testado em macOS 10.15+
- **Windows**: Requer Git Bash ou WSL2

### Segurança
- Scripts não executam comandos como root por padrão
- Verificação de integridade de arquivos
- Limpeza automática de processos órfãos

### Performance
- Instalação incremental de dependências
- Cache de verificações de pré-requisitos
- Início paralelo de serviços quando possível

---

**Desenvolvido para facilitar o desenvolvimento com Claudia.AI**  
*Versão: 1.0.0*  
*Compatibilidade: Linux, macOS, Windows*

