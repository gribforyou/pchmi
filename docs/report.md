# Отчёт по заданию 6

**Проект:** AI_Calendar_App — веб-приложение «Умный Календарь»
**Задание:** 6. Спроектировать инфраструктуру проекта и развернуть её
**Исполнитель:** Шибитов Николай, группа 11, курс 3
**Раздел:** `lab4/task6`

---

## Выполненные пункты

### п. 1. Изучение статей по построению окружения разработки
Изучены статьи по развёртыванию окружения разработки:
- https://habr.com/ru/company/southbridge/blog/329262/
- https://selectel.ru/blog/tutorials/develop-canban-board-on-django-drf-alpine-js/

На их основе приняты решения: разделение backend/frontend, контейнеризация
через Docker, автоматизация сборки через CI/CD.

### п. 2. Структура проекта и ветки
Создана структура проекта для бекенд и веб-версий. В git-репозитории созданы
ветки:
- `main` — production (релизная версия);
- `develop` — development (тестовая версия).

Согласованы правила работы с ветками (запрет прямых пушей, работа через
Pull Request, Conventional Commits). Разработка ведётся только через систему
контроля версий git. Подробности — в README (раздел 2).

### п. 3. Управление проектом (GitHub Projects)
Управление задачами ведётся в GitHub Projects. Созданы проекты:
- «Дизайн и проектирование приложений» — документация и отчёты;
- «Разработка API и бизнес-логики» — задачи бекенда;
- «Разработка веб-приложения» — задачи фронтенда;
- «Разработка мобильного приложения» — задачи мобильной версии.

Коммуникация — в Slack/Telegram. Статусы: `Todo → In Progress → In Review → Done`.

### п. 4. План работ по бекенду
На основе ТЗ составлен план работ по бекенду (разработка API, бизнес-логика,
качество, CI/CD), задачи распределены между участниками команды.
Полный план — в `docs/backend_plan.md`, задачи — в GitHub Projects.

### п. 5. Документирование проекта
Проект задокументирован в README, GitHub Wiki и GitHub Pages (см. `docs/`).
Описаны архитектура, API, развёртывание, инструкции.

### п. 6. Автоматические тесты
Добавлены автоматические тесты бекенда (`backend/test_app.py`, pytest).
В CI тесты (`test-backend`, `test-frontend`) выполняются **до** сборки;
сборка формируется только после прохождения тестов.

### п. 7. Инфраструктура Docker (PlantUML)
Спроектирована контейнерная инфраструктура бекенда и веб-приложения в
PlantUML (`diagrams/`): контекстная, контейнерная и deployment-диаграммы.
Диаграммы уточняют схемы лабораторной работы 3.

### п. 8. Развёртывание через Docker Compose
Инфраструктура бекенда и веб-приложения развёрнута на основе контейнеров.
Конфигурация — в `Dockerfile`, запуск — через `docker compose up --build`.

### п. 9. Приложение «Hello World»
Добавлены приложения «Hello World» для иллюстрации работоспособности
каждого окружения:
- Backend (`GET /` → `Hello World from Backend!`, `/health`, `/docs`);
- Frontend (страница `Hello World from Frontend!`);
- Mobile (экран `Hello World from Mobile!`, React Native/Expo).

### п. 10. Непрерывная интеграция (GitHub Actions)
Настроен GitHub Actions (`ci.yml`) для автоматизации сборки проекта со
сборкой docker-контейнеров (docker/build-push-action).

### п. 11. Swagger в CI/CD
В CI/CD встроена генерация файлов Swagger (OpenAPI) этапом сборки:
из FastAPI-приложения извлекается `swagger.json`.

### п. 12. SonarQube
Настроен SonarQube: локальная версия через Docker (`sonar/sonar.compose.yml`)
для бекенда и веб-приложения, облачная версия подключена как этап CI/CD.
Изучены статьи по SonarQube.

### п. 13. Развёртывание на облачной платформе
Бекенд развёрнут из контейнеров Docker после тестов и проверки качества кода
на бесплатной платформе Render.com. Фронтенд — локально/на другой учётной
записи. Настроен деплой через `render-action`.

### п. 14. Отчёт
Сформирован настоящий отчёт, описывающий работы по всем пунктам задания.

### п. 15. Мобильное приложение
Добавлена заготовка мобильного приложения «Hello World» (React Native/Expo)
в `mobile/`, с Dockerfile, docker-compose-сервисом и CI-джобами.

---

## Распределение работ в проекте

| Участник | Роль | Задачи |
|----------|------|--------|
| Шибитов Николай | Backend / DevOps | API, БД, Docker, CI/CD, тесты, SonarQube, деплой |
| (командная работа) | Frontend | веб-интерфейс, Next.js |
| (командная работа) | Mobile | мобильная версия, React Native/Expo |

## Информация по коммитам

Ниже приведены основные коммиты раздела `lab4/task6` (полный список — в
`git log` репозитория):

| Дата | Коммит | Содержание |
|------|--------|-----------|
| 2026-10-28 | `task6: hello-world backend (FastAPI)` | backend/app.py, test_app.py, Dockerfile |
| 2026-10-28 | `task6: hello-world frontend (Next.js)` | frontend, Dockerfile (multi-stage) |
| 2026-10-28 | `task6: docker-compose и окружение` | docker-compose.yml |
| 2026-10-28 | `task6: PlantUML-диаграммы инфраструктуры` | diagrams/ |
| 2026-10-28 | `task6: CI/CD GitHub Actions` | .github/workflows/ci.yml |
| 2026-10-28 | `task6: SonarQube конфигурация` | sonar/ |
| 2026-10-28 | `task6: документация и отчёт` | README.md, docs/ |

> Фактический список коммитов уточняется по мере их создания в репозитории.

---

## Демонстрация

1. **Запуск локального окружения:**
   ```bash
   cd lab4/task6
   docker compose up --build
   ```
   - Backend: http://localhost:8000 (`Hello World from Backend!`, Swagger `/docs`)
   - Frontend: http://localhost:3000 (`Hello World from Frontend!`)

2. **Запуск тестов:**
   ```bash
   cd lab4/task6/backend
   pip install -r requirements.txt && pytest -v
   ```

3. **SonarQube (локально):**
   ```bash
   docker compose -f sonar/sonar.compose.yml up -d   # http://localhost:9000
   ```

4. **CI/CD (GitHub Actions):** при пуше в `develop`/`main` запускается
   pipeline «тесты → качество → сборка+Swagger → деплой».