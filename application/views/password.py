"""Routes for blog pages."""
from flask import Blueprint, render_template

# Blueprint Configuration
password_bp = Blueprint('password', __name__,
                        template_folder='application/templates/password/',
                        static_folder='static')


@password_bp.route('/password/random', methods=['GET'])
def random():
    """Password Random Characters route."""

    return render_template('password/random.html',
                           title='Sharpe Digital Solutions | Random Character Password Generator',
                           template='blog-template main',
                           body="Random Character Password Generator")


@password_bp.route('/password/words', methods=['GET'])
def words():
    """Password Random Words route."""

    return render_template('password/words.html',
                           title='Sharpe Digital Solutions | Random Words Password Generator',
                           template='blog-template main',
                           body="Random Words Password Generator")
