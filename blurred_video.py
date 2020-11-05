import cv2

# blurred = cv2.GaussianBlur(image, (51, 51), 0)
# viewImage(blurred, 'Blurred dog')

capture = cv2.VideoCapture(0)

face_cascad = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def blur_face(img):
    """Blurs detected face"""

    (h, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)

    if dW % 2 == 0:
        dW -= 1
    if dH % 2 == 0:
        dH -= 1

    return cv2.GaussianBlur(img, (dW, dH), 0)

while True:
    ret, img = capture.read() # Получаем изображение с веб камеры

    faces = face_cascad.detectMultiScale(
        img,
        scaleFactor=1.1,
        minNeighbors=20,
        minSize=(20, 20)
    )

    radius = 20
    color = (255, 0, 0)
    thickness = 2

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img[y:y + h, x:x + w] = blur_face(img[y:y+h, x:x+w])

    cv2.imshow('From camera', img) # Выводим изображение

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()