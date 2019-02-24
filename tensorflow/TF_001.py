import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

# 读取图像的原始数据
image_raw_data = tf.gfile.FastGFile('p_001.png', 'rb').read()  # 必须是 ‘rb’ 模式打开，否则会报错

with tf.Session() as sess:
    # 将图像使用 jpeg 的格式解码从而得到图像对应的三维矩阵
    # tf.image.decode_jpeg 函数对 png 格式的图像进行解码。解码之后的结果为一个张量，
    img_data = tf.image.decode_jpeg(image_raw_data)

    # 输出解码之后的三维矩阵。
    print(img_data.eval())

# 打印图片
with tf.Session() as sess:
    plt.imshow(img_data.eval())
    plt.show()

# 重新调整图片大小
with tf.Session() as sess:
    resized = tf.image.resize_images(img_data, [300, 300], method=0)

    # TensorFlow的函数处理图片后存储的数据是float32格式的，需要转换成uint8才能正确打印图片。
    print("Digital type: ", resized.dtype)
    print("Digital shape: ", resized.get_shape())
    cat = np.asarray(resized.eval(), dtype='uint8')
    # tf.image.convert_image_dtype(rgb_image, tf.float32)
    plt.imshow(cat)
    plt.show()
# 图片色彩调整
with tf.Session() as sess:
    # 将图片的亮度 -0.5。
    adjusted = tf.image.adjust_brightness(img_data, -0.5)
    plt.imshow(adjusted.eval())
    plt.show()

    # 将图片的亮度 +0.5
    adjusted = tf.image.adjust_brightness(img_data, 0.5)
    plt.imshow(adjusted.eval())
    plt.show()

    # 在[-max_delta, max_delta)的范围随机调整图片的亮度。
    adjusted = tf.image.random_brightness(img_data, max_delta=0.5)
    plt.imshow(adjusted.eval())
    plt.show()

with tf.Session() as sess:
    # 将图片的对比度 -5
    adjusted = tf.image.adjust_contrast(img_data, -5)
    plt.imshow(adjusted.eval())
    plt.show()

    # 将图片的对比度 +5
    adjusted = tf.image.adjust_contrast(img_data, 5)
    plt.imshow(adjusted.eval())
    plt.show()

    # 在[lower, upper]的范围随机调整图的对比度。
    lower = 7
    upper = 88
    adjusted = tf.image.random_contrast(img_data, lower, upper)
    plt.imshow(adjusted.eval())
    plt.show()
