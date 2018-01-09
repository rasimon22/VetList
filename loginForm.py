from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms import BooleanField
from wtforms.validators import Required


class SigninForm(FlaskForm):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Secure Password', validators=[Required()])
    remember = BooleanField('Remember Me')
