"""Routes for main pages."""
from flask import Blueprint, render_template


# Blueprint Configuration
main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template('main/home.html')


@main_bp.route('/about', methods=['GET'])
def about():
    """About page route."""
    return render_template('main/about.html',
                           title='Flask-Blueprint Tutorial | About',
                           template='about-template main',
                           body='About')


