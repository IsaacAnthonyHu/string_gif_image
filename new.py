from PIL import Image, ImageDraw, ImageFont
import os

def image_loader(path):

    try:
        im = Image.open(path)
        return im
    except FileNotFoundError:
        print("File Path Incorrect!")
        return False


def gif2frames(img):

    frame = 0
    try:
        while True:
            img.seek(frame)
            yield img.convert("RGBA")
            frame += 1
    except EOFError:
        print("Reach Maximum Frame!")


# got ascii_char sequence from font_grayscale.py

ascii_char = list(r"""8B0$&@R2M9Z6WXNb5#3K4<>*QrSGVAEDwmeansq%1zdIUOgPH7kpoihFfxCLcuJ?Yv=T"+lt/\jy^}{;][()~:-|'`,!._ """)

def get_char(r, g, b, alpha=256):  
        
        # RGBA颜色中，最后ALPHA值为透明度，0代表全透明，1表示不透明
	if alpha == 0:  # 若ALPHA为0则为透明，用空白表示
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  
        # 根据当前像素的RGB值返回对应的灰度值
	unit = (256.0 + 1)/length  
        # 将灰度值按比例对应到列表长度
	return ascii_char[int(gray/unit)]  
        # 将灰度值按比例对应为灰度列表中的字符


def frame2string(img):

    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'
    return txt


def get_string_image_size(text, font='square.ttf', fontsize=10):

    im_test = Image.new("RGB", (1,1), (255,255,255))
    dr_test = ImageDraw.Draw(im_test)
    image_font = ImageFont.truetype(os.path.join("fonts", font), fontsize)
    text_size = dr_test.multiline_textsize(text, font=image_font)
    return text_size, image_font


def txt2image(text, text_size, image_font):

    im = Image.new("RGB", (text_size[0], text_size[1]-1), (255,255,255))
    dr = ImageDraw.Draw(im)
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
        shrink_size = img.size
        generator = gif2frames(img)
        images_list = []
        for x in generator:
            txt = frame2string(x)
            text_size, image_font = get_string_image_size(txt)
            image_x = txt2image(txt, text_size, image_font).resize(shrink_size)
            images_list.append(image_x)
            print("One Frame Converted!")
        images2gif(images_list)
    else:
        print("Wrong File Path!")


if __name__ == '__main__':

    main('cat.gif')
