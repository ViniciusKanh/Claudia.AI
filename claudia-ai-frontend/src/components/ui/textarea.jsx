import { clsx } from 'clsx'
import { forwardRef } from 'react'

const Textarea = forwardRef(({ className, ...props }, ref) => {
  return (
    <textarea
      className={clsx(
        "flex min-h-[80px] w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-sm",
        "placeholder:text-gray-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent",
        "disabled:cursor-not-allowed disabled:opacity-50 resize-none",
        className
      )}
      ref={ref}
      {...props}
    />
  )
})

Textarea.displayName = "Textarea"

export { Textarea }

