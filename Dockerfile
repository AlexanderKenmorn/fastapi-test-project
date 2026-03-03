FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir uvicorn  # На случай, если нет в requirements.txt

# Копирование кода
COPY . .

# Создание непривилегированного пользователя (безопасность)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# HEALTHCHECK для мониторинга (опционально)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Исправленная команда запуска
CMD ["uvicorn", "pomodoro_time.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
