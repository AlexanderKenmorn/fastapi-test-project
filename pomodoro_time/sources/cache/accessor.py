
from redis import Redis


def get_redis_connection() -> Redis:
    """получить соединение с Redis"""
    return Redis(host='localhost', port=6379, db=0, decode_responses=True)


if __name__ == "__main__":
    pass
