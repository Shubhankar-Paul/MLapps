from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired


class QAform(FlaskForm):

    context    = TextAreaField(u'Context:', validators=[DataRequired()] )
    question   = StringField(u'Question:', validators=[DataRequired()] )
    submit     = SubmitField('Submit') 
    


