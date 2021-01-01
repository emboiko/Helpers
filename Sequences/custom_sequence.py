from numbers import Real


class Point:
    def __init__(self,x, y):
        if isinstance(x, Real) and isinstance(y, Real):
            self._point = (x,y)
        else:
            raise TypeError("Coordinates must be real numbers")


    def __repr__(self):
        return f"Point(x={self._point[0]}, y={self._point[1]})"


    def __len__(self):
        return len(self._point)


    def __getitem__(self, item):
        return self._point[item]


class Polygon:
    def __init__(self, *points):
        if points:
            self._points = [Point(*point) for point in points]
        else:
            self._points = []


    def __repr__(self):
        str = ", ".join([str(point) for point in self._points])
        return f"Polygon({str})"


    def __len__(self):
        return len(self._points)


    def __getitem__(self, val):
        # sequence[x] or sequence[x:y:z]
        return self._points[val]


    def __setitem__(self, index, val):
        # sequence[x] = y or sequence[x:y:z] = n
        try:
            rhs = [Point(*point) for point in val]
            single = False
        except TypeError:
            try:
                rhs = Point(*val)
                single = True
            except TypeError:
                raise TypeError("Invalid Point or iterable")
        
        if (isinstance(index, int) and single) \
            or (isinstance(index,slice) and not single):

            self._points[index] = rhs

        else:
            raise TypeError("Incompatible index or slice")



    def __add__(self, other):
        # A new object of the same type
        if isinstance(other, Polygon):
            new_points = self._points + other._points
            return Polygon(*new_points)
        else:
            raise TypeError("Can only concatenate to another Polygon")


    def __iadd__(self, other):
        # The original object memory reference
        self.extend(other)
        return self


    def __contains__(self, val):
        # support for "in"
        pass


    def __delitem__(self, index):
        # support for "del"
        del self._points[index]


    #Then these methods are just implemented accordingly:

    def append(self, point):
        self._points.append(Point(*point))


    def insert(self, index, point):
        self._points.insert(index, Point(*point))


    def extend(self, points):
        if isinstance(points, Polygon):
            self._points += points._points
        else:
            points = [Point(*point) for point in points]
            self._points += points


    def pop(self, index):
        return self._points.pop(index)


    def clear(self):
        self._points.clear()
