from flask import  Blueprint, render_template, session, jsonify

from allapps.prediction.heart_attack.forms import HAform
from allapps.prediction.heart_attack.inference import loadHAmodel, HApredict

from common.common import  loadimage
from allapps.prediction.malaria_screener.forms import ImgloadForm
from allapps.prediction.malaria_screener.inference import load_malaria_model, malaria_detector


from allapps.prediction.sentiment_analysis.forms import CTform
from allapps.prediction.sentiment_analysis.inference import load_model_and_tokenizer, make_prediction


prediction = Blueprint('prediction',__name__, template_folder='templates')



@prediction.route('/heart_attack', methods=['GET', 'POST'])
def heart_attack():

    form = HAform()
    scaler, model = loadHAmodel()
    result = {"prid": "none", "conf": "none"}

    if form.validate_on_submit():

        # Grab the data from the breed on the form.
        session['cp'] = form.cp.data
        session['thalachh'] = form.thalachh.data
        session['exng'] = form.exng.data
        session['oldpeak'] = form.oldpeak.data
        session['age'] = form.age.data
        session['sex'] = form.sex.data

        result = HApredict(scaler, model, session['cp'], session['thalachh'], session['exng'],
                                        session['oldpeak'], session['age'], session['sex'])

        return render_template("heart_attack.html", form=form, result=result, jump_to="result")

    return render_template('heart_attack.html', form=form, result=result, jump_to="top")





@prediction.route('/malaria_prediction', methods=['GET', 'POST'])
def malaria_prediction():

    form = ImgloadForm()
    return render_template("malaria_prediction.html", form=form)



@prediction.route('/malaria_prediction/malaria_prediction_ajax', methods=['POST'])
def malaria_prediction_ajax():
       
    form  = ImgloadForm()
    model = load_malaria_model() 

    if form.validate_on_submit():
        try:
            ori_img  = loadimage(form.image.data)
            prid, conf, Prob = malaria_detector(ori_img,model)  
                        
            return jsonify(data={"prid":prid, "conf" : conf , "massage":"sucess"})
        except: 
            return jsonify(data={"prid":prid, "conf" : conf , "massage":"codeerror"})   

    return jsonify(data={"prid":form.errors, "conf" : "none" , "massage":"fail"}) 








@prediction.route('/Coronavirus_tweets', methods=['GET', 'POST'])
def Coronavirus_tweets():

    form = CTform()
    return render_template("Coronavirus_tweets.html", form=form)



@prediction.route('/Coronavirus_tweets/Coronavirus_tweets_ajax', methods=['POST'])
def Coronavirus_tweets_ajax():
       
    form  = CTform()
    tokenizer, all_stopwords, model  = load_model_and_tokenizer() 
    
    if form.validate_on_submit():
        try:
            text  = form.texts.data
            prid, conf = make_prediction(text,tokenizer, all_stopwords, model) 
            return jsonify(data={"prid":prid, "conf" : conf , "massage":"sucess"})
        except: 
            return jsonify(data={"prid":prid, "conf" : conf , "massage":"codeerror"})   
    return jsonify(data={"prid":form.errors, "conf" : "none" , "massage":"fail"}) 

