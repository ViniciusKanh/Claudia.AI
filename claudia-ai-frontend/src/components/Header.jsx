import { Menu, Bot, Wifi, WifiOff, AlertCircle } from 'lucide-react'
import { Badge } from './ui/badge'

const Header = ({ onToggleSidebar, aiStatus, modelInfo }) => {
  const getStatusInfo = (status) => {
    switch (status) {
      case 'online':
        return {
          icon: <Wifi className="w-3 h-3" />,
          text: 'Online',
          variant: 'success'
        }
      case 'demo_mode':
      case 'demo':
        return {
          icon: <Bot className="w-3 h-3" />,
          text: 'Demo',
          variant: 'warning'
        }
      case 'offline':
        return {
          icon: <WifiOff className="w-3 h-3" />,
          text: 'Offline',
          variant: 'error'
        }
      default:
        return {
          icon: <AlertCircle className="w-3 h-3" />,
          text: 'Conectando...',
          variant: 'secondary'
        }
    }
  }

  const statusInfo = getStatusInfo(aiStatus)

  return (
    <header className="bg-gradient-primary text-white shadow-lg border-b border-primary-700">
      <div className="flex items-center justify-between px-4 py-3">
        <div className="flex items-center space-x-3">
          <button 
            onClick={onToggleSidebar}
            className="p-2 rounded-lg hover:bg-primary-700 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-primary-300"
            aria-label="Abrir menu lateral"
          >
            <Menu className="w-5 h-5" />
          </button>
          
          <div className="flex items-center space-x-3">
            <div className="flex items-center space-x-2">
              <Bot className="w-8 h-8 text-primary-100" />
              <div>
                <h1 className="text-xl font-bold font-display">Claudia.AI</h1>
                <p className="text-xs text-primary-200">Sua assistente inteligente</p>
              </div>
            </div>
          </div>
        </div>
        
        <div className="flex items-center space-x-4">
          <Badge
            variant={statusInfo.variant}
            size="sm"
            className="flex items-center space-x-1 bg-white/10 border-white/20 text-white"
          >
            {statusInfo.icon}
            <span>{statusInfo.text}</span>
          </Badge>

          {modelInfo?.model_name && (
            <Badge
              variant="secondary"
              size="sm"
              className="hidden sm:inline-flex bg-white/10 border-white/20 text-white"
            >
              {modelInfo.model_name}
            </Badge>
          )}

          <div className="hidden md:flex items-center space-x-2 text-sm text-primary-200">
            <span>v1.0.0</span>
          </div>
        </div>
      </div>
      
      {/* Barra de progresso sutil para indicar atividade */}
      {aiStatus === 'connecting' && (
        <div className="h-1 bg-primary-800">
          <div className="h-full bg-primary-300 animate-pulse"></div>
        </div>
      )}
    </header>
  )
}

export default Header

