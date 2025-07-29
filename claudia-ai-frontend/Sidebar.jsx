import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { ScrollArea } from '@/components/ui/scroll-area'
import { 
  Plus, 
  MessageSquare, 
  Archive, 
  Trash2, 
  MoreHorizontal,
  Star,
  Clock
} from 'lucide-react'

const Sidebar = ({ isOpen, conversations = [], onNewConversation, onSelectConversation, activeConversationId }) => {
  const [showArchived, setShowArchived] = useState(false)

  // Mock conversations for demonstration
  const mockConversations = [
    {
      id: 1,
      title: "Como criar uma IA",
      updated_at: "2025-07-28T00:30:00Z",
      message_count: 12,
      is_archived: false
    },
    {
      id: 2,
      title: "Explicação sobre React",
      updated_at: "2025-07-27T15:20:00Z",
      message_count: 8,
      is_archived: false
    },
    {
      id: 3,
      title: "Dicas de programação",
      updated_at: "2025-07-26T10:15:00Z",
      message_count: 15,
      is_archived: false
    },
    {
      id: 4,
      title: "Conversa arquivada",
      updated_at: "2025-07-25T09:00:00Z",
      message_count: 5,
      is_archived: true
    }
  ]

  const displayConversations = conversations.length > 0 ? conversations : mockConversations
  const filteredConversations = displayConversations.filter(conv => 
    showArchived ? conv.is_archived : !conv.is_archived
  )

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    
    if (diffDays === 1) return 'Hoje'
    if (diffDays === 2) return 'Ontem'
    if (diffDays <= 7) return `${diffDays} dias atrás`
    return date.toLocaleDateString('pt-BR')
  }

  const ConversationItem = ({ conversation }) => (
    <div
      className={`group p-3 rounded-lg cursor-pointer transition-all duration-200 hover:bg-gray-50 ${
        activeConversationId === conversation.id ? 'bg-green-50 border-l-4 border-green-500' : ''
      }`}
      onClick={() => onSelectConversation?.(conversation)}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1 min-w-0">
          <h3 className="text-sm font-medium text-gray-900 truncate">
            {conversation.title}
          </h3>
          <div className="flex items-center space-x-2 mt-1">
            <Clock className="w-3 h-3 text-gray-400" />
            <span className="text-xs text-gray-500">
              {formatDate(conversation.updated_at)}
            </span>
            <span className="text-xs text-gray-400">
              • {conversation.message_count} mensagens
            </span>
          </div>
        </div>
        <Button
          variant="ghost"
          size="sm"
          className="opacity-0 group-hover:opacity-100 transition-opacity"
        >
          <MoreHorizontal className="w-4 h-4" />
        </Button>
      </div>
    </div>
  )

  return (
    <aside className={`
      fixed md:relative top-0 left-0 h-full bg-white border-r border-gray-200 transition-transform duration-300 z-40
      ${isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}
      w-80 md:w-80
    `}>
      <div className="flex flex-col h-full">
        {/* Header da Sidebar */}
        <div className="p-4 border-b border-gray-200">
          <Button 
            onClick={onNewConversation}
            className="w-full claudia-gradient text-white hover:opacity-90"
          >
            <Plus className="w-4 h-4 mr-2" />
            Nova Conversa
          </Button>
        </div>

        {/* Filtros */}
        <div className="p-4 border-b border-gray-200">
          <div className="flex space-x-2">
            <Button
              variant={!showArchived ? "default" : "outline"}
              size="sm"
              onClick={() => setShowArchived(false)}
              className="flex-1"
            >
              <MessageSquare className="w-3 h-3 mr-1" />
              Ativas
            </Button>
            <Button
              variant={showArchived ? "default" : "outline"}
              size="sm"
              onClick={() => setShowArchived(true)}
              className="flex-1"
            >
              <Archive className="w-3 h-3 mr-1" />
              Arquivadas
            </Button>
          </div>
        </div>

        {/* Lista de Conversas */}
        <ScrollArea className="flex-1 custom-scrollbar">
          <div className="p-4 space-y-2">
            {filteredConversations.length > 0 ? (
              filteredConversations.map((conversation) => (
                <ConversationItem 
                  key={conversation.id} 
                  conversation={conversation} 
                />
              ))
            ) : (
              <div className="text-center py-8">
                <MessageSquare className="w-12 h-12 text-gray-300 mx-auto mb-3" />
                <p className="text-sm text-gray-500">
                  {showArchived ? 'Nenhuma conversa arquivada' : 'Nenhuma conversa ativa'}
                </p>
                {!showArchived && (
                  <p className="text-xs text-gray-400 mt-1">
                    Clique em "Nova Conversa" para começar
                  </p>
                )}
              </div>
            )}
          </div>
        </ScrollArea>

        {/* Footer da Sidebar */}
        <div className="p-4 border-t border-gray-200">
          <div className="text-xs text-gray-500 text-center">
            <p>Claudia.AI v1.0</p>
            <p className="mt-1">Powered by Llama 3.1 70B</p>
          </div>
        </div>
      </div>
    </aside>
  )
}

export default Sidebar

