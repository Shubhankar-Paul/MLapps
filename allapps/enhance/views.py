from flask import Blueprint , render_template, jsonify

from common.common import  loadimage, showimage
from allapps.enhance.low_light_img_enhancer.forms import ImgloadForm
from allapps.enhance.low_light_img_enhancer.inference import load_Enhance_model, Enhance


enhance = Blueprint('enhance',__name__, template_folder='templates')



@enhance.route('/lowlight_img_enhance', methods=['GET', 'POST'])
def lowlight_img_enhance():

    form = ImgloadForm()
    return render_template("lowlight_img_enhance.html", form=form)




@enhance.route('/lowlight_img_enhance/lowlight_img_enhance_ajax', methods=['POST'])
def lowlight_img_enhance_ajax():
       
    form  = ImgloadForm()
    model = load_Enhance_model() 

    if form.validate_on_submit():
        try:
            ori_img  = loadimage(form.image.data)
            enhance_img = Enhance(ori_img,model)               
            img_enhance = showimage(enhance_img,'.png') 
            
            return jsonify(data={"result":img_enhance,"massage":"sucess"})
        except: 
            return jsonify(data={"result":"none","massage":"codeerror"})   

    return jsonify(data={"result":form.errors,"massage":"fail"}) 

