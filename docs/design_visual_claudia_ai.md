# Design Visual Claudia.AI - Especificações de Interface

**Autor**: Manus AI  
**Data**: 28 de Julho de 2025  
**Versão**: 1.0

## 1. Conceito Visual Geral

### 1.1 Filosofia de Design

O design da Claudia.AI segue uma filosofia de "Inteligência Natural", combinando elementos orgânicos inspirados na natureza com a precisão e clareza da tecnologia moderna. A interface busca transmitir confiança, sustentabilidade e inovação através de uma estética limpa e acolhedora.

**Princípios Fundamentais:**
- **Biofilia**: Conexão com elementos naturais através das cores verdes
- **Minimalismo Funcional**: Cada elemento tem propósito claro
- **Acessibilidade Universal**: Design inclusivo para todos os usuários
- **Sustentabilidade Visual**: Paleta que reflete valores ambientais
- **Inteligência Transparente**: IA explicável através do design

### 1.2 Identidade da Marca

**Nome**: Claudia.AI  
**Tagline**: "Inteligência que cresce com você"  
**Personalidade**: Inteligente, Amigável, Confiável, Sustentável, Inovadora

## 2. Sistema de Cores Detalhado

### 2.1 Paleta Principal

```css
/* Cores Primárias */
--verde-primario: #2D5A27;     /* Verde floresta profundo */
--verde-secundario: #4A7C59;   /* Verde musgo */
--verde-accent: #7FB069;       /* Verde claro vibrante */
--branco-principal: #FFFFFF;   /* Branco puro */
--branco-secundario: #F8F9FA;  /* Branco off-white */

/* Cores de Texto */
--texto-primario: #2C3E50;     /* Cinza escuro */
--texto-secundario: #5D6D7E;   /* Cinza médio */
--texto-terciario: #85929E;    /* Cinza claro */

/* Cores de Estado */
--sucesso: #27AE60;            /* Verde sucesso */
--aviso: #F39C12;              /* Laranja suave */
--erro: #E74C3C;               /* Vermelho suave */
--info: #3498DB;               /* Azul informativo */

/* Cores de Gradiente */
--gradiente-principal: linear-gradient(135deg, #2D5A27 0%, #4A7C59 100%);
--gradiente-accent: linear-gradient(135deg, #7FB069 0%, #4A7C59 100%);
--gradiente-fundo: linear-gradient(180deg, #F8F9FA 0%, #FFFFFF 100%);
```

### 2.2 Aplicação das Cores

**Hierarquia Visual:**
- **Verde Primário**: Cabeçalhos, CTAs principais, logo
- **Verde Secundário**: Elementos interativos, hover states
- **Verde Accent**: Destaques, notificações positivas, badges
- **Branco Principal**: Backgrounds principais, texto em fundos escuros
- **Branco Secundário**: Backgrounds secundários, cards, modais

## 3. Tipografia e Hierarquia

### 3.1 Família de Fontes

```css
/* Fonte Principal - Inter */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Fonte de Código - JetBrains Mono */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

/* Fonte de Títulos - Poppins */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

:root {
  --font-principal: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-codigo: 'JetBrains Mono', 'Courier New', monospace;
  --font-titulos: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

### 3.2 Escala Tipográfica

```css
/* Hierarquia de Tamanhos */
--texto-xs: 0.75rem;    /* 12px - Legendas, timestamps */
--texto-sm: 0.875rem;   /* 14px - Texto auxiliar */
--texto-base: 1rem;     /* 16px - Texto padrão */
--texto-lg: 1.125rem;   /* 18px - Texto destacado */
--texto-xl: 1.25rem;    /* 20px - Subtítulos */
--texto-2xl: 1.5rem;    /* 24px - Títulos de seção */
--texto-3xl: 1.875rem;  /* 30px - Títulos principais */
--texto-4xl: 2.25rem;   /* 36px - Títulos de página */
--texto-5xl: 3rem;      /* 48px - Títulos hero */

