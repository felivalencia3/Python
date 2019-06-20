from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired, Length


class RegisterForm(Form):
    name = StringField(
        'name', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'pass', validators=[DataRequired(), Length(min=6, max=40)]
    )


class LoginForm(Form):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember")


class ForgotForm(Form):
    email = StringField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
