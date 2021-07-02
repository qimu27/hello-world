import os
from PIL import Image
photos_name = os.listdir("images")

for i in photos_name: 
    print(i) 
    photo_path = os.path.join('images',i)
    im =Image.open(photo_path)
    im.show()