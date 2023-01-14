import os, pickle
from transformers import  pipeline


def load_SA_model():

    tok_fpath = 'allapps/nlpapps/summarization/files/tokenizer_SA_sshleifer.pickle'
    mod_fpath = 'allapps/nlpapps/summarization/files/model_SA_sshleifer.pickle' 

    # loading tokenizer
    with open(os.path.abspath(tok_fpath), 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    # loading model
    with open(os.path.abspath(mod_fpath), 'rb') as handle:
        model = pickle.load(handle)
    
    # loading summarizer func
    summarizer = pipeline(task = "summarization",model=model,tokenizer=tokenizer)

    return  summarizer   