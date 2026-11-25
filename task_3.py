import time
from functools import wraps

import pytest


def retry(max_attempts: int = 3, delay: int | float = 1):
    if max_attempts <= 0 or delay <= 0:
        raise ValueError(
            'Значение "max_attempts" или "delay" не может быть ниже или равен 0'
        )
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


@retry()
def dev(number: int, number_1: int) -> float:
    """Проверка"""
    return number / number_1

assert dev.__name__ == 'dev'
assert dev.__doc__ == 'Проверка'
assert dev(10, 2) == 5


# def test_dev():
#     with pytest.raises(ZeroDivisionError):
#         dev(2, 0)
