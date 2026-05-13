import cv2
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("gravar")

img_counter = 0
nomeV=str(input("insira o JC do estudante: "))
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
    cv2.imshow("gravar", frame)


    k = cv2.waitKey(1)
 
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        nome = nome.strip('1234567890')+str(img_counter)
        
        print(nome)
        cv2.imwrite(nome+'.png',frame)

        os.rename(nome+'.png',caminho+'/'+nome+'.png')

        img_counter += 1



cam.release()

cv2.destroyAllWindows()
