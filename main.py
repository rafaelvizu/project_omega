import cv2
from simple_facerec import SimpleFacerec


sfr = SimpleFacerec()
sfr.load_encoding_images('./tests/imgs/')


# load camera / o parametro é para o tanto de web cam que tem no pc
cap = cv2.VideoCapture(0)

while True:    
     ret, frame = cap.read()

     # detecta as faces
     face_locations, face_names =  sfr.detect_known_faces(frame)

     for face_loc, name in zip (face_locations, face_names):
          top, right, bottom, left = face_loc

          # desenha um retangulo na face
          cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

          # escreve o nome da pessoa
          cv2.putText(frame, name, (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

     cv2.imshow('Frame', frame)
     key = cv2.waitKey(1) # vai att a cada 1 milisegundo

     if key == 27:
          break

cap.release()
cv2.destroyAllWindows()
