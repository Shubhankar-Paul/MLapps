import numpy as np 
import re, os, pickle
from nltk.stem.porter import PorterStemmer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences 




def load_model_and_tokenizer():

    tokenizer_fpath = 'allapps/prediction/sentiment_analysis/files/tokenizer.pickle'
    model_fpath     = 'allapps/prediction/sentiment_analysis/files/Corona_tweets_MODEL.h5'
    stopwords_fpath = 'allapps/prediction/sentiment_analysis/files/all_stopwords.pickle'

    with open(os.path.abspath(tokenizer_fpath), 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open(os.path.abspath(stopwords_fpath), 'rb') as handle:
        all_stopwords = pickle.load(handle)

    model = load_model(os.path.abspath(model_fpath))

    return tokenizer, all_stopwords, model   


def make_prediction(text,tokenizer, all_stopwords, model):

    max_seq_len = 60 
    
    ## Clean Text
    clean = re.sub('[^a-zA-Z]', ' ', text)
    clean = clean.lower()
    clean = clean.split()
    ps = PorterStemmer()
    all_stopwords.remove('not')
    clean = [ps.stem(word) for word in clean if not word in set(all_stopwords)]
    clean = ' '.join(clean)


    ## Generate Sequences
    sequence = tokenizer.texts_to_sequences([clean])

    ## PAD Sequences
    sequence_pad = pad_sequences(sequence, maxlen=max_seq_len, value=0, padding='post', truncating='pre')

    ## predict probabilities
    predict_prob = model.predict(sequence_pad)

    ## predict classes
    predict_class = np.argmax(predict_prob,axis=1)
    

    ## display result
    if predict_class ==2:
        prid = "Neutral"
        conf =  f'({(predict_prob[0][predict_class][0]):2.4%})'

    elif predict_class ==1:
        prid = "Positive"
        conf =  f'({(predict_prob[0][predict_class][0]):2.4%})'

    elif predict_class ==0:
        prid = "Negative"
        conf =  f'({(predict_prob[0][predict_class][0]):2.4%})'

    else :
        prid = "error" 
        conf = "error"
    
    return prid, conf