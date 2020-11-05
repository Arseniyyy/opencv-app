import cv2
from image_show import viewImage

image = cv2.imread('./images/dog.jpeg')

def grey_color(path_to_image):
    """Converts image to grey colors"""

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, threshold_image = cv2.threshold(image, 127, 255, 0)
    viewImage(gray_image, 'Dog in gray colors')
    viewImage(threshold_image, 'Black-white dog')


def blur_image():
    """Bluring image"""

    blurred = cv2.GaussianBlur(image, (51, 51), 0)
    viewImage(blurred, 'Blurred dog')

blur_image()