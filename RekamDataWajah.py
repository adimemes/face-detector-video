import cv2, os

wajahDir = 'detector/wajah'
cap = cv2.VideoCapture(0)
cap.set(3,640) # 3 untuk lebar
cap.set(4,480) # 4 untuk tinggi 

faceDetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeDetector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
faceID = input("masukan nim anda [tekan enter]: ")
print ("posisikan wajah anda pada kamera")
ambilData = 1
while True:
    succes, img = cap.read()
    abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = faceDetector.detectMultiScale(abu, 1.3,5)
    for (x, y, w, h) in face:
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(225,0,0),2) #(biru,hijau,merah)
        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(wajahDir+'/'+namaFile,img)
        ambilData +=1
        roiabu = abu [y:y+h,x:x+w]
        roiwarna = img[y:y+h,x:x+w]
        mata = eyeDetector.detectMultiScale(roiabu)
        for (xe,ye,we,he) in mata:
            cv2.rectangle(roiwarna, (x,y), (x+w,y+h),(0,225,0),1)
    
    cv2.imshow("video",img)
    # cv2.imshow("abu", abu)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    elif ambilData>2:
        break

print("pengambilan data selesai")
cap.release()
cv2.destroyAllWindows()
