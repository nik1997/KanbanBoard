from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User, Task

class LoginForm(FlaskForm):
    '''
        Login form with, email, password, remember_me (checkbox) and submit button
    '''
    email = StringField('Email Address')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    '''
        Registration form asking all the details with validation in each field
    '''
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    maxProgressLimit = IntegerField('Maximum Number of Tasks in Progress', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',
        validators=[DataRequired(), EqualTo('password')]) # ensuring the repeated passwords match
    submit = SubmitField('Register')

    def validate_email(self, email):
        '''
            Helper function to validate email by checking if the email is already used for creating a user.
        '''
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')
