import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) # 3 untuk lebar
cap.set(4,480) # 4 untuk tinggi 

faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


while True:
    success, img = cap.read()
    abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = faceDetector.detectMultiScale(abu, 1.3,5)
    for (x, y, w, h) in face:
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(225,0,0),3) #(biru,hijau,merah)
    cv2.imshow("video",img)
    # cv2.imshow("abu", abu)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
