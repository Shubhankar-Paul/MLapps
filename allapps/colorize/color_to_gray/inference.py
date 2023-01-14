import cv2 as cv


def color_to_gray(img_bgr):

    img_gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)

    return img_gray



