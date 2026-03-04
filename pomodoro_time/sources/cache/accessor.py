"""accessor.py"""

import os
import logging
import redis
from contextlib import contextmanager
from pomodoro_time.sources.settings import Settings

logger = logging.getLogger(__name__)

settings = Settings()
REDIS_URL = settings.redis_url


@contextmanager
def redis_session_maker():
    """Контекстный менеджер для безопасной работы с Redis"""
    client = None
    try:
        client = redis.from_url(
            REDIS_URL,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_keepalive=True,  # 🔥 Поддерживает соединение активным
            health_check_interval=30,  # 🔥 Проверяет "живость" каждые 30 сек
            retry_on_timeout=True,  # 🔥 Автоматический повтор при таймауте
        )
        client.ping()  # Проверяем соединение
        logger.debug("✅ Redis connection established")
        yield client
    except redis.AuthenticationError as e:
        logger.error(f"❌ Redis auth failed: {e}")
        raise
    except redis.ConnectionError as e:
        logger.error(f"❌ Redis connection failed: {e}")
        raise
    except redis.TimeoutError as e:
        logger.error(f"❌ Redis timeout: {e}")
        raise
    finally:
        if client:
            client.close()
            logger.debug("🔌 Redis connection closed")


if __name__ == "__main__":
    pass
