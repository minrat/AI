# pip install qrcode
'''
https://pypi.org/project/qrcode/
    version :
        二维码版本（支持 1 到 40，其中版本1为： 21x21 像素)
    error_correction：（维码的错误纠正功能）
        ERROR_CORRECT_L
            约7%或更少的错误能被纠正.
        ERROR_CORRECT_M (default)
            约15%或更少的错误能被纠正
        ERROR_CORRECT_Q
            约25%或更少的错误能被纠正
        ERROR_CORRECT_H.
            约30%或更少的错误能被纠正
    box_size ：
        二维码的盒子有多少像素
    border ：
        边框的厚度，默认为4
'''
import qrcode
qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

if __name__ == '__main__':
    # 信息
    data = []
    name = input("What is your name:\n")
    no = input("What is your No?\n")
    address = input("What is your address?\n")
    # 信息丰富
    data.append(name)
    data.append(no)
    data.append(address)
    #
    qr.add_data(data)
    qr.make(fit=True)
    # 图片背景以及填充色可通过：fill_color 及 back_color 更改
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('QR_Pic_demo.png')
