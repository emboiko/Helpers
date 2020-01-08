def counted(fn):
    """
        A function counter
    """

    from functools import wraps

    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {fn.__name__} (ID={id(fn)}): called {count} times.")
        return fn(*args, **kwargs)
    
    return inner


# @counted
# def some_func():
#     """
#         A dummy function
#     """

#     print("some_func")


# @counted
# def add(a: int, b: int):
#     """
#         Returns the sum of a & b
#     """

#     return a+b


# @counted
# def add_all(*args: int):
#     """
#         Returns the sum of *args
#     """

#     total = 0
#     for arg in args:
#         total += arg
#     return total


# def main():
#     print(help(counted))
#     print(help(add_all))

#     for i in range(10):
#         add_all(1,2,3,4,5)

#     some_func()

# if __name__ == "__main__":
#     main()
