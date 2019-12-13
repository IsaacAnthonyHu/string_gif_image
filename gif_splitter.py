import PIL.Image as Image
import os

def gif_split(img_name):

    img = Image.open(img_name)

    frame = 0

    try:

        while True:

            img.seek(frame)

            img.save('split_gif/{}.png'.format(frame))

            frame += 1

    except EOFError:
        
        print("Reach Maximum frame!")



    
