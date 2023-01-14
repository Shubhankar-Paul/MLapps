from flask import Blueprint , render_template, jsonify

from common.common import  loadimage, showimage 
from allapps.detection.cardiac_detection.forms import ImgloadForm
from allapps.detection.cardiac_detection.inference import load_cardiac_model, Cardiac


detection = Blueprint('detection',__name__, template_folder='templates')



@detection.route('/cardiac_detection', methods=['GET', 'POST'])
def cardiac_detection():

    form = ImgloadForm()
    return render_template("cardiac_detection.html", form=form)




@detection.route('/cardiac_detection/cardiac_detection_ajax', methods=['POST'])
def cardiac_detection_ajax():
       
    form  = ImgloadForm()
    model = load_cardiac_model() 

    if form.validate_on_submit():
        try:
            ori_img  = loadimage(form.image.data)
            detected_img = Cardiac(ori_img,model)               
            img_detected = showimage(detected_img,'.png') 
            
            return jsonify(data={"result":img_detected,"massage":"sucess"})
        except: 
            return jsonify(data={"result":"none","massage":"codeerror"})   

    return jsonify(data={"result":form.errors,"massage":"fail"}) 
