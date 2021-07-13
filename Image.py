import PIL
from PIL import Image

class Img(object):
    """

    """
    def __init__(self, width, height, color=(0,0,0)):
        """

        :param width:
        :param height:
        :param color:
        """
        self.width = width
        self.height = height
        self.img =  Image.new("RGB", (self.width, self.height), color)

    def draw(self, x, y, color):
        """

        :param x:
        :param y:
        :param color:
        :return:
        """
        self.img.putpixel((x, y), color)

    def save(self, filename):
        """

        :param filename:
        :return:
        """
        self.img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self.img.save(filename, "PNG")

    def show(self):
        """

        :return:
        """
        self.img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self.img.show()