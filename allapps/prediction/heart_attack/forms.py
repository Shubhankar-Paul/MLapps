from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, SubmitField, IntegerRangeField, DecimalRangeField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class HAform(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''

    cp          = SelectField(u'Chest Pain Type:', choices=[(1, "Typical angina"  ), 
                                                            (2, "Atypical angina" ), 
                                                            (3, "Non-anginal pain"),
                                                            (0, "Asymptomatic"    ) ], validators=[DataRequired()] )

    thalachh    = IntegerRangeField(u'Heart Rate (Maximum):', validators=[DataRequired(), 
                                                                                 NumberRange(min=71, max=202, message='bla')])

    exng        = RadioField(u'Exercise Induced Angina?:', choices=[(1, "Yes"),                                                      
                                                                    (0, "No" ) ], default=1, validators=[DataRequired()] )

    oldpeak     = DecimalRangeField(u'ST Depression :',
                                              validators=[InputRequired(), NumberRange(min=0.0, max=6.2, message='bla') ] ,render_kw={"step": ".1"})


    age         = IntegerRangeField(u'Age (in Years):', validators=[DataRequired(), NumberRange(min=1, max=100, message='bla')])

    sex         = SelectField(u'Gender:', choices=[(1, "Male"   ),                                                      
                                                   (0, "Female" ) ], validators=[DataRequired()] )

    submit      = SubmitField('Submit') 