/* Pesos de Fonte */
--peso-light: 300;
--peso-normal: 400;
--peso-medium: 500;
--peso-semibold: 600;
--peso-bold: 700;
--peso-extrabold: 800;
```

## 4. Layout e Grid System

### 4.1 Sistema de Grid Responsivo

```css
/* Container Principal */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Breakpoints */
--breakpoint-sm: 640px;   /* Mobile */
--breakpoint-md: 768px;   /* Tablet */
--breakpoint-lg: 1024px;  /* Desktop */
--breakpoint-xl: 1280px;  /* Desktop Large */

/* Grid System */
.grid {
  display: grid;
  gap: 1.5rem;
}

.grid-cols-1 { grid-template-columns: repeat(1, 1fr); }
.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-12 { grid-template-columns: repeat(12, 1fr); }

/* Layout Principal */
.layout-main {
  display: grid;
  grid-template-areas: 
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 280px 1fr;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
```

### 4.2 Espaçamento e Proporções

```css
/* Sistema de Espaçamento */
--espaco-xs: 0.25rem;   /* 4px */
--espaco-sm: 0.5rem;    /* 8px */
--espaco-md: 1rem;      /* 16px */
--espaco-lg: 1.5rem;    /* 24px */
--espaco-xl: 2rem;      /* 32px */
--espaco-2xl: 3rem;     /* 48px */
--espaco-3xl: 4rem;     /* 64px */

/* Proporções Áureas */
--proporcao-quadrada: 1;
--proporcao-video: 1.777; /* 16:9 */
--proporcao-aurea: 1.618;
--proporcao-retrato: 0.75; /* 3:4 */
```

## 5. Componentes da Interface

### 5.1 Header/Navegação

```css
.header {
  background: var(--gradiente-principal);
  color: var(--branco-principal);
  padding: var(--espaco-md) 0;
  box-shadow: 0 2px 10px rgba(45, 90, 39, 0.1);
}

.logo {
  font-family: var(--font-titulos);
  font-size: var(--texto-2xl);
  font-weight: var(--peso-bold);
  color: var(--branco-principal);
}

.nav-menu {
  display: flex;
  gap: var(--espaco-lg);
  align-items: center;
}

.nav-item {
  color: var(--branco-principal);
  text-decoration: none;
  font-weight: var(--peso-medium);
  transition: color 0.3s ease;
}

.nav-item:hover {
  color: var(--verde-accent);
}
```

### 5.2 Área de Chat

```css
.chat-container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 120px);
  background: var(--gradiente-fundo);
}

.messages-area {
  flex: 1;
  overflow-y: auto;
  padding: var(--espaco-lg);
  scroll-behavior: smooth;
}

.message {
  margin-bottom: var(--espaco-lg);
  display: flex;
  align-items: flex-start;
  gap: var(--espaco-md);
}

.message.user {
  flex-direction: row-reverse;
}

