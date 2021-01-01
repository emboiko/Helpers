from random import randint

class RandomNums:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.accesses = 0


    def __len__(self):
        return self.length


    def __next__(self):
        if self.accesses >= self.length:
            raise StopIteration
        else:
            self.accesses += 1
            return randint(self.range_min, self.range_max)


    def __iter__(self):
        return self


class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length


    def __len__(self):
        return self.length


    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            square = self.i** 2
            self.i += 1
            return square


    def __iter__(self):
        return self
