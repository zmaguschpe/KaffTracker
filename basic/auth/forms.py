from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField #BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Info', validators=[DataRequired()])
    password = PasswordField('Info', validators=[DataRequired()])
    # pw validate hier?
    #bool remember
    submit = SubmitField('submit')

class RegisterForm(FlaskForm):
    username = StringField('Info', validators=[DataRequired()])
    password = PasswordField('Info', validators=[DataRequired()])
    #validate >1
    submit = SubmitField('submit')
    
 
'''
class LoginForm(FlaskForm):
    username = StringField(u'Username', validators=[validators.DataRequired()])
    password = PasswordField(u'Password', validators=[validators.optional()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our the exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True

'''