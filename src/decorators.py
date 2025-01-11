from datetime import datetime
from functools import wraps
from time import time
from typing import Any


def decor_log(filename: str = '') -> Any:
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_ex_time = datetime.now()
            start_time = time()
            log_message = (
                f"----------\nStart of execution: {start_ex_time}\nFunction: {func.__name__} "
                f"| Args: {args} | Kwargs: {kwargs}\n"
            )
            try:
                result = func(*args, **kwargs)
                log_message += f"Status 'OK' | Result: {result}"
                return result
            except Exception as e:
                log_message += f"Status 'ERROR' | {type(e).__name__}: {str(e)}"
            finally:
                end_time = time()
                log_message += f"\nExecution time: {end_time - start_time:.7f}"
                if filename:
                    with open(filename, "w") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator
