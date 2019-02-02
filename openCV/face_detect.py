import cv2

cascPath = "haarcascade_frontalface_alt_tree.xml"
faceCascde = cv2.CascadeClassifier(cascPath)
image = cv2.imread("multi.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
faces = faceCascde.detectMultiScale(
    gray,
    scaleFactor=1.0009,
    minNeighbors=3,
    minSize=(30, 30),
)
print("Found {0} faces!".format(len(faces)))
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Multi Face Detect", image)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
