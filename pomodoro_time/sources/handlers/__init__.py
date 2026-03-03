"""обработчики"""

from .ping import router as ping_router
from .tasks import router as task_router

routers = [ping_router, task_router]

__all__ = ['ping_router', 'task_router']
