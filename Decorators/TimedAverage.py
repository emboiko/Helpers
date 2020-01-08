def timed_average(iterations: int):
    """
        Runs a function [iterations] times and returns the result of the last.

        Logs average run time to console.
    """
    def dec(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(iterations):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            average_run_time = total_elapsed / iterations
            print(f"Average run time: {average_run_time:.4f}s over {iterations} iterations.")
            return result
        
        return inner

    return dec


# @timed_average(10)
# def some_func():
#     """
#         Dummy function
#     """
#     for i in range(10_000_000):
#         i * 2


# def main():
#     print(help(timed_average))
#     print(help(some_func))
#     some_func()


# if __name__ == "__main__":
#     main()
