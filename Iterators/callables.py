def counter():
    i = 0


    def inc():
        nonlocal i
        i += 1
        return i

    return inc


class CallableIter:
    def __init__(self, callable, stop):
        self.callable = callable
        self.stop = stop
        self.consumed = False
    

    def __iter__(self):
        return self


    def __next__(self):
        if self.consumed:
            raise StopIteration
        else:
            result = self.callable()
            if result == self.stop:
                self.consumed = True
                raise StopIteration
            else:
                return result

