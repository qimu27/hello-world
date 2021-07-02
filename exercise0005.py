#  你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136*640)的大小。
import os

from PIL import Image

def size_change(filename):
    photos_name = os.listdir(filename)
   
    
    for i in photos_name:
        photo_path = os.path.join('images',i)
        im =Image.open(photo_path)
        w = im.size[0]
        h = im.size[1]

        if w > 1136 or h > 640:
            im.thumbnail((1136,640))
        im.save(i)  
if __name__ == '__main__':
    size_change("images")         