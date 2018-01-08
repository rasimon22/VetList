from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email
class SignupForm(FlaskForm):
    branches = [('USMC', 'United States Marine Corps'),
            ('Navy','U.S. Navy'), ('Army','U.S. Army'), 
            ('USAF', 'United States Air Force'), ('USCG', 'U.S. Coast Guard')] 
    username =TextField('Username', validators=[Required()])
    firstName  =TextField('firstName', validators=[Required()])
    lastName  =TextField('firstName', validators=[Required()])
    branch = SelectField(label="Branch",choices = branches,
            validators=[Required('Please enter your branch of service')])
    email = TextField('Email address', validators=[Required('Provide email address'), 
        Email()])
    password=PasswordField('Secure Password', validators=[Required(), 
        EqualTo('confirm',message='passwords must match')])
    confirm=PasswordField('Match passwords',validators=[Required()])
