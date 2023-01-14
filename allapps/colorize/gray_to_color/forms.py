from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField



class ImgloadForm2(FlaskForm):
    image = FileField('image', validators=[FileRequired(), 
    	                                   FileAllowed(['jpg', 'png', 'jpeg'], 'Upload Images only in--> jpg, jpeg, or png')],
                                           render_kw={"accept":".png, .jpg, .jpeg"})

    submit = SubmitField('Submit') 