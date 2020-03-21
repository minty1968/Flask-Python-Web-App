"""Routes for blog pages."""
from flask import Blueprint, render_template


# Blueprint Configuration
blog_bp = Blueprint('blog', __name__,
                    template_folder='templates',
                    static_folder='static')


@blog_bp.route('/blog', methods=['GET'])
def blog():
    """Blog route."""
    return render_template('index.html',
                           title='Sharpe Digital Solutions | Movie Blog',
                           template='blog-template main',
                           body="Movie Blog")
