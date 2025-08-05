import { Plus, MessageSquare, X, Clock, Trash2 } from 'lucide-react'
import { ScrollArea } from './ui/scroll-area'
import { Badge } from './ui/badge'

const Sidebar = ({ 
  isOpen, 
  onClose, 
  conversations, 
  activeConversation, 
  onSelectConversation, 
  onNewConversation,
  onDeleteConversation 
}) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    
    if (diffDays === 1) return 'Hoje'
    if (diffDays === 2) return 'Ontem'
    if (diffDays <= 7) return `${diffDays} dias atrás`
    
    return date.toLocaleDateString('pt-BR', { 
      day: '2-digit', 
      month: '2-digit' 
    })
  }

  const truncateTitle = (title, maxLength = 30) => {
    if (title.length <= maxLength) return title
    return title.substring(0, maxLength) + '...'
  }

  return (
    <>
      {/* Overlay para mobile */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden"
          onClick={onClose}
        />
      )}
      
      {/* Sidebar */}
      <div className={`
        sidebar fixed md:relative inset-y-0 left-0 z-50 w-80 bg-white border-r border-gray-200 
        transform transition-transform duration-300 ease-in-out md:transform-none
        ${isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
      `}>
        <div className="flex flex-col h-full">
          {/* Header da Sidebar */}
          <div className="flex items-center justify-between p-4 border-b border-gray-200 bg-gray-50">
            <h2 className="text-lg font-semibold text-gray-800">Conversas</h2>
            <div className="flex items-center space-x-2">
              <button
                onClick={onNewConversation}
                className="p-2 text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500"
                title="Nova conversa"
              >
                <Plus className="w-5 h-5" />
              </button>
              <button
                onClick={onClose}
                className="p-2 text-gray-500 hover:bg-gray-100 rounded-lg transition-colors duration-200 md:hidden focus:outline-none focus:ring-2 focus:ring-gray-500"
                title="Fechar menu"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
          </div>
          
          {/* Lista de Conversas */}
          <ScrollArea className="flex-1 p-2">
            {conversations.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-32 text-gray-500">
                <MessageSquare className="w-8 h-8 mb-2 opacity-50" />
                <p className="text-sm text-center">
                  Nenhuma conversa ainda.<br />
                  Comece uma nova conversa!
                </p>
              </div>
            ) : (
              <div className="space-y-1">
                {conversations.map((conversation) => (
                  <div
                    key={conversation.id}
                    className={`
                      conversation-item group relative p-3 rounded-lg cursor-pointer 
                      transition-all duration-200 hover:bg-gray-50
                      ${activeConversation?.id === conversation.id 
                        ? 'bg-primary-50 border border-primary-200 shadow-sm' 
                        : 'hover:shadow-sm'
                      }
                    `}
                    onClick={() => onSelectConversation(conversation)}
                  >
                    <div className="flex items-start justify-between">
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center space-x-2 mb-1">
                          <MessageSquare className="w-4 h-4 text-gray-400 flex-shrink-0" />
                          <h3 className="text-sm font-medium text-gray-900 truncate">
                            {truncateTitle(conversation.title)}
                          </h3>
                        </div>
                        
                        <div className="flex items-center space-x-2 text-xs text-gray-500">
                          <Clock className="w-3 h-3" />
                          <span>{formatDate(conversation.updated_at)}</span>
                          {conversation.message_count > 0 && (
                            <Badge variant="secondary" size="sm">
                              {conversation.message_count}
                            </Badge>
                          )}
                        </div>
                      </div>
                      
                      {/* Botão de deletar (aparece no hover) */}
                      {onDeleteConversation && (
                        <button
                          onClick={(e) => {
                            e.stopPropagation()
                            onDeleteConversation(conversation.id)
                          }}
                          className="opacity-0 group-hover:opacity-100 p-1 text-gray-400 hover:text-red-500 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 rounded"
                          title="Deletar conversa"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      )}
                    </div>
                    
                    {/* Indicador de conversa ativa */}
                    {activeConversation?.id === conversation.id && (
                      <div className="absolute left-0 top-1/2 transform -translate-y-1/2 w-1 h-8 bg-primary-500 rounded-r"></div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </ScrollArea>
          
          {/* Footer da Sidebar */}
          <div className="p-4 border-t border-gray-200 bg-gray-50">
            <button
              onClick={onNewConversation}
              className="w-full flex items-center justify-center space-x-2 p-3 bg-primary-600 hover:bg-primary-700 text-white rounded-lg transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
            >
              <Plus className="w-4 h-4" />
              <span className="font-medium">Nova Conversa</span>
            </button>
          </div>
        </div>
      </div>
    </>
  )
}

export default Sidebar

