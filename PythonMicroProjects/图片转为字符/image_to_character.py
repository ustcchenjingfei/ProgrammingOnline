"""
灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。
将某一颜色分解成r g b三种颜色分量，在转换为灰度值 gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
"""

from PIL import Image

IMG = r'image_to_character.png'
WIDTH = 60
HEIGHT = 45

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):  # alpha透明度 （0~255）
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
    x = int((gray / (256 + 1) * length))  # （此时alpha已固定。gray/256 = x/length x为灰度对应的字符的位置索引）
    # x = int((gray / (alpha+1)) * length) # 此时alpha未固定，+1是为了防止gray=255,alpha=255,而导致x超出列表索引值
    return ascii_char[x]  # 不同的灰度对应着不同的字符，通过灰度来区分色块


if __name__ == '__main__':
    im = Image.open(IMG)  # 使用 PIL 的 Image.open 打开图片文件，获得对象 im
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    # 使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片。

    txt = ""

    for i in range(HEIGHT):  # 遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))  # j为横坐标，i为纵坐标
            # im.getpixel((j,i))  获取得到坐标 (j,i) 位置的 RGB 像素值（有的时候会包含 alpha 值），返回的结果是一个元组
            # im.getpixel的参数是（j,i）,（j,i）其实是图片的横纵坐标。通过调用这个函数，把图片的横纵坐标上的颜色，分割成了(r,g,b,alpha)这个四个参数
        txt += '\n'

    print(txt)
    # 写入文件
    with open("output.txt", 'w') as f:
        f.write(txt)