.message-bubble {
  max-width: 70%;
  padding: var(--espaco-md) var(--espaco-lg);
  border-radius: 1.5rem;
  font-size: var(--texto-base);
  line-height: 1.5;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.message-bubble.user {
  background: var(--verde-primario);
  color: var(--branco-principal);
  border-bottom-right-radius: 0.5rem;
}

.message-bubble.assistant {
  background: var(--branco-principal);
  color: var(--texto-primario);
  border: 1px solid #E5E7EB;
  border-bottom-left-radius: 0.5rem;
}
```

### 5.3 Input de Mensagem

```css
.input-container {
  padding: var(--espaco-lg);
  background: var(--branco-principal);
  border-top: 1px solid #E5E7EB;
}

.input-wrapper {
  display: flex;
  align-items: flex-end;
  gap: var(--espaco-md);
  max-width: 800px;
  margin: 0 auto;
}

.message-input {
  flex: 1;
  min-height: 44px;
  max-height: 120px;
  padding: var(--espaco-md);
  border: 2px solid #E5E7EB;
  border-radius: 1.5rem;
  font-family: var(--font-principal);
  font-size: var(--texto-base);
  resize: none;
  transition: border-color 0.3s ease;
}

.message-input:focus {
  outline: none;
  border-color: var(--verde-primario);
  box-shadow: 0 0 0 3px rgba(45, 90, 39, 0.1);
}

.send-button {
  width: 44px;
  height: 44px;
  background: var(--verde-primario);
  color: var(--branco-principal);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.send-button:hover {
  background: var(--verde-secundario);
  transform: scale(1.05);
}
```

### 5.4 Sidebar

```css
.sidebar {
  width: 280px;
  background: var(--branco-principal);
  border-right: 1px solid #E5E7EB;
  padding: var(--espaco-lg);
  overflow-y: auto;
}

.sidebar-section {
  margin-bottom: var(--espaco-2xl);
}

.sidebar-title {
  font-family: var(--font-titulos);
  font-size: var(--texto-lg);
  font-weight: var(--peso-semibold);
  color: var(--texto-primario);
  margin-bottom: var(--espaco-md);
}

.conversation-item {
  padding: var(--espaco-md);
  border-radius: 0.75rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-bottom: var(--espaco-sm);
}

.conversation-item:hover {
  background: var(--branco-secundario);
}

.conversation-item.active {
  background: var(--verde-accent);
  color: var(--branco-principal);
}
```

## 6. Animações e Microinterações

### 6.1 Transições Padrão

```css
/* Transições Globais */
* {
  transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
}

/* Animações de Entrada */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Aplicação das Animações */
.message {
  animation: fadeIn 0.5s ease-out;
}

.sidebar {
  animation: slideIn 0.3s ease-out;
}

.typing-indicator {
  animation: pulse 1.5s infinite;
}
```

### 6.2 Estados de Loading

```css
.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid var(--verde-accent);
  border-top: 2px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

## 7. Responsividade

### 7.1 Adaptações Mobile

```css
/* Mobile First Approach */
@media (max-width: 768px) {
  .layout-main {
    grid-template-areas: 
      "header"
      "main"
      "footer";
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    position: fixed;
    top: 0;
    left: -280px;
    height: 100vh;
    z-index: 1000;
    transition: left 0.3s ease;
  }
  
  .sidebar.open {
    left: 0;
  }
  
  .message-bubble {
    max-width: 85%;
  }
  
  .container {
    padding: 0 0.5rem;
  }
}

/* Tablet */
@media (min-width: 769px) and (max-width: 1024px) {
  .layout-main {
    grid-template-columns: 240px 1fr;
  }
  
  .sidebar {
    width: 240px;
  }
}
```

## 8. Acessibilidade

### 8.1 Contraste e Legibilidade

```css
/* Garantir contraste mínimo WCAG AA */
.high-contrast {
  --texto-primario: #000000;
  --verde-primario: #1B4332;
  --verde-secundario: #2D5A27;
}

/* Focus States */
*:focus {
  outline: 2px solid var(--verde-primario);
  outline-offset: 2px;
}

/* Texto alternativo para ícones */
.icon {
  width: 24px;
  height: 24px;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

### 8.2 Navegação por Teclado

```css
/* Skip Links */
.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: var(--verde-primario);
  color: var(--branco-principal);
  padding: 8px;
  text-decoration: none;
  z-index: 1001;
}

.skip-link:focus {
  top: 6px;
}

/* Indicadores de foco melhorados */
.focusable:focus {
  box-shadow: 0 0 0 3px rgba(45, 90, 39, 0.3);
  border-radius: 4px;
}
```

## 9. Dark Mode (Futuro)

### 9.1 Paleta Dark Mode

```css
[data-theme="dark"] {
  --verde-primario: #7FB069;
  --verde-secundario: #4A7C59;
  --verde-accent: #A8D5A8;
  --branco-principal: #1A1A1A;
  --branco-secundario: #2D2D2D;
  --texto-primario: #FFFFFF;
  --texto-secundario: #B0B0B0;
  --texto-terciario: #808080;
}
```

Esta especificação de design visual fornece uma base sólida para a implementação da interface Claudia.AI, garantindo consistência, acessibilidade e uma experiência de usuário excepcional.

