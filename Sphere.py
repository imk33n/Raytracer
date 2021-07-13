from Vector import *

class Sphere(object):
    """

    """
    def __init__(self, center, radius, material):
        """

        :param center:
        :param radius:
        :param material:
        """
        self.center = center
        self.radius = radius
        self.material = material

    def __repr__(self):
        """

        :return:
        """
        return 'Sphere(%s,%s)' %(repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        """

        :param ray:
        :return:
        """
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v*v - co.dot(co) + self.radius * self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, p):
        """

        :param p:
        :return:
        """
        return (p-self.center).normalized()

    def color(self, ray, hitdist, l):
        """

        :param ray:
        :param hitdist:
        :param l:
        :return:
        """
        if hitdist:
            hitpoint = ray.pointAtParameter(hitdist)
            n = self.normalAt(hitpoint)

            lichtVekt = l.quelle - hitpoint
            colorAmbiente = self.phongfarbe.scale(self.phongmaterial.a)
            colorDiffus = l.farbe.scale(self.phongmaterial.b).scale(lichtVekt.dot(n))

            lr = lichtVekt.scale(-1)-n.scale(2*n.dot(lichtVekt.scale(-1)))

            colorSpek = l.farbe.scale(self.phongmaterial.s).scale(lr.dot(ray.direction.scale(-1))**self.phongmaterial.n)

            color = colorAmbiente.__add__(colorDiffus).__add__(colorSpek).tupel()

            return color

    def colorAt(self,  hitpoint):
        """

        :param hitpoint:
        :return:
        """
        return self.phongfarbe