# Развёртывание

## Локальное окружение (Docker Compose)
```bash
cd lab4/task6
docker compose up --build
```
- Backend: http://localhost:8000 (Swagger UI: `/docs`)
- Frontend: http://localhost:3000
- Mobile (web): http://localhost:8081

Остановка: `docker compose down`

## Облако (Render.com)
Бекенд развёрнут как Web Service на Render.com (Docker-контейнер).
Деплой запускается через GitHub Actions при пуше в `main`.

## SonarQube (локально)
```bash
docker compose -f sonar/sonar.compose.yml up -d   # http://localhost:9000
```