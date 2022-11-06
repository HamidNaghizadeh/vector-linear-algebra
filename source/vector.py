class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        newCoords = []
        for i in range(0, self.dimension):
            newCoords.append(self.coordinates[i] + v.coordinates[i])
        return Vector(newCoords)

    def __sub__(self, v):
        newCoords = []
        for i in range(0, self.dimension):
            newCoords.append(self.coordinates[i] - v.coordinates[i])
        return Vector(newCoords)

    def times_scalar(self, factor):
        newCoords = []
        for i in range(0, self.dimension):
            newCoords.append(self.coordinates[i] * factor)
        return Vector(newCoords)