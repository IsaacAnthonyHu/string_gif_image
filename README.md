# string_gif_image
Convert a gif image to frames, then convert them to string images, and finally add them together as another gif.

#TODO 动态图转字符画动态图的一个重要问题是：字符长宽与其横竖间距并不均等，本项目中已尽量使用等长宽字体square.ttf，但字符横竖间距并不能得到有效的调整

# 且对于不同字体需要重新分析其不同字符所占的黑色面积，从而重新建立灰度字符列表(完成)

目前的问题是，若开始就缩小图片，则输出结果过小；若不开始就缩小，则处理时间过长

目前想用cv2库直接读取图片灰度值，另直接使用np.vectorize(function)将灰度矩阵转化为对应字符，不知道在速度上会不会有改善(不一定，处理时间长应该是ImageDraw画了太多的字上去, 有时间用ipython测测)

可以换成`PIL.ImageDraw.Draw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")`

看看是不是比`PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)`快

https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html#fonts

```python
import cv2
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

def grayscale_convert(gs):
    ascii_char =list(r"""8B0$&@R2M9Z6WXNb5#3K4<>*QrSGVAEDwmeansq%1zdIUOgPH7kpoihFfxCLcuJ?Yv=T"+lt/\jy^}{;][()~:-|'`,!._ """)
    length = len(ascii_char)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

vconverter = np.vectorize(grayscale_convert)
result = vconverter(img)
```
以我目前的水平不知道该如何改进了，目前大图的缩放是一个问题，这个项目暂时就停在这里吧，以后有机会再继续优化。
