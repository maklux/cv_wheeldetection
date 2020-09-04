from pictureLoader import PictureLoader
from param import Param
from circle import Circle

pics = PictureLoader('path').load()

counter = 0
for pic in pics:
    counter += 1
    print(pic)
    c = Circle(pic.get('src') +'\\' + pic.get('filename'))
    c.findCircle(Param(), 1)
    if counter == 2:
        break
    
