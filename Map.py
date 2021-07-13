import io
from Triangle import Triangle
from Material import Material
from Phongfarbe import *
from Vector import Vector

class Map(object):
    """

    """
    def __init__(self):
        """

        """
        self.objects = []
        #self.readObjectsFromFile("squirrel.txt")

    def addObject(self, obj):
        """

        :param obj:
        :return:
        """
        self.objects.append(obj)
    def addObjects(self, objs):
        """

        :param objs:
        :return:
        """
        for obj in objs:
            self.objects.append(obj)

    def readObjectsFromFile(self, filename):
        v_list = []

        file = open(filename, "r")
        material = Phongmaterial(0.7, 0.5, 0.1, 10)

        for line in file:
            line = line.strip()
            line = line.split(" ")
            if line[0] == 'v':
                v_list.append(Vector([float(line[1]), float(line[2]), float(line[3])]))
            if line[0] == 'f':
                try:
                    a = v_list[int(line[1])]
                    b = v_list[int(line[2])]
                    c = v_list[int(line[3])]
                    tri = Triangle(a, b, c, Material(Phongfarbe(0, 0, 0), material))
                    self.addObject(tri)
                except:
                    pass

        file.close()