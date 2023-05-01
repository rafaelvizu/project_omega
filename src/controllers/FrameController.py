import cv2
import os
from helpers.simple_facerec import SimpleFacerec

#os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'


class FrameController():
     def __init__(self, path_to_images):
          self.path_to_images = path_to_images
          self.str = SimpleFacerec()
          self.str.load_encoding_images(path_to_images)


     def update_storage(self):
          self.str.load_encoding_images(self.path_to_images)
          

     def generateFrames(self, RTSP_URL):
          #cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
          cap = cv2.VideoCapture(0)

          while True:    
               ret, frame = cap.read()

               # detecta as faces
               face_locations, face_names = self.str.detect_known_faces(frame)

               for face_loc, name in zip (face_locations, face_names):
                    top, right, bottom, left = face_loc

                    # desenha um retangulo na face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

                    # escreve o nome da pessoa
                    if name == 'Unknown':
                         name = 'Desconhecido'

                    cv2.putText(frame, name, (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

               # criar imagem do frame e retorná-la
               img = cv2.imencode('.jpg', frame)[1].tobytes()

               
               
               yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
