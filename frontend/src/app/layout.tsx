import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Hello World — Frontend',
  description: 'Демонстрационное приложение «Hello World» для окружения frontend',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ru">
      <body style={{ margin: 0, fontFamily: 'system-ui, sans-serif' }}>{children}</body>
    </html>
  );
}