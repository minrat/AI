import cv2

img = cv2.imread("handshake.jpg")

cv2.putText(img, "Machine Learn", (20, 50),
            cv2.FONT_HERSHEY_TRIPLEX, 2.0, (10, 10, 10), thickness=2)
cv2.putText(img, "Shake With Robot , 2018.10.07", (20, 400),
            cv2.FONT_HERSHEY_PLAIN, 2.0, (10, 10, 10), thickness=2)

cv2.namedWindow("Image_Show")
cv2.imshow("Image_Show", img)
cv2.waitKey(0)
