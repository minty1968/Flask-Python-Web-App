"""Routes for conversion pages."""
from flask import render_template, Blueprint

convert_bp = Blueprint('convert', __name__, template_folder='application/templates/convert/',
                       static_folder='static',
                       url_prefix='/admin')


@convert_bp.route('/convert/distance', methods=('GET', 'POST'))
def measurement():
    """Measurement route."""

    return render_template('convert/measurement.html',
                           title='Sharpe Digital Solution | Measurement Conversion',
                           template='convert-template main',
                           body="Measurement")


@convert_bp.route('/convert/temps', methods=('GET', 'POST'))
def temps():
    """Temperature route."""

    return render_template('convert/temps.html',
                           title='Sharpe Digital Solution | Temperature Conversion',
                           template='convert-template main',
                           body="Temperature")


@convert_bp.route('/convert/weights', methods=('GET', 'POST'))
def weights():
    """Weights route."""

    return render_template('convert/weights.html',
                           title='Sharpe Digital Solution | Weight Conversion',
                           template='convert-template main',
                           body="Weight")
