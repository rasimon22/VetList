from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email
class SignupForm(Form):
    username =TextField('Username', validators=[Required()])
    email = TextField('Email address', validators=[Required('Provide email address'), Email()])
    password=PasswordField('Secure Password', validators=[Required(), 
        EqualTo('confirm',message='passwords must match')])
    confirm=PasswordField('Match passwords',validators=[Required()])
