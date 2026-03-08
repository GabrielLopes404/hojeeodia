export default function Home() {
  const hoje = new Date();
  const opcoes: Intl.DateTimeFormatOptions = { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  };
  const dataFormatada = hoje.toLocaleDateString('pt-BR', opcoes);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-8">
      <div className="text-center max-w-2xl">
        <h1 className="text-4xl md:text-6xl font-bold mb-6 text-balance">
          Hoje é o Dia
        </h1>
        <p className="text-xl md:text-2xl text-[var(--muted-foreground)] mb-8 capitalize">
          {dataFormatada}
        </p>
        <div className="bg-[var(--muted)] rounded-[var(--radius)] p-8 border border-[var(--border)]">
          <p className="text-lg">
            Bem-vindo ao Hoje é o Dia! O seu site está funcionando.
          </p>
        </div>
      </div>
    </main>
  );
}
