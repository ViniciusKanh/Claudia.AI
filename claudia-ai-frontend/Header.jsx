import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Menu, Settings, User, Zap } from 'lucide-react'

const Header = ({ onMenuToggle, aiStatus = 'demo_mode' }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const handleMenuToggle = () => {
    setIsMenuOpen(!isMenuOpen)
    onMenuToggle?.()
  }

  const getStatusBadge = () => {
    switch (aiStatus) {
      case 'online':
        return (
          <Badge variant="default" className="bg-green-500 hover:bg-green-600">
            <Zap className="w-3 h-3 mr-1" />
            Online
          </Badge>
        )
      case 'demo_mode':
        return (
          <Badge variant="secondary" className="bg-blue-100 text-blue-800 hover:bg-blue-200">
            <Zap className="w-3 h-3 mr-1" />
            Demo
          </Badge>
        )
      default:
        return (
          <Badge variant="destructive">
            <Zap className="w-3 h-3 mr-1" />
            Offline
          </Badge>
        )
    }
  }

  return (
    <header className="claudia-gradient text-white shadow-lg">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          {/* Logo e Menu Mobile */}
          <div className="flex items-center space-x-4">
            <Button
              variant="ghost"
              size="sm"
              onClick={handleMenuToggle}
              className="md:hidden text-white hover:bg-white/10"
            >
              <Menu className="w-5 h-5" />
            </Button>
            
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center">
                <span className="text-lg font-bold">C</span>
              </div>
              <div>
                <h1 className="font-poppins text-xl font-bold">Claudia.AI</h1>
                <p className="text-xs text-white/80 hidden sm:block">
                  Inteligência que cresce com você
                </p>
              </div>
            </div>
          </div>

          {/* Status da IA */}
          <div className="flex items-center space-x-4">
            {getStatusBadge()}
            
            {/* Botões de ação */}
            <div className="hidden md:flex items-center space-x-2">
              <Button
                variant="ghost"
                size="sm"
                className="text-white hover:bg-white/10"
              >
                <Settings className="w-4 h-4" />
              </Button>
              <Button
                variant="ghost"
                size="sm"
                className="text-white hover:bg-white/10"
              >
                <User className="w-4 h-4" />
              </Button>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header

