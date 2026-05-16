import cv2
import tkinter as tk
import os
import sys
from datetime import datetime
import time

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
nomeV=''
cv2.namedWindow("gravar")

def fechar():
    sys.exit()

def inserir():
    global nomeV
    nomeV=entrada.get()
    root.destroy()

root = tk.Tk()
root.geometry('300x200')
root.title('Registro de estudante.')
aviso = tk.Label(root, text='Insira o JC do estudante!',font=('helvetica',16))
aviso.pack()

entrada = tk.Entry(root)
entrada.pack()

Bfechar=tk.Button(root,command=fechar,text=('Cancelar'))
Bfechar.pack(side='right')

Bconfirma=tk.Button(root,command=inserir,text=('confirmar'))
Bconfirma.pack(side='right')

root.mainloop()

img_counter = 0



caminho = 'banco/'+nomeV
try:
    os.makedirs(caminho,exist_ok=True)
except FileExistsError:
    print("!este jc já foi registrado!")
else:
    pass


nome=nomeV+'-'

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("B.O")
        break
    

    frame = cv2.putText(frame,'Aluno: '+ nomeV,(800,40),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    frame = cv2.putText(frame,datetime.now().strftime("%d/%m/%Y %H:%M:%S"),(850,620),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)

    k = cv2.waitKey(1)
    
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        nome = nome.strip('1234567890')+str(img_counter)
        cv2.imwrite(nome+'.png',frame)
        os.replace(nome+'.png',caminho+'/'+nome+'.png')
        img_counter += 1
        cv2.imshow("gravar", frame)
        time.sleep(0.67)

    frame = cv2.putText(frame,'Nº de fotos tiradas: '+ str(img_counter),(800,80),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    frame = cv2.putText(frame,'Esc - Sair',(40,40),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
    frame = cv2.putText(frame,'Espaco - Tirar foto',(40,80),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)

    cv2.imshow("gravar", frame)

cam.release()

cv2.destroyAllWindows()
