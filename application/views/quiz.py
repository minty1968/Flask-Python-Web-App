"""Routes for Quiz pages."""
from flask import Blueprint, render_template
from flask_login import login_required


# Blueprint Configuration
quiz_bp = Blueprint('quiz', __name__,
                    template_folder='templates',
                    static_folder='static')


@quiz_bp.route('/quiz/lpic1', methods=['GET'])
def lpic1():
    """LPIC-1 Quiz route."""
    return render_template('index.html',
                           title='Sharpe Digital Solutions | LPIC-1 Quiz',
                           template='quiz-template main',
                           body="LPIC-1 Quiz")


@quiz_bp.route('/quiz/lpic1', methods=['GET'])
def lpic2():
    """LPIC-2 Quiz route."""
    return render_template('index.html',
                           title='Sharpe Digital Solutions | LPIC-2 Quiz',
                           template='quiz-template main',
                           body="LPIC-2 Quiz")


@quiz_bp.route('/quiz/lpic3', methods=['GET'])
def lpic3():
    """LPIC-3 Quiz route."""
    return render_template('index.html',
                           title='Sharpe Digital Solutions | LPIC-3 Quiz',
                           template='quiz-template main',
                           body="LPIC-3 Quiz")
