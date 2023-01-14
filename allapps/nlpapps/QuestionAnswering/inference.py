import os, pickle

from transformers import  pipeline

def load_QA_model():

    tok_fpath = 'allapps/nlpapps/QuestionAnswering/files/tokenizer_QA_roberta_base_squad2.pickle'
    mod_fpath = 'allapps/nlpapps/QuestionAnswering/files/model_QA_roberta_base_squad2.pickle' 

    # loading tokenizer
    with open(os.path.abspath(tok_fpath), 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    # loading model
    with open(os.path.abspath(mod_fpath), 'rb') as handle:
        model = pickle.load(handle)
    
    # loading question_answering func
    question_answering = pipeline(task = "question-answering",model=model,tokenizer=tokenizer)

    return  question_answering   



