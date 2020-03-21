"""Routes for logged-in account pages."""
from flask import Blueprint, render_template

# Blueprint Configuration
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Admin dashboard route."""
    return render_template('admin/dashboard.html',
                           title='Flask-Blueprint Tutorial | Admin Dashboard',
                           template='dashboard-template account',
                           body="Account")
