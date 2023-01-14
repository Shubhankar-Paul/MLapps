from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerRangeField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class SAform(FlaskForm):

    longtexts  = TextAreaField(u'Long Text:', validators=[DataRequired()] )
    maxlength  = IntegerRangeField(u'Maximum Summarize Words:', validators=[DataRequired(), 
                                                                            NumberRange(min=1, max=100, message='bla')])
    submit     = SubmitField('Submit') 
    