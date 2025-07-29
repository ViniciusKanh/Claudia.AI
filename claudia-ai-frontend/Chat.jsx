import { useState, useRef, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { ScrollArea } from '@/components/ui/scroll-area'
import { 
  Send, 
  Mic, 
  Paperclip, 
  MoreVertical,
  ThumbsUp,
  ThumbsDown,
  Copy,
  RefreshCw,
  Bot,
  User
} from 'lucide-react'

const Chat = ({ conversation, onSendMessage, isLoading = false }) => {
  const [message, setMessage] = useState('')
  const [isRecording, setIsRecording] = useState(false)
  const messagesEndRef = useRef(null)
  const textareaRef = useRef(null)

  // Mock messages for demonstration
  const mockMessages = [
    {
      id: 1,
      role: 'assistant',
      content: 'Olá! Sou a Claudia.AI, sua assistente de inteligência artificial. Como posso ajudar você hoje?',
      timestamp: '2025-07-28T00:30:00Z',
      tokens_used: 25
    },
    {
      id: 2,
      role: 'user',
      content: 'Oi Claudia! Pode me explicar como você funciona?',
      timestamp: '2025-07-28T00:31:00Z'
    },
    {
      id: 3,
      role: 'assistant',
      content: 'Claro! Eu sou baseada no modelo Llama 3.1 70B e funciono através de processamento de linguagem natural. Posso ajudar com uma ampla variedade de tarefas como responder perguntas, explicar conceitos, ajudar com programação, escrever textos e muito mais. O que torna nossa conversa especial é que eu aprendo com nossos diálogos para oferecer respostas cada vez mais personalizadas para você!',
      timestamp: '2025-07-28T00:31:30Z',
      tokens_used: 89
    }
  ]

  const messages = conversation?.messages || mockMessages

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSendMessage = () => {
    if (message.trim() && !isLoading) {
      onSendMessage?.(message.trim())
      setMessage('')
      // Auto-resize textarea
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto'
      }
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  const handleTextareaChange = (e) => {
    setMessage(e.target.value)
    // Auto-resize
    const textarea = e.target
    textarea.style.height = 'auto'
    textarea.style.height = Math.min(textarea.scrollHeight, 120) + 'px'
  }

  const formatTime = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  const MessageBubble = ({ message: msg, isLast }) => {
    const isUser = msg.role === 'user'
    
    return (
      <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4 fade-in`}>
        <div className={`flex max-w-[80%] ${isUser ? 'flex-row-reverse' : 'flex-row'} items-start space-x-3`}>
          {/* Avatar */}
          <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
            isUser ? 'bg-green-500 ml-3' : 'bg-gray-100 mr-3'
          }`}>
            {isUser ? (
              <User className="w-4 h-4 text-white" />
            ) : (
              <Bot className="w-4 h-4 text-green-600" />
            )}
          </div>
          
          {/* Message Content */}
          <div className={`${isUser ? 'message-bubble-user' : 'message-bubble-assistant'} p-4 shadow-sm`}>
            <p className="text-sm leading-relaxed whitespace-pre-wrap">
              {msg.content}
            </p>
            
            {/* Message Footer */}
            <div className={`flex items-center justify-between mt-2 pt-2 border-t ${
              isUser ? 'border-white/20' : 'border-gray-100'
            }`}>
              <span className={`text-xs ${isUser ? 'text-white/70' : 'text-gray-500'}`}>
                {formatTime(msg.timestamp)}
                {msg.tokens_used && (
                  <span className="ml-2">• {msg.tokens_used} tokens</span>
                )}
              </span>
              
              {!isUser && (
                <div className="flex items-center space-x-1">
                  <Button variant="ghost" size="sm" className="h-6 w-6 p-0">
                    <Copy className="w-3 h-3" />
                  </Button>
                  <Button variant="ghost" size="sm" className="h-6 w-6 p-0">
                    <ThumbsUp className="w-3 h-3" />
                  </Button>
                  <Button variant="ghost" size="sm" className="h-6 w-6 p-0">
                    <ThumbsDown className="w-3 h-3" />
                  </Button>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    )
  }

  const TypingIndicator = () => (
    <div className="flex justify-start mb-4">
      <div className="flex items-start space-x-3">
        <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center">
          <Bot className="w-4 h-4 text-green-600" />
        </div>
        <div className="message-bubble-assistant p-4">
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-gray-400 rounded-full typing-indicator"></div>
            <div className="w-2 h-2 bg-gray-400 rounded-full typing-indicator" style={{animationDelay: '0.2s'}}></div>
            <div className="w-2 h-2 bg-gray-400 rounded-full typing-indicator" style={{animationDelay: '0.4s'}}></div>
            <span className="text-sm text-gray-500 ml-2">Claudia está digitando...</span>
          </div>
        </div>
      </div>
    </div>
  )

  return (
    <div className="flex flex-col h-full bg-white">
      {/* Chat Header */}
      <div className="flex items-center justify-between p-4 border-b border-gray-200 bg-white">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
            <Bot className="w-5 h-5 text-green-600" />
          </div>
          <div>
            <h2 className="font-semibold text-gray-900">
              {conversation?.title || 'Nova Conversa'}
            </h2>
            <p className="text-sm text-gray-500">
              {isLoading ? 'Respondendo...' : 'Online • Responde em segundos'}
            </p>
          </div>
        </div>
        
        <div className="flex items-center space-x-2">
          <Button variant="ghost" size="sm">
            <RefreshCw className="w-4 h-4" />
          </Button>
          <Button variant="ghost" size="sm">
            <MoreVertical className="w-4 h-4" />
          </Button>
        </div>
      </div>

      {/* Messages Area */}
      <ScrollArea className="flex-1 custom-scrollbar">
        <div className="p-4 space-y-4">
          {messages.map((msg, index) => (
            <MessageBubble 
              key={msg.id} 
              message={msg} 
              isLast={index === messages.length - 1}
            />
          ))}
          
          {isLoading && <TypingIndicator />}
          
          <div ref={messagesEndRef} />
        </div>
      </ScrollArea>

      {/* Input Area */}
      <div className="p-4 border-t border-gray-200 bg-white">
        <div className="flex items-end space-x-3">
          {/* Attachment Button */}
          <Button variant="ghost" size="sm" className="flex-shrink-0">
            <Paperclip className="w-4 h-4" />
          </Button>
          
          {/* Message Input */}
          <div className="flex-1 relative">
            <Textarea
              ref={textareaRef}
              value={message}
              onChange={handleTextareaChange}
              onKeyPress={handleKeyPress}
              placeholder="Digite sua mensagem para Claudia..."
              className="chat-input resize-none min-h-[44px] max-h-[120px] pr-12"
              disabled={isLoading}
            />
            
            {/* Voice Recording Button */}
            <Button
              variant="ghost"
              size="sm"
              className={`absolute right-2 top-2 ${isRecording ? 'text-red-500' : 'text-gray-400'}`}
              onClick={() => setIsRecording(!isRecording)}
            >
              <Mic className="w-4 h-4" />
            </Button>
          </div>
          
          {/* Send Button */}
          <Button
            onClick={handleSendMessage}
            disabled={!message.trim() || isLoading}
            className="send-button flex-shrink-0 w-11 h-11"
          >
            <Send className="w-4 h-4" />
          </Button>
        </div>
        
        {/* Input Footer */}
        <div className="flex items-center justify-between mt-2 text-xs text-gray-500">
          <span>
            Pressione Enter para enviar, Shift+Enter para nova linha
          </span>
          <span>
            {message.length}/2000
          </span>
        </div>
      </div>
    </div>
  )
}

export default Chat

