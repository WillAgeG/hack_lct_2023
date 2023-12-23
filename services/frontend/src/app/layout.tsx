import type { Metadata } from 'next'
import { Work_Sans } from 'next/font/google'
import Header from '@/components/header'
import { Providers } from './provider'
import './globals.css'

const font = Work_Sans({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Compas',
  description: 'Compas youtube profession',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${font.className} px-[5%] text-[#051531]`}>
        <Providers>
          <Header />
          <main className="flex justify-between items-center h-[88vh] relative">
            {children}
          </main>
        </Providers>
      </body>
    </html>
  )
}
