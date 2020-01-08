def timed(fn):
    """
        A function performance timer
    """

    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        _args = [str(arg) for arg in args]
        _kwargs = [f"{key}={value}" for key, value in kwargs.items()]

        all_args = _args + _kwargs
        args_str = ",".join(all_args)

        print(f"{fn.__name__}({args_str}) took {elapsed:.3f}s")
        return result

    return inner


# @timed
# def wait(duration: float):
#     """
#         Blocks for [duration] seconds
#     """
#     from time import sleep
#     sleep(duration)


# @timed
# def loop_a_lot(iterations: int):
#     """
#         Loops arbitrarily over n iterations
#     """
#     for i in range(iterations):
#         i * 2


# @timed
# def calc_recursive_fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


# @timed
# def fib_recursive(n):
#     return calc_recursive_fib(n)


# def main():
    # print(help(loop_a_lot))
    # loop_a_lot(10_000_000)
    # wait(1)
    # print(calc_recursive_fib(10))
    # print(fib_recursive(10))


# if __name__ == "__main__":
#     main()
