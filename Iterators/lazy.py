from math import pi, factorial


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None


    @property
    def radius(self):
        return self._radius


    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None


    @property
    def area(self):
        if self._area is None:
            self._area = pi * (self.radius ** 2)

        return self._area


class Factorials:
    def __init__(self, length):
        self.length = length
        # We can remove the length and constructor altogether
        # if we wanted to make this an infinite iterator


    def __iter__(self):
        return self.FactIter(self.length)


    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0


        def __iter__(self):
            return self


        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = factorial(self.i)
                self.i += 1
                return result


