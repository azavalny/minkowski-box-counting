import cv2

def preprocess_image(img):
    """Preprocesses an image by increasing the saturation to allow for much more accurate bounding box detection"""

    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hsvImg[...,1] = hsvImg[...,1]*1.75 #increase saturation by 175%

    image_f =cv2.cvtColor(hsvImg,cv2.COLOR_HSV2BGR)

    return image_f