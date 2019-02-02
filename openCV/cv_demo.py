# 引用opencv 工具库
import cv2

# 读入图片资源
img = cv2.imread("handshake.jpg", cv2.IMREAD_COLOR)
# 创建显示窗体
cv2.namedWindow("Image_Show")
# 将图片资源加载至窗体
cv2.imshow("Image_Show", img)
# 无限期等待输入
k = cv2.waitKey(0)
# 当输入ESC时退出
if k == 27:
    cv2.destroyAllWindows()
