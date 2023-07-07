from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeLocalField
from wtforms.validators import DataRequired, Email, Length, Regexp


class ReviewForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30), Regexp('.*gmail.com$', message='Email must end with gmail')])
    message = TextAreaField('message')
  
