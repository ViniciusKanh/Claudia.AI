import { useState, useEffect } from 'react'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import Chat from './components/Chat'
import './App.css'

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)
  const [activeConversation, setActiveConversation] = useState(null)
  const [conversations, setConversations] = useState([])
  const [aiStatus, setAiStatus] = useState('demo_mode')
  const [isLoading, setIsLoading] = useState(false)

  // Simula carregamento do status da IA
  useEffect(() => {
    const checkAiStatus = async () => {
      try {
        const response = await fetch('https://nghki1cl50ve.manus.space/api/ai/status')
        if (response.ok) {
          const data = await response.json()
          setAiStatus(data.status)
        }
      } catch (error) {
        console.log('Backend não disponível, usando modo demo')
        setAiStatus('demo_mode')
      }
    }

    checkAiStatus()
    // Verifica status a cada 30 segundos
    const interval = setInterval(checkAiStatus, 30000)
    return () => clearInterval(interval)
  }, [])

  const handleMenuToggle = () => {
    setIsSidebarOpen(!isSidebarOpen)
  }

  const handleNewConversation = () => {
    const newConversation = {
      id: Date.now(),
      title: 'Nova Conversa',
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
      is_archived: false,
      messages: []
    }
    
    setConversations(prev => [newConversation, ...prev])
    setActiveConversation(newConversation)
    setIsSidebarOpen(false) // Fecha sidebar no mobile
  }

  const handleSelectConversation = (conversation) => {
    setActiveConversation(conversation)
    setIsSidebarOpen(false) // Fecha sidebar no mobile
  }

  const handleSendMessage = async (messageContent) => {
    if (!activeConversation) {
      handleNewConversation()
      return
    }

    setIsLoading(true)

    // Adiciona mensagem do usuário
    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: messageContent,
      timestamp: new Date().toISOString()
    }

    // Atualiza conversa ativa
    const updatedConversation = {
      ...activeConversation,
      messages: [...(activeConversation.messages || []), userMessage],
      updated_at: new Date().toISOString()
    }
    
    setActiveConversation(updatedConversation)

    try {
      // Tenta enviar para o backend
      const response = await fetch('https://nghki1cl50ve.manus.space/api/ai/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          conversation_id: activeConversation.id,
          message: messageContent,
          user_id: 1 // Mock user ID
        })
      })

      if (response.ok) {
        const data = await response.json()
        
        // Adiciona resposta da IA
        const aiMessage = {
          id: Date.now() + 1,
          role: 'assistant',
          content: data.ai_response.content,
          timestamp: new Date().toISOString(),
          tokens_used: data.ai_response.tokens_used
        }

        const finalConversation = {
          ...updatedConversation,
          messages: [...updatedConversation.messages, aiMessage]
        }

        setActiveConversation(finalConversation)
      } else {
        throw new Error('Backend não disponível')
      }
    } catch (error) {
      console.log('Usando resposta simulada')
      
      // Simula resposta da IA
      setTimeout(() => {
        const aiMessage = {
          id: Date.now() + 1,
          role: 'assistant',
          content: `Obrigada pela sua mensagem! Você disse: "${messageContent}". Como estou em modo demonstração, esta é uma resposta simulada. Em breve estarei totalmente funcional com o modelo Llama 3.1 70B para oferecer respostas mais inteligentes e personalizadas!`,
          timestamp: new Date().toISOString(),
          tokens_used: 45
        }

        const finalConversation = {
          ...updatedConversation,
          messages: [...updatedConversation.messages, aiMessage]
        }

        setActiveConversation(finalConversation)
        setIsLoading(false)
      }, 2000)
      return
    }

    setIsLoading(false)
  }

  return (
    <div className="h-screen flex flex-col bg-gray-50 font-inter">
      {/* Header */}
      <Header 
        onMenuToggle={handleMenuToggle}
        aiStatus={aiStatus}
      />

      {/* Main Content */}
      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <Sidebar
          isOpen={isSidebarOpen}
          conversations={conversations}
          onNewConversation={handleNewConversation}
          onSelectConversation={handleSelectConversation}
          activeConversationId={activeConversation?.id}
        />

        {/* Chat Area */}
        <main className="flex-1 flex flex-col">
          {activeConversation ? (
            <Chat
              conversation={activeConversation}
              onSendMessage={handleSendMessage}
              isLoading={isLoading}
            />
          ) : (
            <WelcomeScreen 
              onNewConversation={handleNewConversation}
              aiStatus={aiStatus}
            />
          )}
        </main>
      </div>

      {/* Mobile Overlay */}
      {isSidebarOpen && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-30 md:hidden"
          onClick={() => setIsSidebarOpen(false)}
        />
      )}
    </div>
  )
}

