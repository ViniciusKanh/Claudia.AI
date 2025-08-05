import { useState, useEffect } from 'react'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import Chat from './components/Chat'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [conversations, setConversations] = useState([])
  const [activeConversation, setActiveConversation] = useState(null)
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [aiStatus, setAiStatus] = useState('connecting')
  const [currentUser, setCurrentUser] = useState(null)

  // Verificar status da IA e criar usuário padrão
  useEffect(() => {
    checkAIStatus()
    initializeUser()
    loadConversations()
  }, [])

  const checkAIStatus = async () => {
    try {
      const response = await fetch(`${API_URL}/ai/status`)
      if (response.ok) {
        const data = await response.json()
        setAiStatus(data.status === 'online' ? 'online' : 'demo')
      } else {
        setAiStatus('offline')
      }
    } catch (error) {
      console.error('Erro ao verificar status da IA:', error)
      setAiStatus('offline')
    }
  }

  const initializeUser = async () => {
    try {
      // Verificar se já existe um usuário
      const usersResponse = await fetch(`${API_URL}/users`)
      if (usersResponse.ok) {
        const users = await usersResponse.json()
        if (users.length > 0) {
          setCurrentUser(users[0])
          return
        }
      }

      // Criar usuário padrão se não existir
      const response = await fetch(`${API_URL}/users`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: 'usuario_claudia',
          email: 'usuario@claudia.ai',
          preferences: {
            theme: 'green',
            language: 'pt-BR'
          }
        }),
      })

      if (response.ok) {
        const user = await response.json()
        setCurrentUser(user)
      }
    } catch (error) {
      console.error('Erro ao inicializar usuário:', error)
      // Usar usuário mock se falhar
      setCurrentUser({
        id: 1,
        username: 'usuario_claudia',
        email: 'usuario@claudia.ai'
      })
    }
  }

  const loadConversations = async () => {
    try {
      const response = await fetch(`${API_URL}/conversations`)
      if (response.ok) {
        const data = await response.json()
        setConversations(data)
      }
    } catch (error) {
      console.error('Erro ao carregar conversas:', error)
    }
  }

  const loadMessages = async (conversationId) => {
    try {
      const response = await fetch(`${API_URL}/conversations/${conversationId}`)
      if (response.ok) {
        const data = await response.json()
        setMessages(data.messages || [])
      }
    } catch (error) {
      console.error('Erro ao carregar mensagens:', error)
      setMessages([])
    }
  }

  const createNewConversation = async () => {
    if (!currentUser) return

    try {
      const response = await fetch(`${API_URL}/conversations`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: currentUser.id,
          title: 'Nova Conversa',
        }),
      })

      if (response.ok) {
        const newConversation = await response.json()
        setConversations(prev => [newConversation, ...prev])
        setActiveConversation(newConversation)
        setMessages([])
        setSidebarOpen(false)
      }
    } catch (error) {
      console.error('Erro ao criar conversa:', error)
    }
  }

  const selectConversation = async (conversation) => {
    setActiveConversation(conversation)
    await loadMessages(conversation.id)
    setSidebarOpen(false)
  }

  const deleteConversation = async (conversationId) => {
    try {
      const response = await fetch(`${API_URL}/conversations/${conversationId}`, {
        method: 'DELETE',
      })

      if (response.ok) {
        setConversations(prev => prev.filter(conv => conv.id !== conversationId))
        
        if (activeConversation?.id === conversationId) {
          setActiveConversation(null)
          setMessages([])
        }
      }
    } catch (error) {
      console.error('Erro ao deletar conversa:', error)
    }
  }

  const sendMessage = async (messageContent) => {
    if (!activeConversation || !currentUser) {
      // Criar nova conversa se não existir
      await createNewConversation()
      return
    }

    setIsLoading(true)

    try {
      // Adicionar mensagem do usuário localmente
      const userMessage = {
        id: Date.now(),
        role: 'user',
        content: messageContent,
        created_at: new Date().toISOString(),
        conversation_id: activeConversation.id
      }
      setMessages(prev => [...prev, userMessage])

      // Enviar para a API
      const response = await fetch(`${API_URL}/ai/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: messageContent,
          conversation_id: activeConversation.id,
          user_id: currentUser.id,
        }),
      })

      if (response.ok) {
        const data = await response.json()
        
        // Adicionar resposta da IA
        const aiMessage = {
          id: Date.now() + 1,
          role: 'assistant',
          content: data.response,
          created_at: new Date().toISOString(),
          conversation_id: activeConversation.id,
          metadata: {
            model: data.model,
            status: data.status,
            tokens: data.tokens
          }
        }
        setMessages(prev => [...prev, aiMessage])

        // Atualizar título da conversa se for a primeira mensagem
        if (messages.length === 0) {
          const updatedConversation = {
            ...activeConversation,
            title: messageContent.length > 50 
              ? messageContent.substring(0, 50) + '...' 
              : messageContent
          }
          setActiveConversation(updatedConversation)
          setConversations(prev => 
            prev.map(conv => 
              conv.id === activeConversation.id ? updatedConversation : conv
            )
          )
        }
      } else {
        throw new Error('Falha ao enviar mensagem')
      }
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error)
      
      // Adicionar mensagem de erro
      const errorMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: 'Desculpe, ocorreu um erro ao processar sua mensagem. Tente novamente.',
        created_at: new Date().toISOString(),
        conversation_id: activeConversation.id,
        metadata: { status: 'error' }
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <Sidebar
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        conversations={conversations}
        activeConversation={activeConversation}
        onSelectConversation={selectConversation}
        onNewConversation={createNewConversation}
        onDeleteConversation={deleteConversation}
      />

      {/* Main Content */}
      <div className="flex-1 flex flex-col min-w-0">
        <Header
          onToggleSidebar={() => setSidebarOpen(!sidebarOpen)}
          aiStatus={aiStatus}
        />
        
        <main className="flex-1 overflow-hidden">
          <Chat
            conversation={activeConversation}
            messages={messages}
            onSendMessage={sendMessage}
            isLoading={isLoading}
            aiStatus={aiStatus}
          />
        </main>
      </div>
    </div>
  )
}

export default App

