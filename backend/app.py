from fastapi import FastAPI

app = FastAPI(
    title="Hello World API",
    description="Демонстрационное приложение «Hello World» для окружения backend",
    version="1.0.0",
)


@app.get("/", tags=["hello"])
def root():
    """Приветствие бэкенда."""
    return {"message": "Hello World from Backend!"}


@app.get("/health", tags=["health"])
def health():
    """Проверка работоспособности сервиса."""
    return {"status": "ok"}