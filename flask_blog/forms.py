from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired , Length , Email , EqualTo, ValidationError
from flask_blog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

#FileField is type of field
#FileAllowed is type of file allowed


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

    def validate_username(self , username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Already used username , please choose another one')


    def validate_email(self , email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Already used email id , please choose another one')


class LoginForm(FlaskForm):

    email = StringField('Email', validators = [DataRequired() , Email()])
    password = PasswordField('Password' , validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username' , validators = [DataRequired() , Length(min = 2 , max = 20)])
    email = StringField('Email', validators = [DataRequired() , Email()])
    submit = SubmitField('Update')
    picture = FileField('Update Profile Picture' ,validators =  [FileAllowed(['jpg' , 'png'])])
    def validate_username(self , username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Already used username , please choose another one')


    def validate_email(self , email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Already used email id , please choose another one')


class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content' , validators = [DataRequired()])
    submit = SubmitField('Post')
