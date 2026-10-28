import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Hello World — Frontend',
};

export default function Home() {
  return (
    <main
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'linear-gradient(135deg, #10b981, #0f766e)',
        color: '#fff',
      }}
    >
      <h1 style={{ fontSize: '3rem', margin: 0 }}>Hello World from Frontend!</h1>
      <p style={{ fontSize: '1.2rem', opacity: 0.9 }}>
        Next.js «Hello World» успешно запущен в контейнере.
      </p>
    </main>
  );
}