import { clsx } from 'clsx'

const badgeVariants = {
  default: "bg-primary-100 text-primary-800 border-primary-200",
  secondary: "bg-gray-100 text-gray-800 border-gray-200",
  success: "bg-success-100 text-success-800 border-success-200",
  warning: "bg-warning-100 text-warning-800 border-warning-200",
  error: "bg-error-100 text-error-800 border-error-200",
  outline: "text-gray-700 border-gray-300 bg-transparent"
}

const badgeSizes = {
  sm: "px-2 py-0.5 text-xs",
  md: "px-2.5 py-0.5 text-sm",
  lg: "px-3 py-1 text-base"
}

export function Badge({ 
  children, 
  variant = "default", 
  size = "md", 
  className,
  ...props 
}) {
  return (
    <span
      className={clsx(
        "inline-flex items-center font-medium rounded-full border",
        badgeVariants[variant],
        badgeSizes[size],
        className
      )}
      {...props}
    >
      {children}
    </span>
  )
}

