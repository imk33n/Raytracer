class Material(object):
    """

    """
    def __init__(self, phongfarbe, phongmaterial):
        """

        :param phongfarbe:
        :param phongmaterial:
        """
        self.phongfarbe = phongfarbe
        self.phongmaterial = phongmaterial

    def colorAtPoint(self,p):
        """

        :param p:
        :return:
        """
        return self.phongfarbe

    def getPhongmaterial(self):
        """

        :return:
        """
        return self.phongmaterial
