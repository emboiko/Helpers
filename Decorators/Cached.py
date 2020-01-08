def cached_single_arg(fn):
    """
        Memoizes (caches) a function called with one argument.
        Consider functools.lru_cache() as an alternative.
    """

    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


# @cached_single_arg
# def fib(n):
#     print(f"Calculating fib({n})")
#     return 1 if n < 3 else fib(n-1) + fib(n-2)


# @cached_single_arg
# def fact(n):
#     print(f"Calculating fact({n})")
#     return 1 if n < 2 else n * fact(n-1)


# def main():
#     fib(10)
#     fib(10)
#     fib(11)

#     fact(6)
#     fact(6)
#     fact(7)


# if __name__ == "__main__":
#     main()
