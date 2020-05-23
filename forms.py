from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    useremail = StringField('Email', validators=[DataRequired(),Email()])
    userpass = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    useremail = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    userpass = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(useremail=field.data).first():
            raise ValidationError('Your email has been already registered!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')
