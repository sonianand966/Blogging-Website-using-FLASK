from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo



#import this to create or use forms in flask

class RegistrationForm(FlaskForm):
    #write the name of the class from where this class of RegistrationForm would be inherited, here it is FlaskForm

    # StringField is a class which creates an object of say string type returns it with some checks in place done by the validator part

    #validator again is a class of wtforms package comprising of many validation check methods like DataRequired() , Email() (valid email or not) , length of varioud fields , equal to options.....

    #Now , more importantly whatever you write inside the first argument of StringField is the "LABEL FOR THAT PARTICULAR CONTENT IN THE HTML FILE."
    username = StringField('Username' , validators = [DataRequired() , Length(min = 2 , max = 20)])
    email = StringField('Email', validators = [DataRequired() , Email()])
    password = PasswordField('Password'  , validators  = [DataRequired()])
    confirm_password = PasswordField('confirm' , validators = [DataRequired() , EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    email = StringField('Email', validators = [DataRequired() , Email()])
    password = PasswordField('Password' , validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
