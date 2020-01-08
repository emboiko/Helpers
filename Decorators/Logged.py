def logged(fn):
    """
        A function logger
    """

    from datetime import datetime
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        run_time = datetime.now()
        result = fn(*args, **kwargs)
        print(f"{run_time}: called {fn.__name__}")
        return result

    return inner


# @logged
# def some_func():
#     pass


# @logged
# def some_other_func():
#     pass


# def main():
#     some_func()
#     some_other_func()


# if __name__ == "__main__":
#     main()
