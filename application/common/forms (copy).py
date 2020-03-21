from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, SubmitField, PasswordField, TextAreaField, BooleanField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length)


class RegisterForm(FlaskForm):
    """Sign up for a user account."""
    email = StringField('Email',
                        validators=[Length(min=8, message='Please enter a valid email address.'),
                                    Email(message='Please enter a valid email address.'),
                                    DataRequired(message='Please enter a valid email address.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=8, message='Please select a stronger password.')])
    confirm = PasswordField('Repeat Password', [
        EqualTo('password', message='Passwords must match.'), DataRequired()])
    remember_me = BooleanField('Remember Me')
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')


class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message='Not a valid email address.'), DataRequired()])
    body = TextAreaField('Message', [DataRequired(),
                                     Length(min=10, max=150,
                                            message='Message should be between 10 and 150 characters')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Contact')


class LoginForm(FlaskForm):
    """Sign In form."""
    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                             Email('Please enter a valid email address.')])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=8, message='Password Incorrect.')])
    remember_me = BooleanField('Remember Me')
    recaptcha = RecaptchaField()
    submit = SubmitField('Log In')
