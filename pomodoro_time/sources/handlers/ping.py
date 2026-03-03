"""обработчики"""

from pomodoro_time.sources.settings import Settings

from fastapi import APIRouter

router = APIRouter(prefix='/ping', tags=['ping'])

@router.get('/db')
async def ping_db():
    """ping/db"""
    _settings = Settings()
    return {'massage': _settings.sql_db_name}

@router.get('/add')
async def ping_add():
    """ping/add"""
    return {'text': 'приложение работает'}

