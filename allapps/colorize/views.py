from flask import Blueprint, render_template, jsonify


from common.common import  loadimage, showimage

from allapps.colorize.color_to_gray.forms import ImgloadForm
from allapps.colorize.color_to_gray.inference import color_to_gray

from allapps.colorize.gray_to_color.inference import load_Colorize_model , Colorize  



colorize = Blueprint('colorize',__name__, template_folder='templates')


@colorize.route('/color2gray' , methods=['GET', 'POST'])
def color2gray():

    form = ImgloadForm()
    return render_template("color2gray.html", form=form)



@colorize.route('/color2gray/color2gray_ajax', methods=['POST'])
def color2gray_ajax():
       
    form = ImgloadForm()

    if form.validate_on_submit():
        try:
            ori_img  = loadimage(form.image.data)
            gray_img = color_to_gray(ori_img) 
            img_gray = showimage(gray_img,'.png') 
            return jsonify(data={"result":img_gray,"massage":"sucess"})
        except:
            return jsonify(data={"result":"none","massage":"codeerror"})   

    return jsonify(data={"result":form.errors,"massage":"fail"}) 





@colorize.route('/gray2color' , methods=['GET', 'POST'])
def gray2color():

    form = ImgloadForm()
    return render_template("gray2color.html", form=form)


@colorize.route('/gray2color/gray2color_ajax', methods=['POST'])
def gray2color_ajax():
       
    form  = ImgloadForm()
    model = load_Colorize_model() 

    if form.validate_on_submit():

        try:
            ori_img  = loadimage(form.image.data)
            color_img = Colorize(model, ori_img)
            img_color = showimage(color_img,'.png') 
            
            return jsonify(data={"result":img_color,"massage":"sucess"})
        except:
            return jsonify(data={"result":"none","massage":"codeerror"})  
            
    return jsonify(data={"result":form.errors,"massage":"fail"}) 

