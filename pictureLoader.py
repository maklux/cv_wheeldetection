import os

class PictureLoader:
    
    def __init__(self, src):
        self.src = src
        self.pictures_list = []
        
    def load(self):
        os.chdir(self.src)
        for filename in os.listdir('.'):
            self.pictures_list.append({"filename" : filename, "src" : self.src})
        return self.pictures_list    