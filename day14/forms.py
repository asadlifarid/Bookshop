from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.csrf import CSRFProtect



class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    
    


class LoginForm(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    is_subscribe = BooleanField()


