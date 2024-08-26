import os
from datetime import datetime
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

R = TypeVar("R")
P = ParamSpec("P")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[[P.args, P.kwargs], R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = datetime.now()
            func_name = func.__name__
            arg_values = {**dict(zip(func.__code__.co_varnames, args)), **kwargs}

            if filename:
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, "a") as file:
                    file.write(f"{start_time} - Starting execution of '{func_name}' with arguments: {arg_values}\n")
            else:
                print(f"{start_time} - Starting execution of '{func_name}' with arguments: {arg_values}")

            try:
                status_code = "error"
                result = None
                result = func(*args, **kwargs)
                status_code = "ok"

            except Exception as e:
                error_message = f"{start_time} - Error in '{func_name}' with arguments: {arg_values} - \
                Exception: {type(e).__name__}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message)
                else:
                    print(error_message)
                raise
            finally:
                end_time = datetime.now()
                end_message = f"{end_time} - Finished execution of '{func_name}' with status: {status_code}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(end_message)
                else:
                    print(end_message)

            return result

        return wrapper

    return decorator
