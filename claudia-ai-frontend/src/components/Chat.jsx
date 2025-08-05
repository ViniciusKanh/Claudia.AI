import { useState, useRef, useEffect } from 'react'
import { Send, Bot, User, ThumbsUp, ThumbsDown, Copy, RotateCcw } from 'lucide-react'
import { ScrollArea } from './ui/scroll-area'
import { Textarea } from './ui/textarea'
import { Badge } from './ui/badge'

const Chat = ({ 
  conversation, 
  messages, 
  onSendMessage, 
  isLoading, 
  aiStatus 
}) => {
  const [inputValue, setInputValue] = useState('')
  const [isTyping, setIsTyping] = useState(false)
  const messagesEndRef = useRef(null)
  const textareaRef = useRef(null)

  // Auto-scroll para a última mensagem
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isLoading])

  // Auto-resize do textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto'
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`
    }
  }, [inputValue])

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!inputValue.trim() || isLoading) return

    const message = inputValue.trim()
    setInputValue('')
    setIsTyping(true)

    try {
      await onSendMessage(message)
    } finally {
      setIsTyping(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text)
    // Aqui você poderia adicionar uma notificação de sucesso
  }

  const formatTime = (dateString) => {
    return new Date(dateString).toLocaleTimeString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  const LoadingIndicator = () => (
    <div className="flex items-center space-x-2 text-gray-500">
      <div className="loading-dots">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <span className="text-sm">Claudia está pensando...</span>
    </div>
  )

  const MessageBubble = ({ message, isUser }) => (
    <div className={`chat-message ${isUser ? 'user' : 'assistant'}`}>
      <div className="flex items-start space-x-3">
        <div className={`
          flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center
          ${isUser ? 'bg-primary-600' : 'bg-gray-100'}
        `}>
          {isUser ? (
            <User className="w-4 h-4 text-white" />
          ) : (
            <Bot className="w-4 h-4 text-primary-600" />
          )}
        </div>
        
        <div className="flex-1 min-w-0">
          <div className="flex items-center space-x-2 mb-1">
            <span className="text-sm font-medium text-gray-900">
              {isUser ? 'Você' : 'Claudia'}
            </span>
            {message.created_at && (
              <span className="text-xs text-gray-500">
                {formatTime(message.created_at)}
              </span>
            )}
            {!isUser && message.metadata?.status === 'demo' && (
              <Badge variant="warning" size="sm">Demo</Badge>
            )}
          </div>
          
          <div className="prose prose-sm max-w-none">
            <p className="text-gray-800 whitespace-pre-wrap leading-relaxed">
              {message.content}
            </p>
          </div>
          
          {!isUser && (
            <div className="flex items-center space-x-2 mt-3">
              <button
                onClick={() => copyToClipboard(message.content)}
                className="p-1 text-gray-400 hover:text-gray-600 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gray-500 rounded"
                title="Copiar mensagem"
              >
                <Copy className="w-4 h-4" />
              </button>
              
              <button
                className="p-1 text-gray-400 hover:text-green-600 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-green-500 rounded"
                title="Gostei"
              >
                <ThumbsUp className="w-4 h-4" />
              </button>
              
              <button
                className="p-1 text-gray-400 hover:text-red-600 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 rounded"
                title="Não gostei"
              >
                <ThumbsDown className="w-4 h-4" />
              </button>
              
              <button
                className="p-1 text-gray-400 hover:text-blue-600 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded"
                title="Regenerar resposta"
              >
                <RotateCcw className="w-4 h-4" />
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  )

  return (
    <div className="flex flex-col h-full bg-gray-50">
      {/* Header da conversa */}
      {conversation && (
        <div className="bg-white border-b border-gray-200 p-4">
          <h2 className="text-lg font-semibold text-gray-900 truncate">
            {conversation.title}
          </h2>
          <p className="text-sm text-gray-500">
            {messages.length} mensagens
          </p>
        </div>
      )}
      
      {/* Área de mensagens */}
      <ScrollArea className="flex-1 p-4">
        <div className="max-w-4xl mx-auto space-y-4">
          {messages.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-64 text-gray-500">
              <Bot className="w-16 h-16 mb-4 text-primary-300" />
              <h3 className="text-xl font-semibold mb-2">Olá! Sou a Claudia</h3>
              <p className="text-center max-w-md">
                Sua assistente de IA inteligente. Como posso ajudá-lo hoje? 
                Faça uma pergunta ou comece uma conversa!
              </p>
              {aiStatus === 'demo' && (
                <Badge variant="warning" className="mt-4">
                  Modo Demonstração Ativo
                </Badge>
              )}
            </div>
          ) : (
            <>
              {messages.map((message) => (
                <MessageBubble
                  key={message.id}
                  message={message}
                  isUser={message.role === 'user'}
                />
              ))}
              
              {(isLoading || isTyping) && (
                <div className="chat-message assistant">
                  <div className="flex items-start space-x-3">
                    <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center">
                      <Bot className="w-4 h-4 text-primary-600" />
                    </div>
                    <div className="flex-1">
                      <LoadingIndicator />
                    </div>
                  </div>
                </div>
              )}
            </>
          )}
          <div ref={messagesEndRef} />
        </div>
      </ScrollArea>
      
      {/* Área de input */}
      <div className="bg-white border-t border-gray-200 p-4">
        <form onSubmit={handleSubmit} className="max-w-4xl mx-auto">
          <div className="flex items-end space-x-3">
            <div className="flex-1">
              <Textarea
                ref={textareaRef}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Digite sua mensagem... (Enter para enviar, Shift+Enter para nova linha)"
                className="min-h-[60px] max-h-32 resize-none"
                disabled={isLoading || aiStatus === 'offline'}
              />
            </div>
            
            <button
              type="submit"
              disabled={!inputValue.trim() || isLoading || aiStatus === 'offline'}
              className="btn-primary p-3 rounded-xl disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
              title="Enviar mensagem"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
          
          {aiStatus === 'offline' && (
            <p className="text-sm text-red-500 mt-2 text-center">
              IA offline. Verifique a conexão com o servidor.
            </p>
          )}
          
          <div className="flex items-center justify-between mt-2 text-xs text-gray-500">
            <span>
              {inputValue.length > 0 && `${inputValue.length} caracteres`}
            </span>
            <span>
              Pressione Enter para enviar
            </span>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Chat

