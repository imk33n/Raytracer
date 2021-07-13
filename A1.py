#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
from PIL import Image
from Plane import *
from Sphere import *
from Triangle import *
from Material import *
from CheckerboardMaterial import *
from Camera import *
import math
from Image import Img

imageWidth = 400
imageHeight = 400
BACKGROUND_COLOR = (255, 0, 0)

def phong(c_a, c_in, ka, kd, ks, n, cos_phi, cos_theta):

    ambient = c_a.scale(ka)
    diffus = c_in.scale(kd*cos_phi)
    specular = c_in.scale(ks * cos_theta**n)
    return ambient + diffus + specular

if __name__=="__main__":
    # create main window
    #im = Image.new("RGB", (imageWidth, imageHeight), (0, 0, 0))
    im = Img(imageWidth, imageHeight)

    fieldofview = 45
    a = fieldofview / 2
    height = 2 * math.tan(a)
    width = imageHeight / imageWidth * height
    pixelWidth = width / (imageWidth - 1)
    pixelHeight = height / (imageHeight - 1)

    c = Vector([0, 3, 0])

    l = Lichtquelle(Vector([30, 30, 10]), Phongfarbe(255, 255, 255))
    material = Phongmaterial(0.7, 0.5, 0.1, 10)

    cam = Camera(Vector([0, 1.8, 10]), Vector([0, 3, 0]), Vector([0, 1, 0]))

    #Objekte
    plane2 = Plane(Vector([0, 0, 0]), Vector([0, 1, 0]), Material(Phongfarbe(192, 192, 192), material))
    plane = Plane(Vector([0, 0, 0]), Vector([0, 1, 0]), CheckerboardMaterial())
    tr1 = Triangle(Vector([0, 4.5, 0]), Vector([-1.25, 2.5, 0]), Vector([1.25, 2.5, 0]), Material(Phongfarbe(255, 255, 0), material))
    sp1 = Sphere(Vector([0, 4.5, 0]), 1, Material(Phongfarbe(255, 0, 0), material))
    sp2 = Sphere(Vector([1.25, 2.5, 0]), 1, Material(Phongfarbe(0, 255, 0), material))
    sp3 = Sphere(Vector([-1.25, 2.5, 0]), 1, Material(Phongfarbe(0, 0, 255), material))

    objectlist = []
    objectlist.append(sp1)
    objectlist.append(sp2)
    objectlist.append(sp3)
    objectlist.append(tr1)
    objectlist.append(plane)

    for x in range(imageWidth):
        for y in range(imageHeight):
            ray = cam.calcRay(x, y, pixelWidth, width, pixelHeight, height)
            maxdist = float('inf')
            color = BACKGROUND_COLOR
            for obj in objectlist:
                #Distanz Auge Objekt -> Strahl
                hitdist = obj.intersectionParameter(ray)
                if hitdist and hitdist >= 0:
                    if hitdist < maxdist:
                        maxdist = hitdist

                        #Schnittpunkt von Strahl und Objekt
                        hitpoint = ray.pointAtParameter(hitdist)
                        #vom Schnittpunkt zum Licht -> Vektor
                        hitToLight = (l.quelle-hitpoint).normalized()
                        #Normale zum Schnittpunkt
                        normal = obj.normalAt(hitpoint)
                        #Sklarprodukt verktor: schnittpunkt zum licht
                        cos_phi = hitToLight.dot(normal)
                        #hitToLight negieren -> formel für spiegelung in die richtige Richtung
                        specular_direction = -hitToLight-2*normal.dot(-hitToLight)*normal
                        cos_theta = specular_direction.dot(- ray.direction)
                        cos_theta = max(0, cos_theta)
                        #Phongformel
                        ph = phong(obj.material.colorAtPoint(hitpoint), l.farbe, obj.material.phongmaterial.a, obj.material.phongmaterial.b, obj.material.phongmaterial.s, obj.material.phongmaterial.n, cos_phi, cos_theta)
                        color = ph

                        #Schattenberechnung
                        for ob in objectlist:
                            if ob != obj:
                                ht = ob.intersectionParameter(Ray(hitpoint, l.quelle-hitpoint))
                                if ht and ht > 0:
                                    color = color.scale(0.5)
                                    break

                        im.draw(x, y, color.tupel())
    #im = im.swap()
    im.show()
    im.save("test.png")





