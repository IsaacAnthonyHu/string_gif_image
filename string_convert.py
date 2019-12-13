from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r, g, b, alpha=256):  # RGBA颜色中，最后ALPHA值为透明度，0代表全透明，1表示不透明
        if alpha == 0:  # 若ALPHA为0则为透明，用空白表示
                return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 根据当前像素的RGB值返回对应的灰度值
        unit = (256.0 + 1)/length  # 将灰度值按比例对应到列表长度(+1的理由没有明白，测试下不加一结果也一样，怀疑是四舍五入之类的)
        return ascii_char[int(gray/unit)]  # 将灰度值按比例对应为灰度列表中的字符
                            

def convert(img):

    im = Image.open(img)
    txt = ""
    width = im.size[0]
    height = im.size[1]
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    with open("string_images/{}.txt".format(x), 'w') as f:
        f.write(txt)
