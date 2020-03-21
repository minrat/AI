from PIL import Image, ImageDraw, ImageFont
from random import choice, randint, randrange
import string

# 候选字符集,大小写字母+数字
chrs = string.ascii_letters + string.digits


def selected_chars(length):
    """
    返回length个随机字符串
    """
    result = ''.join(choice(chrs) for _ in range(length))
    return result

def get_color():
    """
    设置随机颜色
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r,g,b)

def get_pic(size=(200, 100), char_number=6, bg_color=(255, 255, 255)):
    """
    图片大小，验证码长度，背景颜色
    """
    # 创建空白图像和绘图对象
    image_tmp = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(image_tmp)

    # 生成并计算随机字符的宽度和高度
    text = selected_chars(char_number)
    font = ImageFont.truetype('Roboto-Regular.ttf', 48)  # 选定一款系统字体
    width, height = draw.textsize(text, font)
    if width + 2*char_number > size[0] or height > size[1]:
        print('Size Error!')
        return

    # 绘制字符串
    startX = 0
    width_eachchr = width // char_number  # 计算每个字符宽度
    for i in range(char_number):
        startX += width_eachchr + 1
        position = (startX, (size[1]-height)//2+randint(-10, 10))  # 字符坐标, Y坐标上下浮动
        draw.text(xy=position, text=text[i], font=font, fill=get_color())  # 绘制函数

    # 对像素位置进行微调，实现验证码扭曲效果
    img_final = Image.new('RGB', size, bg_color)
    pixels_final = img_final.load()
    pixels_tmp = image_tmp.load()
    for y in range(size[1]):
        offset = randint(-1, 0)  # randint()相当于闭区间[x,y]
        for x in range(size[0]):
            newx = x + offset  # 像素微调
            if newx >= size[0]:
                newx = size[0] - 1
            elif newx < 0:
                newx = 0
            pixels_final[newx, y] = pixels_tmp[x, y]

    # 绘制随机颜色随机位置的干扰像素
    draw = ImageDraw.Draw(img_final)
    for i in range(int(size[0]*size[1]*0.07)):  # 7%密度的干扰像素
        draw.point((randrange(size[0]), randrange(size[1])), fill=get_color())  # randrange取值范围是左开右闭

    # 绘制随机干扰线，这里设置为8条
    for i in range(8):
        start = (0, randrange(size[1]))
        end = (size[0], randrange(size[1]))
        draw.line([start, end], fill=get_color(), width=1)

    # 绘制随机弧线
    for i in range(8):
        start = (-50, -50)  # 起始位置在外边看起来才会像弧线
        end = (size[0]+10, randint(0, size[1]+10))
        draw.arc(start+end, 0, 360, fill=get_color())

    # 保存图片
    img_final.save('code.jpg')
    img_final.show()


if __name__ == '__main__':
    get_pic()
    # get_pic((200, 100), 5, (255, 255, 255))
