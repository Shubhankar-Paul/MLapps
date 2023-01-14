from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, length


class CTform(FlaskForm):

    texts       = TextAreaField(u'Coronavirus Tweets:', validators=[DataRequired(), length(max=200)] )

    submit      = SubmitField('Submit') 




