import cv2

# 读入图片资源
img = cv2.imread("handshake.jpg")
cv2.namedWindow("Image_Show_Pre")
cv2.imshow("Image_Show_Pre", img)

# 负片效果变换
r, g, b = cv2.split(img)
r = 255 - r
g = 255 - g
b = 255 - b

img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

cv2.namedWindow("Image_Show_After")
cv2.imshow("Image_Show_After", img)
cv2.waitKey(0)


