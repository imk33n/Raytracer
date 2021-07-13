import math
from copy import deepcopy

class Vector(object):
    """

    """
    def __init__(self, array):
        """

        :param array:
        """
        if len(array) < 1 or not type(array) == list:
            raise AttributeError("Vektor braucht mind. 1 Parameter (als Liste)")
        self.array = deepcopy([float(x) for x in array])
        self.dimensions = len(self.array)


    def magnitude(self):
        """

        :return:
        """
        quadsum = 0.0
        for x in self.array:
            quadsum += x**2
        return math.sqrt(quadsum)


    def normalize(self):
        """

        :return:
        """
        quadsum = 0.0
        mag = self.magnitude()
        self.array = [x/mag for x in self.array] if mag != 0 else [0.0, 0.0, 0.0]


    def normalized(self):
        """

        :return:
        """
        v = Vector(self.array)
        v.normalize()
        return v


    def scale(self, t):
        """

        :param t:
        :return:
        """
        return Vector([x * t for x in self.array])

    def scaled(self, t):
        """

        :param t:
        :return:
        """
        v = Vector(self.array)
        v.scale(t)
        return v


    def dot(self, other):
        """

        :param other:
        :return:
        """

        "Skalarprodukt"
        # erstmal nur fuer 3 dimensionen
        if isinstance(other,Vector):
            return self.array[0]*other.array[0] + self.array[1]*other.array[1] + self.array[2]*other.array[2]
        else:
            raise TypeError("Kein Vektor")

    def cross(self, other):
        """

        :param other:
        :return:
        """
        return Vector([self.array[1] * other.array[2] - self.array[2] * other.array[1],
                       self.array[2] * other.array[0] - self.array[0] * other.array[2],
                       self.array[0] * other.array[1] - self.array[1] * other.array[0]])

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        if self.dimensions != other.dimensions:
            raise ArithmeticError("Vektoren mÃ¼ssen die gleiche Anzahl Dimensionen haben")
        a = []
        for i in range(len(self.array)):
            a.append(self.array[i] + other.array[i])

        return Vector(a)

    def __sub__(self, other):
        """

        :param other:
        :return:
        """
        if self.dimensions != other.dimensions:
            raise ArithmeticError("Vektoren mÃ¼ssen die gleiche Anzahl Dimensionen haben")
        a = []
        for i in range(len(self.array)):
            a.append(self.array[i] - other.array[i])
        return Vector(a)

    def __div__(self, other):
        """

        :param other:
        :return:
        """
        if type(other) != float:
            raise TypeError("Divisor muss float sein")
        return Vector([x/other for x in self.array])

    __truediv__ = __div__

    def __mul__(self, other):
        """

        :param other:
        :return:
        """
        return Vector([x*other for x in self.array])

    __rmul__ =__mul__

    def __neg__(self):
        """

        :return:
        """
        return self.scale(-1)

    def __repr__(self):
        """

        :return:
        """
        return "Vector(%s)" % ", ".join([str(x) for x in self.array])

