from Vector import *
from Phongfarbe import *

class CheckerboardMaterial(object):
    """

    """
    def __init__(self):
        """

        """
        self.baseColor =Phongfarbe(255, 255, 255)
        self.otherColor = Phongfarbe(0, 0, 0)
        self.ambienteCoefficient = 1.0
        self.diffuseCoefficient = 0.6
        self.spectacularCoeffizient = 0.2
        self.checkSize = 1
        self.phongmaterial= Phongmaterial(self.ambienteCoefficient, self.diffuseCoefficient, self.spectacularCoeffizient,2)

    def colorAtPoint(self, p):
        """

        :param p:
        :return:
        """
        v = p
        v.scale(1.0/self.checkSize)
        if(int(abs(v.array[0]) + 0.5) + int(abs(v.array[1])+0.5) + int(abs(v.array[2])+0.5)) %2:
            return self.otherColor
        return self.baseColor

    def getPhongmaterial(self):
        """

        :return:
        """
        return self.phongmaterial()