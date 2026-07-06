import cv2
from deepface import DeepFace

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow("gravar")
count = 0
verificado=False
match=''
while True:
    ret, frame = cam.read()
    
    if not ret:
        print("B.O")
        break


    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    
    count+=1
    if count == 30:
        try: match=DeepFace.find(frame,'banco')
        except: 
            match="quem e esse neguinho?????"
            verificado=False
        else: 
            if not match[0].empty:
                match = str(match[0].at[0, "identity"]).split('\\')[1]
                verificado = True
            else:
                match = "quem e esse neguinho?????"
                verificado = False
        count=0
    frame = cv2.putText(frame,'match:'+match,(80,80),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)


    cv2.imshow("gravar", frame)

cam.release()

cv2.destroyAllWindows()