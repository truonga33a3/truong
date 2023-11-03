from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired

class SignUpForm(FlaskForm):
    inputFirstName = StringField('First Name',
        [DataRequired(message="Please enter your first name!")])
    inputLastName = StringField('Last Name',
        [DataRequired(message="Please enter your last name!")])
    inputEmail = StringField('Email address',
        [Email(message="Not a valid email address!"),
        DataRequired(message="Please enter your email address!")])
    inputPassword = PasswordField('Password',
        [InputRequired(message="Please enter your password!"),
        EqualTo('inputConfirmPassword', message="Password dose not match!")])
    inputConfirmPassword = PasswordField('Confirm password')
    submit = SubmitField('Sign Up')

class SignInForm(FlaskForm):
    inputEmail = StringField('Email address',
        [Email(message="Not a valid email address!"),
        DataRequired(message="Please enter your email address")])
    inputPassword = PasswordField('Password',
        [InputRequired(message="Please enter your password!")])
    submit = SubmitField('Sign In')

class TaskForm(FlaskForm):
    inputDescription = StringField('Task Description',
        [DataRequired(message="Please enetr your task content!")])
    inputPriority = SelectField('Priority', coerce = int)

    submit = SubmitField('Create Task')


class ProjectForm(FlaskForm):
    inputName = StringField('Project name',
        [DataRequired(message = "Please enter your project name!")])
    inputDescription = StringField('Project description',
        [DataRequired(message = "Please enter your project description!")])
    inputDeadline = DateField('Deadline', format='%Y-%m-%d', default=datetime.now() + relativedelta(months=+2))
    
    submit = SubmitField()