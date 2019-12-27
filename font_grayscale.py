from PIL import Image, ImageDraw, ImageFont
import os
import cv2
import pandas as pd

def txt2image(text, font="square.ttf", fontsize=10):
    im_test = Image.new("RGB", (1,1), (255,255,255))
    dr_test = ImageDraw.Draw(im_test)
    image_font = ImageFont.truetype(os.path.join("fonts", font), fontsize)
    text_size = dr_test.multiline_textsize(text, font=image_font)
    im = Image.new("RGB", text_size, (255,255,255))
    dr = ImageDraw.Draw(im)
    dr.text((0,0), text, font=image_font, fill="#000000")
    return im


def main():

    string_list = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()`~-=_+[]{}\|;":',./<>? """
    grayscale_dic = {}
    for string in string_list:
        string_image = txt2image(string)
        string_image.save(r"font_test/string.jpg")
        grayscale = cv2.imread(r"font_test/string.jpg" , cv2.IMREAD_GRAYSCALE)
        grayscale_dic[string] = sum([sum(x) for x in grayscale])

    df = pd.DataFrame(grayscale_dic, index=['value'])
    df.to_csv('result.csv')



if __name__ == "__main__":
    main()
