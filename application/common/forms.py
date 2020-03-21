"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField, BooleanField, validators)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)


class ContactForm(FlaskForm):
    """Contact form."""

    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    body = TextAreaField('Message', [
        DataRequired(),
        Length(min=4, message='Your message is too short.')])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Sign In form."""
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
    ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
