import urllib.request
import numpy as np
import cv2


class IPCamera:


    def __init__(self, url, chunk_size=4096):
        self.url = url
        self.chunk_size = chunk_size
        self.buffer = b''
        self.stream = None
        self._conectar()

    def _conectar(self):
        self.stream = urllib.request.urlopen(self.url)
        self.buffer = b''

    def isOpened(self):
        return self.stream is not None

    def set(self, *args, **kwargs):
        # No-op: resolução é definida pelo app da câmera IP, não pelo
        # cv2. Mantido só pra compatibilidade com o código que já
        # chamava cam.set(...).
        return True

    def read(self):
        """Retorna (ret, frame), igual ao cv2.VideoCapture.read()."""
        if self.stream is None:
            return False, None

        while True:
            try:
                data = self.stream.read(self.chunk_size)
            except Exception as e:
                print("Erro lendo o stream da câmera IP:", e)
                return False, None

            if not data:
                # conexão caiu / stream acabou
                return False, None

            self.buffer += data

            start = self.buffer.find(b'\xff\xd8')
            end = self.buffer.find(b'\xff\xd9')

            if start != -1 and end != -1:
                jpg = self.buffer[start:end + 2]
                self.buffer = self.buffer[end + 2:]

                frame = cv2.imdecode(
                    np.frombuffer(jpg, dtype=np.uint8),
                    cv2.IMREAD_COLOR
                )

                if frame is not None:
                    return True, frame
                # frame corrompido, continua tentando

    def release(self):
        if self.stream is not None:
            try:
                self.stream.close()
            except Exception:
                pass
            self.stream = None
