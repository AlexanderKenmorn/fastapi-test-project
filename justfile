# justfile
set shell := ["cmd", "/C"]

help:  # помощь
	@echo Commands:
	@echo   run                    Запустить сервер
	@echo   migrate                Запустить миграцию

run:  # запуск файла main.py
	@echo pomodoro запущен
	@python pomodoro_time/main.py

migrate comment:
    @alembic revision --autogenerate -m "{{comment}}"
    @alembic upgrade head
