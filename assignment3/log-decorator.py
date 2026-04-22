# Task 1: Writing and Testing a Decorator

import functools
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
if not logger.handlers:
    logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        positional = list(args) if args else "none"
        keyword = dict(kwargs) if kwargs else "none"
        result = func(*args, **kwargs)
        logger.log(
            logging.INFO,
            "function: %s\n"
            "positional parameters: %s\n"
            "keyword parameters: %s\n"
            "return: %s\n"
            % (func.__name__, positional, keyword, repr(result)),
        )
        return result

    return wrapper


@logger_decorator
def hello_world():
    print("Hello, World!")


@logger_decorator
def all_positional_true(*args):
    return True


@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    hello_world()
    all_positional_true(10, 20, 30)
    return_decorator(name="decorator", n=1)
