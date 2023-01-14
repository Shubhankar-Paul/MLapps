import os,cv2
import numpy as np
import tensorflow as tf 



def charbonnier_loss(y_true, y_pred):
    return tf.reduce_mean(tf.sqrt(tf.square(y_true - y_pred) + tf.square(1e-3)))


def peak_signal_noise_ratio(y_true, y_pred):
    return tf.image.psnr(y_pred, y_true, max_val=255.0)


def load_Enhance_model():

    model_fpath   = "allapps/enhance/low_light_img_enhancer/files/Low-light_image_enhancement.h5"

    model = tf.keras.models.load_model( os.path.abspath(model_fpath), 
                                        custom_objects={"charbonnier_loss": charbonnier_loss, 
                                                        "peak_signal_noise_ratio":peak_signal_noise_ratio})
    
    return model



def Enhance(original_image, model):

    image = cv2.resize(original_image, (600, 400), interpolation = cv2.INTER_LINEAR)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    output = model.predict(image)

    output_image = output[0] * 255.0
    output_image = output_image.clip(0, 255)
    output_image = output_image.reshape((np.shape(output_image)[0], np.shape(output_image)[1], 3))
    output_image = cv2.resize(output_image, (original_image.shape[1],original_image.shape[0]), interpolation = cv2.INTER_LINEAR)
    
    return output_image


    