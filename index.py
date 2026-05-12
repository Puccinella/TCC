from deepface import DeepFace
import cv2

resultado = DeepFace.find(img_path='testes/faker.jpg',db_path='banco')

for x in range(len(resultado)):
    print(resultado[x])