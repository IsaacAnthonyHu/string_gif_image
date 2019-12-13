from PIL import Image
import argparse

# 命令行输入参数处理，详情可见MODULE.MD
parser = argparse.ArgumentParser()
parser.add_argument('file')  # 输入文件,设定位置参数file，为转换目标的图片文件
parser.add_argument('-o', '--output')   # 输出文件，设定可选参数output，为输出文件的名称，默认为字符串类型
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽，设定可选参数width，默认值为80整数类型
parser.add_argument('--height', type=int, default=80)  # 输出字符画高，设定可选参数height，默认值为80整数类型

# 获取参数
args = parser.parse_args()

print(args)
input("""Ensure your args.
And press any key to continue.""")

# 从args中将参数赋值到新建变量中
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 将256灰度值映射到70个字符上
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):  # RGBA颜色中，最后ALPHA值为透明度，0代表全透明，1表示不透明
	if alpha == 0:  # 若ALPHA为0则为透明，用空白表示
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 根据当前像素的RGB值返回对应的灰度值
	unit = (256.0 + 1)/length  # 将灰度值按比例对应到列表长度(+1的理由没有明白，测试下不加一结果也一样，怀疑是四舍五入之类的)
	return ascii_char[int(gray/unit)]  # 将灰度值按比例对应为灰度列表中的字符


if __name__ == '__main__':  # 若模块是直接运行的，则执行以下代码块

	im = Image.open(IMG)
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)  # 图片缩小，使用最邻近的像素点

	txt = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j, i)))
			# 如果是在函数调用中，*args表示将可迭代对象扩展为函数的参数列表
			# 例如args = (1,2,3)
			# func = (*args)
			# 等价于函数调用func(1,2,3)
		txt += '\n'

	print(txt)

	# 字符画输出到文件
	if OUTPUT:  # 若指定参数output 文件，则添加进该文件中
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:  # 若无指定output 参数，则新建output.txt文件写入内容
		with open("output.txt", 'w') as f:
			f.write(txt)
