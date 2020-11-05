import cv2
from image_show import viewImage

image_path = './images/girls.jpeg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)

faces_detected = f'Лиц обнаружено {len(faces)}'

print(faces_detected)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

viewImage(image, faces_detected)