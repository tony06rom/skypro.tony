from datetime import datetime
from functools import wraps
from pathlib import Path
from time import time
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
WRAPS_DIR = ROOT_DIR / "wraps"


def decor_log(filename: Any = "") -> Any:
    """Логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

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
                    with open(f"{WRAPS_DIR}\\{filename}", "w", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator
