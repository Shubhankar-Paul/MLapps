from flask import Blueprint , render_template, jsonify


from allapps.nlpapps.QuestionAnswering.forms import QAform
from allapps.nlpapps.QuestionAnswering.inference import load_QA_model

from allapps.nlpapps.summarization.forms import SAform
from allapps.nlpapps.summarization.inference import load_SA_model


nlpapps = Blueprint('nlpapps',__name__, template_folder='templates')



@nlpapps.route('/QuestionAnswering', methods=['GET', 'POST'])
def QuestionAnswering():

    form = QAform()
    return render_template("QuestionAnswering.html", form=form)


@nlpapps.route('/QuestionAnswering/QuestionAnswering_ajax', methods=['POST'])
def QuestionAnswering_ajax():
       
    form  = QAform()
    model = load_QA_model() 

    if form.validate_on_submit():
        try:               
            result = model(question = form.question.data,
                           context  = form.context.data  ) 

            conf   = f"{(result['score']):2.2%}"
            
            return jsonify(data={"prid":result['answer'], "conf" : conf  , "massage":"sucess"})
        except: 
            return jsonify(data={"prid":result['answer'], "conf" : conf , "massage":"codeerror"})   

    return jsonify(data={"prid":form.errors, "conf" : "none" , "massage":"fail"}) 




@nlpapps.route('/summarization', methods=['GET', 'POST'])
def summarization():

    form = SAform()
    return render_template("summarization.html", form=form)


@nlpapps.route('/summarization/summarization_ajax', methods=['POST'])
def summarization_ajax():
       
    form  = SAform()
    model = load_SA_model() 

    if form.validate_on_submit():
        try:               
            result = model(form.longtexts.data,
                            min_length=1, max_length=form.maxlength.data )[0] 
            
            return jsonify(data={"prid":result['summary_text'], "massage":"sucess"})
        except: 
            return jsonify(data={"prid":result['summary_text'], "massage":"codeerror"})   

    return jsonify(data={"prid":form.errors, "massage":"fail"}) 

