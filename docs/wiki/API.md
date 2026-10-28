# API

Backend «Hello World» (FastAPI) — `lab4/task6/backend/app.py`.

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/` | Приветствие `Hello World from Backend!` |
| GET | `/health` | Health-check `{"status": "ok"}` |
| GET | `/docs` | Swagger UI |
| GET | `/openapi.json` | OpenAPI-схема (JSON) |

## Генерация Swagger в CI
На этапе сборки CI из приложения извлекается OpenAPI-схема в `swagger.json`:
```bash
python -c "from app import app; open('swagger.json','w').write(app.openapi().to_json())"
```