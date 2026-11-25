import pytest
import time

from functools import wraps


def retry(max_attempts: int = 3, delay: int = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    else:
                        time.sleep(delay)
        return wrapper
    return decorator


@retry()
def dev(number: int, number_1: int):
    return number / number_1


def test_dev():
    with pytest.raises(ZeroDivisionError):
        dev(2, 0)
