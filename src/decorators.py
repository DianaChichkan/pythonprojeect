from functools import wraps
from typing import Callable, Any
from time import time


def log(filename="mylog.txt") -> Callable:
    """Декоратор для логирования функции, аргументов, результатов и ошибок"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            try:
                if filename is not None:
                    with open(filename, "a") as file:
                         file.write(f"\n{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as error:
                if filename is not None:
                    with open(filename, "a") as file:
                         file.write(f"\n{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")
                raise error
        return wrapper
    return decorator


def printing(func):
    def wrapper(*args, **kwargs) :
          print(f'Function {func} started')
          result = func(*args, **kwargs)
          print(f'Function {func} finished')
          return result
    return wrapper


def timer(func):
   def wrapper(*args, **kwargs):
       time_1 = time()
       result = func(*args, **kwargs)
       time_2 = time()
       print(f'Time for work: {time_2 - time_1}')
       return result
   return wrapper


@printing
@timer
def my_function():
    for i in range (100000000):
        continue

my_function()