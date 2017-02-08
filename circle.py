from imagePrep import ImagePrep

class Circle:
    def __init__(self, filename):
        self.filename = filename

    def findCircle(self, param, count):
        print(self.filename)
        imgPrep = ImagePrep(self.filename)
        imgPrep.blur()
        imgPrep.findCircle(param)