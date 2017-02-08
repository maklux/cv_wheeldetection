from pictureLoader import PictureLoader
from param import Param
from circle import Circle

pics = PictureLoader('C:\\Users\\makayser\\OneDrive\\DSVM\\Projects\\1701 Audi\\CV_WheelStationary\\damage').load()

counter = 0
for pic in pics:
    counter += 1
    print(pic)
    c = Circle(pic.get('src') +'\\' + pic.get('filename'))
    c.findCircle(Param(), 1)
    if counter == 2:
        break
    