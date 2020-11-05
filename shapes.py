import cv2
from image_show import viewImage
# from colors import image

image = cv2.imread('./images/dog.jpeg')

def draw_rectangle():
    """Draws rectangle on image"""

    cv2.rectangle(image, (384,0),(510,128),(0,255,0), 3)
    cv2.circle(image, (447, 63), 63, (0, 0, 255), -1)
    viewImage(image, 'Dog with rectangle')


def text():
    """Adds text to an image"""

    font = cv2.FONT_ITALIC
    cv2.putText(image, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

    viewImage(image, 'Dog image with text')