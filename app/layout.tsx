import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Hoje é o Dia",
  description: "Descubra que dia especial é hoje",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
