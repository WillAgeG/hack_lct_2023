# Сервис анализа социальных сетей для профориентации молодежи
## Хакатон «Лидеры цифровой трансформации»

[![Main deploy lct workflow](https://github.com/WillAgeG/hack_lct_2023/actions/workflows/main.yml/badge.svg)](https://github.com/WillAgeG/hack_lct_2023/actions/workflows/main.yml)

### Описание
Вебсайт предназначен для прогнозирования карьеры на основе просмотренных видео на YouTube.

### Микросервисная архитектура

Сервисы:

- **Load Balancer:** Распределяет трафик по сервисам. Используется nginx.
  
- **Accounts:** Отвечает за взаимодействие с пользователями. Используется Django REST Framework (DRF).

- **Frontend:** [Не заполнено]

- **Parser:** Получает данные через YouTube API.

- **Predicter:** Осуществляет прогнозирование профориентации.

### Стек используемых основных технологий

| Программа    | Версия |
|--------------|--------|
| Docker       | [не заполнено] |
| Django       | [не заполнено] |
| FastAPI      | [не заполнено] |
| PostgreSQL   | [не заполнено] |
| Nginx        | [не заполнено] |
| Celery       | [не заполнено] |
| Redis        | [не заполнено] |

### Локальный запуск проекта

1. Создайте файл `.env` и заполните его, исходя из примера из `.env.example`.
2. Запустите Docker Compose:

```
docker-compose -f docker-compose.yml up -d
```
