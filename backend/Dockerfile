# Dockerfile для backend «Hello World» (FastAPI + uvicorn)
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Открываем порт API
EXPOSE 8000

# Запуск uvicorn без hot-reload (для продакшн-сборки)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]