import cv2
from deepface import DeepFace
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow("gravar")
count = 0
verificado=False
match=''
nome=''
x,y,height,width=0,0,0,0
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
    if count == 10:
        try: match=DeepFace.find(frame,'banco')
        except: 
            nome="N/A"
            verificado=False
        else: 
            if not match[0].empty:
                x=match[0].at[0,'source_x']
                height=match[0].at[0,'source_h']
                y=match[0].at[0,'source_y']
                width=match[0].at[0,'source_w']
                nome = str(match[0].at[0, "identity"]).split('\\')[1]
                verificado = True
            else:
                nome = "N/A"
                verificado = False
        count=0


    frame = cv2.putText(frame,'match:'+nome,(x,y-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    frame = cv2.rectangle(frame,(x,y),(x+width,y+height),(0,0,200),2)

    cv2.imshow("gravar", frame)

cam.release()

cv2.destroyAllWindows()