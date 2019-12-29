from PIL import Image, ImageDraw, ImageFont
import os


def image_loader(path):

    try:
        im = Image.open(path)
        return im
    except FileNotFoundError:
        print("File Path Incorrect!")
        return False


def image_shrinker(image):

    size = image.size
    max_size = max(size)
    shrink_ratio = max_size//100
    if shrink_ratio == 0:
        shrink_ratio = 1
    width = round(size[0]/shrink_ratio)
    height = round(size[1]/shrink_ratio)

    return (width, height)

def gif2frames(img):

    frame = 0
    try:
        while True:
            img.seek(frame)
            yield img.convert("RGBA")
            frame += 1
    except EOFError:
        print("Reach Maximum Frame!")

# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list(r"""8B0$&@R2M9Z6WXNb5#3K4<>*QrSGVAEDwmeansq%1zdIUOgPH7kpoihFfxCLcuJ?Yv=T"+lt/\jy^}{;][()~:-|'`,!._ """)
def get_char(r, g, b, alpha=256):  # RGBA颜色中，最后ALPHA值为透明度，0代表全透明，1表示不透明
	if alpha == 0:  # 若ALPHA为0则为透明，用空白表示
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 根据当前像素的RGB值返回对应的灰度值
	unit = (256.0 + 1)/length  # 将灰度值按比例对应到列表长度(+1的理由没有明白，测试下不加一结果也一样，怀疑是四舍五入之类的)
	return ascii_char[int(gray/unit)]  # 将灰度值按比例对应为灰度列表中的字符


def frame2string(im):
    
    # im = Image.open(image).convert("RGBA")
    txt = ""
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    return txt


def get_txt_size(text, font='square.ttf', fontsize=10):

    im_test = Image.new("RGB", (1,1), (255,255,255))
    dr_test = ImageDraw.Draw(im_test)
    image_font = ImageFont.truetype(os.path.join("fonts", font), fontsize)
    text_size = dr_test.multiline_textsize(text, font=image_font)
    return text_size

def txt2image(text, textsize, font="square.ttf", fontsize=10):
    
    im = Image.new("RGB", textsize, (255, 255, 255))
    dr = ImageDraw.Draw(im)
    image_font = ImageFont.truetype(os.path.join("fonts", font), fontsize)
    dr.text((0,0), text, font=image_font, fill="#000000")
    return im


def images2gif(images_list):

	images_list[0].save('output_gif/output.gif')
	im = Image.open('output_gif/output.gif')
	images = images_list[1:]
	im.save('output_gif/output.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")


def main(image_path):
	
    img = image_loader(image_path)
    if img:
        shrink_size = image_shrinker(img)
        generator = gif2frames(img)
        images_list = []
        for x in generator:
            x = x.resize(shrink_size)
            txt = frame2string(x)
            text_size = get_txt_size(txt)
            image_x = txt2image(txt, text_size)
            images_list.append(image_x)
            print("One Frame Converted!")
        images2gif(images_list)
    else:
        print("Wrong File Path")

if __name__ == "__main__":

    main('cat.gif')