// Componente de Boas-vindas
const WelcomeScreen = ({ onNewConversation, aiStatus }) => {
  const suggestions = [
    "Como você pode me ajudar?",
    "Explique como funciona a inteligência artificial",
    "Quais são suas principais funcionalidades?",
    "Como posso usar você para estudar?",
    "Ajude-me a escrever um texto",
    "Tire minhas dúvidas sobre programação"
  ]

  return (
    <div className="flex-1 flex items-center justify-center p-8">
      <div className="max-w-2xl mx-auto text-center">
        {/* Logo e Título */}
        <div className="mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg">
            <span className="text-3xl font-bold text-white">C</span>
          </div>
          <h1 className="text-4xl font-bold text-gray-900 mb-2 font-poppins">
            Bem-vindo à Claudia.AI
          </h1>
          <p className="text-lg text-gray-600">
            Sua assistente de inteligência artificial que cresce com você
          </p>
        </div>

        {/* Status */}
        <div className="mb-8">
          <div className={`inline-flex items-center px-4 py-2 rounded-full text-sm font-medium ${
            aiStatus === 'online' 
              ? 'bg-green-100 text-green-800' 
              : 'bg-blue-100 text-blue-800'
          }`}>
            <div className={`w-2 h-2 rounded-full mr-2 ${
              aiStatus === 'online' ? 'bg-green-500' : 'bg-blue-500'
            }`}></div>
            {aiStatus === 'online' ? 'Sistema Online' : 'Modo Demonstração'}
          </div>
        </div>

        {/* Funcionalidades */}
        <div className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="p-6 bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">🧠</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Inteligente</h3>
            <p className="text-sm text-gray-600">
              Baseada no modelo Llama 3.1 70B para respostas precisas e contextuais
            </p>
          </div>
          
          <div className="p-6 bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">📚</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Aprende</h3>
            <p className="text-sm text-gray-600">
              Sistema de aprendizado contínuo que se adapta ao seu estilo
            </p>
          </div>
          
          <div className="p-6 bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">🌱</span>
            </div>
            <h3 className="font-semibold text-gray-900 mb-2">Sustentável</h3>
            <p className="text-sm text-gray-600">
              Design eco-friendly com foco em eficiência e responsabilidade
            </p>
          </div>
        </div>

        {/* Sugestões */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">
            Experimente perguntar:
          </h3>
          <div className="grid md:grid-cols-2 gap-3">
            {suggestions.map((suggestion, index) => (
              <button
                key={index}
                onClick={() => onNewConversation()}
                className="p-3 text-left bg-white border border-gray-200 rounded-lg hover:border-green-300 hover:bg-green-50 transition-colors text-sm text-gray-700"
              >
                "{suggestion}"
              </button>
            ))}
          </div>
        </div>

        {/* CTA */}
        <button
          onClick={onNewConversation}
          className="claudia-gradient text-white px-8 py-3 rounded-lg font-semibold hover:opacity-90 transition-opacity shadow-lg"
        >
          Começar Nova Conversa
        </button>
      </div>
    </div>
  )
}

export default App
