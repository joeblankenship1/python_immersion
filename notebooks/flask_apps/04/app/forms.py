from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class DataInput(FlaskForm):
    record_id = IntegerField('record_id', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])
    submit = SubmitField('Submit')

