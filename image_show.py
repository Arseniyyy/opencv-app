import cv2


def viewImage(image, name_of_window):
    """Views image"""

    cv2.namedWindow(name_of_window)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop(path_to_image):
    """Crops image"""

    image = cv2.imread(path_to_image)
    cropped = image[10:500, 100:200]
    viewImage(cropped, 'Dog after cropping')
