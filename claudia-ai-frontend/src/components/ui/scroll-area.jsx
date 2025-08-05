import { clsx } from 'clsx'

export function ScrollArea({ children, className, ...props }) {
  return (
    <div
      className={clsx(
        "scroll-area overflow-y-auto",
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
}

