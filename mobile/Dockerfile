# Dockerfile для mobile «Hello World» (React Native / Expo)
# Собирает web-версию приложения и раздаёт её статическим сервером.
# Для нативных платформ (iOS/Android) используются Expo Go / EAS Build.
#
# ── Стадия 1: сборка web-экспорта ───────────────────────────────────────────
FROM node:20-alpine AS builder
WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .
RUN npm run build

# ── Стадия 2: статический сервер ────────────────────────────────────────────
FROM nginx:alpine AS runner
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]