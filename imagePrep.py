import cv2
from debugImage import DebugImage

class ImagePrep:

    def __init__(self, filename):
        self.blurLevel = 5
        self.imgPrep = cv2.imread(filename, 0) #load grayscale image
        self.imgOrg = cv2.imread(filename) #load original image


    def blur(self):
        self.imgPrep = cv2.medianBlur(self.imgPrep, self.blurLevel)
        DebugImage(self.imgOrg).show()
        DebugImage(self.imgPrep).show() 

    def gray(self):
        self.imgPrep = cv2.cvtColor(self.imgPrep, cv2.COLOR_GRAY2BGR)

    def findCircle(self, param):
        return cv2.HoughCircles(self.imgPrep, cv2.HOUGH_GRADIENT, param.db, param.minDist, param1=param.param1, param2=param.param2, minRadius=param.minRadius, maxRadius=param.maxRadius)