# Архитектура и инфраструктура

## Стек
- **Backend:** Python 3.12, FastAPI, uvicorn, pytest.
- **Frontend:** Next.js 14, React 18, TypeScript.
- **Mobile:** React Native 0.74 + Expo 51.
- **БД:** PostgreSQL 16.
- **Контейнеризация:** Docker + Docker Compose.
- **CI/CD:** GitHub Actions.
- **Качество кода:** SonarQube.

## Инфраструктура Docker
Контейнеры `backend` (FastAPI, порт 8000), `frontend` (Next.js, порт 3000)
и `mobile` (React Native/Expo web, порт 8081) собираются из
соответствующих `Dockerfile` и запускаются через `docker compose up --build`.

Схемы PlantUML — в каталоге `lab4/task6/diagrams/`.

## Ветки
- `main` — production
- `develop` — development