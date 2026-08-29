import cv2
import datetime
import time
from deepface import DeepFace
from deepface.modules.verification import find_distance
from banco_de_dados import buscar_todos_embeddings
from ip_camera import IPCamera
import urllib.request


tAbertu = 0
catraca_bloqueada = True   # começa bloqueada

def abrir():
    urllib.request.urlopen(IP_CATRACA + '/liberado')

def bloquear():
    urllib.request.urlopen(IP_CATRACA + '/bloqueado')

verificado=False



IP_CAMERA_URL = 'http://192.168.15.3:8080/video'
IP_CATRACA = 'http://192.168.15.7'

cam = IPCamera(IP_CAMERA_URL)
cv2.namedWindow("gravar")
count = 0
verificado=False
match=''
nome=''

x,y,height,width=0,0,0,0

saidas=[]

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
                if not saidas or (saidas[-1]['horario'] < datetime.datetime.now()-datetime.timedelta(seconds=10) or saidas[-1]['JC']!=nome):
                    saidaEntrada = {'JC': nome, 'horario': datetime.datetime.now()}
                    saidas.append(saidaEntrada)
                    print(saidaEntrada)
                    abrir()
                    tAbertu = time.perf_counter()
                    catraca_bloqueada = False   # agora está aberta
            else:
                nome = "N/A"
                x,y,height,width=0,0,0,0
                verificado = False

    if not catraca_bloqueada and time.perf_counter()-tAbertu > 5:
        bloquear()
        catraca_bloqueada = True   # só entra aqui de novo depois do próximo "abrir()"


    frame = cv2.putText(frame,'match:'+nome,(x,y-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    frame = cv2.rectangle(frame,(x,y),(x+width,y+height),(0,0,200),2)
    print(time.perf_counter()-tAbertu)
    cv2.imshow("gravar", frame)

cam.release()


cv2.destroyAllWindows()

import nova_interface
