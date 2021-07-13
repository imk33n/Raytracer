#!/usr/bin/python
# -*- coding: utf-8 -*-
from Vector import *

class Plane(object):
    """

    """
    def __init__(self, point, normal,material):
        """

        :param point:
        :param normal:
        :param material:
        """
        self.point = point
        self.normal = normal.normalized()
        self.material = material

    def __repr__(self):
        """

        :return:
        """
        return 'Plane(%s,%s)' %(repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        """

        :param ray:
        :return:
        """
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)
        if b:
            return -a/b
        else:
            return None


    def normalAt(self,p):
        """

        :param p:
        :return:
        """
        "Normalenvektor"
        return self.normal

    def colorAt(self, hitdist):
        """

        :param hitdist:
        :return:
        """
        return self.phongfarbe
