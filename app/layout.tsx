import type { Metadata, Viewport } from "next"
import { Inter } from "next/font/google"
import "./globals.css"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Solidy - Seguro Auto Inteligente",
  description:
    "Protecao total para seu carro. Seguro auto inteligente, rapido e sem complicacao. Simule em segundos e dirija com tranquilidade.",
  keywords: [
    "seguro auto",
    "seguro carro",
    "cotacao seguro",
    "protecao veicular",
    "assistencia 24h",
  ],
}

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#1a2e1a" },
  ],
  width: "device-width",
  initialScale: 1,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
