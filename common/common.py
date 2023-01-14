import cv2 as cv
import numpy as np
import base64

#from PIL import Image


def loadimage(img_data):

    #img = Image.open(img_data)                   #| this will lod the image as is if image is grayscale the -->(h,w) &
    #img = np.array(img)                          #| if the original image is colore then --> (h,w,c) 


    img = np.fromfile(img_data, np.uint8)         #| this approach will give us option to chose for example
    img = cv.imdecode(img, cv.IMREAD_COLOR)       #| cv.IMREAD_COLOR     --> will always load the image in  COLOR
                                                  #| cv.IMREAD_GRAYSCALE --> will always load the image in  GRAYSCALE
    return img       

def showimage(img,typ):

    _, buffer = cv.imencode(typ, img)
    image = base64.b64encode(buffer).decode('utf-8')
    return image