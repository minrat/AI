import cv2
import numpy as np

h = 420
w = 630
img = np.zeros((h, w, 3), np.uint8)
p1 = np.random.randint(h, size=(2000, 1))
p2 = np.random.randint(w, size=(2000, 1))

for i in range(2000):
    img[p1[i], p2[i], [0]] = np.random.randint(0, 255)
    img[p1[i], p2[i], [1]] = np.random.randint(0, 255)
    img[p1[i], p2[i], [2]] = np.random.randint(0, 255)

cv2.imshow("Image_Show", img)
k = cv2.waitKey(0)
# 当输入ESC时退出
if k == 27:
    cv2.destroyAllWindows()
