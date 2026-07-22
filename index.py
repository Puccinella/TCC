import cv2
import time
from deepface import DeepFace
from deepface.modules.verification import find_distance
from banco_de_dados import buscar_todos_embeddings
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow("gravar")
tI=time.time()
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
    if count%20==0:
        try: 
            resultado = DeepFace.represent(frame, model_name='Facenet512', enforce_detection=False)
            embedding_cam = resultado[0]["embedding"]

            rosto = resultado[0]["facial_area"]
            x = rosto["x"]
            y = rosto["y"]
            height = rosto["h"]
            width = rosto["w"]
            
            menor_distancia = None
            melhor_jc = None
            for prontuario, embedding in buscar_todos_embeddings():
                distancia = find_distance(embedding_cam, embedding, distance_metric='cosine')
                if menor_distancia is None or distancia < menor_distancia:
                    menor_distancia = distancia
                    melhor_jc = prontuario
        except: 
            nome="N/A"
            x,y,height,width=0,0,0,0
            verificado=False
        else:
            if melhor_jc is not None and menor_distancia < 0.4:
                nome = melhor_jc
                verificado = True
            else:
                nome = "N/A"
                x,y,height,width=0,0,0,0
                verificado = False

    frame = cv2.putText(frame,'match:'+nome,(x,y-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    frame = cv2.rectangle(frame,(x,y),(x+width,y+height),(0,0,200),2)

    cv2.imshow("gravar", frame)

cam.release()

cv2.destroyAllWindows()

import menu