# Dockerfile для frontend «Hello World» (Next.js 14, standalone)
# ── Стадия 1: сборка ─────────────────────────────────────────────────────────
FROM node:20-alpine AS builder
WORKDIR /app

# Копируем манифесты и устанавливаем зависимости
COPY package.json package-lock.json* ./
RUN npm install

# Копируем исходники и собираем standalone-сборку
COPY . .
RUN npm run build

# ── Стадия 2: рантайм ────────────────────────────────────────────────────────
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000

# standalone-сборка Next.js содержит только нужные файлы
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public

EXPOSE 3000

CMD ["node", "server.js"]