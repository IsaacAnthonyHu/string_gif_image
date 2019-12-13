from PIL import Image
import os

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r, g, b, alpha=256):  # RGBA颜色中，最后ALPHA值为透明度，0代表全透明，1表示不透明
	if alpha == 0:  # 若ALPHA为0则为透明，用空白表示
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 根据当前像素的RGB值返回对应的灰度值
	unit = (256.0 + 1)/length  # 将灰度值按比例对应到列表长度(+1的理由没有明白，测试下不加一结果也一样，怀疑是四舍五入之类的)
	return ascii_char[int(gray/unit)]  # 将灰度值按比例对应为灰度列表中的字符

def to_string(im, width, height):
    
    # im = Image.open(image).convert("RGBA")
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    return txt

def gif_split(img_name):

    img = Image.open(img_name)
    frame = 0
    try:
        while True:
            img.seek(frame)
            yield (img.convert("RGBA"),img.size[0],img.size[1])
            #yield (img.convert("RGBA"),img.size[0],img.size[1])
            frame += 1
    except EOFError:
        print("Reach Maximum Frame!")

def txt2image(width, height, text):
    
    im = Image.new("RGB", (8*width, 15*height), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join("fonts", "consolas.ttf"), 14)
    dr.text((0,0), text, font=font, fill="#000000")
    return im

def gif_make(*args):