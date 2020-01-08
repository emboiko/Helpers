from time import perf_counter

class Timer:
    def __init__(self):
        self.elapsed = 0


    def __enter__(self):
        self.start = perf_counter()
        return self


    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False
