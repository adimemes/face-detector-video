import cv2

img = cv2.imread("gambar/one_piece.png")
cv2.imshow("luffy",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("luffy gray", gray)

detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faceDetector = detector.detectMultiScale(gray, scalefactor = 1.1, minNeighbors=3)

print (f'number of faces found = {len(faceDetector)}')

for (x,y,w,h) in faceDetector:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,225), thickness=2)

cv2.imshow("detector",img)
cv2.waitKey(0)