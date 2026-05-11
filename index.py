from deepface import DeepFace

resultado = DeepFace.verify('db/lula.webp','lula2.webp')

print(resultado['verified'])