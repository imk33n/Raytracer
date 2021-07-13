#!/usr/bin/python
# -*- coding: utf-8 -*-

class Phongfarbe(object):
    """

    """
    def __init__(self, rot, gruen, blau):
        """

        :param rot:
        :param gruen:
        :param blau:
        """
        self.rot = rot
        self.gruen = gruen
        self.blau = blau
        self.farbe = (rot, gruen, blau)

    def scale(self, scalar):
        """

        :param scalar:
        :return:
        """
        return Phongfarbe(int(self.rot*scalar), int(self.gruen * scalar), int(self.blau * scalar))

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        return Phongfarbe(self.rot + other.rot, self.gruen + other.gruen, self.blau + other.blau )

    def tupel(self):
        """

        :return:
        """
        return (int(self.rot), int(self.gruen), int(self.blau))

    def __repr__(self):
        """

        :return:
        """
        return 'Color (%s,%s,%s)' %(repr(self.rot), repr(self.gruen), repr(self.blau))

class Phongmaterial(object):
    """

    """

    def __init__(self, a,b,s,n):
        """

        :param a:
        :param b:
        :param s:
        :param n:
        """
        self.a = a
        self.b = b
        self.s = s
        self.n = n

