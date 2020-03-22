"""App configuration."""
from os import environ


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')

    # DB Info
    MONGO_URI = environ.get('MONGO_URI')

    # ReCaptcha Info
    RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUB')
    RECAPTCHA_PARAMETERS = {'size': '100%'}
