from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email
class SigninForm(FlaskForm):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Secure Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    
