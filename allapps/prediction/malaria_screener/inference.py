import os,cv2
import numpy as np
import tensorflow as tf 

def load_malaria_model():

    model_fpath   = "allapps/prediction/malaria_screener/files/malaria_detector.h5"

    model = tf.keras.models.load_model( os.path.abspath(model_fpath))

    return model 


def malaria_detector(image, model):

    image = cv2.resize(image, (130, 130), interpolation = cv2.INTER_LINEAR)
    image = np.expand_dims(image, axis=0)
    output = model.predict(image)[0][0]

    if output <= 0.5:
        prid = "Parasitize found"
        conf =  f'({(1-output):2.2%})'
        Prob =  output

    elif output > 0.5:
        prid = "Uninfected" 
        conf = f'({(output):2.2%})'
        Prob = output 
    else:
        prid = "error" 
        conf = "error"
        Prob = "error"

    return prid, conf, Prob



        