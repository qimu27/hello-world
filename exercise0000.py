# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 
from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 选择字体及字体大小
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    
    width, height = img.size
    # 在给定位置绘制一个字符串
    draw.text((width-40, 0), '19', font=myfont, fill="red")
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    # 打开并识别图像
    image = Image.open('header.jpg')
    add_num(image)
    image.show('header.jpg')