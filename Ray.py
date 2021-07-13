class Ray(object):
    """

    """
    def __init__(self, origin, direction):
        """

        :param origin:
        :param direction:
        """
        self.origin = origin
        self.direction = direction.normalized()

    def __repr__(self):
        """

        :return:
        """
        return 'Ray(%s,%s)' %(repr(self.origin), repr(self.direction))

    def pointAtParameter(self, t):
        """

        :param t:
        :return:
        """
        return self.origin + self.direction.scale(t)