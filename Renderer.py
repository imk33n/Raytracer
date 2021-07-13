import math

import PIL

import Image
from Plane import Plane
from Vector import Vector
from Sphere import Sphere
from Material import Material
from Phongfarbe import *
from Camera import Camera
from CheckerboardMaterial import CheckerboardMaterial
from Triangle import Triangle
from Map import Map
from Lichtquelle import Lichtquelle
from Image import Img
from Ray import Ray
import time
import threading

class Renderer(object):
    """

    """
    def __init__(self, fieldofview, imageWidth, imageHeight, lichtquelle, map, cam, background_color=(255,0,0)):
        """

        :param fieldofview:
        :param imageWidth:
        :param imageHeight:
        :param lichtquelle:
        :param map:
        :param cam:
        :param background_color:
        """
        self.BACKGROUND_COLOR = background_color
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.fieldofview = fieldofview
        self.a = self.fieldofview / 2
        self.height = 2 * math.tan(self.a)
        self.width = self.imageHeight / self.imageWidth * self.height
        self.pixelWidth = self.width / (self.imageWidth - 1)
        self.pixelHeight = self.height / (self.imageHeight - 1)

        self.im = Img(self.imageWidth, self.imageHeight)

        self.lichtquelle = lichtquelle
        self.map = map
        self.cam = cam

    def phong(self, c_a, c_in, ka, kd, ks, n, cos_phi, cos_theta):
        """

        :param c_a:
        :param c_in:
        :param ka:
        :param kd:
        :param ks:
        :param n:
        :param cos_phi:
        :param cos_theta:
        :return:
        """
        ambient = c_a.scale(ka)
        diffus = c_in.scale(kd * cos_phi)
        specular = c_in.scale(ks * cos_theta ** n)
        return ambient + diffus + specular

    def renderSingleThreaded(self):
        """

        :return:
        """
        start_time = time.time()

        for x in range(self.imageWidth):
            for y in range(self.imageHeight):
                ray = self.cam.calcRay(x, y, self.pixelWidth, self.width, self.pixelHeight, self.height)
                maxdist = float('inf')
                color = self.BACKGROUND_COLOR
                for obj in self.map.objects:
                    # Distanz Auge Objekt -> Strahl
                    hitdist = obj.intersectionParameter(ray)
                    if hitdist and hitdist >= 0:
                        if hitdist < maxdist:
                            maxdist = hitdist

                            # Schnittpunkt von Strahl und Objekt
                            hitpoint = ray.pointAtParameter(hitdist)
                            # vom Schnittpunkt zum Licht -> Vektor
                            hitToLight = (self.lichtquelle.quelle - hitpoint).normalized()
                            # Normale zum Schnittpunkt
                            normal = obj.normalAt(hitpoint)
                            # Sklarprodukt verktor: schnittpunkt zum licht
                            cos_phi = hitToLight.dot(normal)
                            specular_direction = -hitToLight - 2 * normal.dot(-hitToLight) * normal
                            cos_theta = specular_direction.dot(- ray.direction)
                            cos_theta = max(0, cos_theta)
                            # Phongformel
                            ph = self.phong(obj.material.colorAtPoint(hitpoint), self.lichtquelle.farbe, obj.material.phongmaterial.a, obj.material.phongmaterial.b, obj.material.phongmaterial.s,obj.material.phongmaterial.n, cos_phi, cos_theta)

                            color = ph

                            # Schattenberechnung
                            for ob in map.objects:
                                if ob != obj:
                                    ht = ob.intersectionParameter(Ray(hitpoint, self.lichtquelle.quelle - hitpoint))
                                    if ht and ht > 0:
                                        color = color.scale(0.5)
                                        break

                            self.im.draw(x, y, color.tupel())

        end_time = time.time()
        self.im.show()
        self.im.save("test.png")
        print("Rendering (Single Threaded) took " + str(end_time - start_time))

    def renderMultiThreaded(self):
        """

        :return:
        """

    def renderMultiprocessed(self):
        """

        :return:
        """

map = Map()
cam = Camera(Vector([0, 1.8, 10]), Vector([0, 3, 0]), Vector([0, 1, 0]))
lichtquelle = Lichtquelle(Vector([30, 30, 10]), Phongfarbe(255, 255, 255))

#kugeln und dreieck sowie die ebenen
material = Phongmaterial(0.7, 0.5, 0.1, 10)
plane2 = Plane(Vector([0, 0, 0]), Vector([0, 1, 0]), Material(Phongfarbe(192, 192, 192), material))
plane = Plane(Vector([0, 0, 0]), Vector([0, 1, 0]), CheckerboardMaterial())
tr1 = Triangle(Vector([0, 4.5, 0]), Vector([-1.25, 2.5, 0]), Vector([1.25, 2.5, 0]), Material(Phongfarbe(255, 255, 0), material)) #schachbrett
sp1 = Sphere(Vector([0, 4.5, 0]), 1, Material(Phongfarbe(255, 0, 0), material))
sp2 = Sphere(Vector([1.25, 2.5, 0]), 1, Material(Phongfarbe(0, 255, 0), material))
sp3 = Sphere(Vector([-1.25, 2.5, 0]), 1, Material(Phongfarbe(0, 0, 255), material))
map.addObjects([sp1, sp2, sp3, tr1, plane])

#squirrel einlesen
map.readObjectsFromFile("squirrel.txt")

renderer = Renderer(45, 50, 50, lichtquelle, map, cam, (255,192,203))
renderer.renderSingleThreaded()
