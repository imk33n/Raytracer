from Ray import *

class Camera(object):
    """

    """
    def __init__(self, e, c, up):
        """

        :param e:
        :param c:
        :param up:
        """
        self.e = e
        self.c = c
        self.up = up
        self.ce = c.__sub__(e)
        self.f = self.ce.__div__(self.ce.magnitude())
        self.fup = self.f.cross(up)
        self.s = self.fup.__div__(self.fup.magnitude())
        self.u = self.s.cross(self.f)

    def calcRay(self, x, y, pixelWidth, width, pixelHeight, height):
        """

        :param x:
        :param y:
        :param pixelWidth:
        :param width:
        :param pixelHeight:
        :param height:
        :return:
        """
        xcomp = self.s.scale(x * pixelWidth - width / 2)
        ycomp = self.u.scale(y * pixelHeight - height / 2)
        ray = Ray(self.e, (self.f + xcomp + ycomp))
        return ray