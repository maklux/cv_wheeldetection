import cv2

class DebugImage:
    def __init__(self, image):
        self.img = image

    def show(self):
        cv2.imshow('circle', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()