from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class KtEntryForm(FlaskForm):
    submit = SubmitField('&#x26FE')
class EntryForm(FlaskForm):
    info = StringField('Info', validators=[DataRequired()])
    submit = SubmitField('submit')