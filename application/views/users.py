from flask import render_template, url_for, redirect, request, Blueprint, flash, session
from application.common.forms import ContactForm, LoginForm, RegisterForm
from flask_login import login_required, logout_user, current_user
from application.models.users import User
from .. import login_manager


# Set up a Blueprint
users_bp = Blueprint('users', __name__,
                     template_folder='application/templates/users/',
                     static_folder='application/static')


@users_bp.route('/forms/contact', methods=('GET', 'POST'))
@login_required
def contact():
    """ Contact Form route."""
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        return redirect(url_for('success'), code=200)
    return render_template('users/contact.html',
                           title='Sharpe Digital Solutions | Contact Form',
                           template='form-template contact',
                           body="Contact Form",
                           form=contact_form)


@users_bp.route('/forms/register', methods=('GET', 'POST'))
def register_user():
    """ Registration Form route."""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # Get Form Fields
        email = request.form.get('email')
        password = request.form.get('password')
        # Validate Login Attempt
        existing_user = User.get_by_email(email=email)
        print(existing_user)
        if existing_user is None:
            print('Signing up now')
            User.signup_user(email, password)
            session['email'] = email
            return render_template('users/profile.html', email=session['email'])
        else:
            flash('A user already exists with that email address.')
            return redirect(url_for('users.login_user'))
    # GET: Serve Log-in page
    return render_template('users/register.html',
                           title='Sharpe Digital Solutions | Registration Form',
                           template='form-template register',
                           body="Registration Form",
                           form=form)


@users_bp.route('/forms/login', methods=('GET', 'POST'))
def login_user():
    """ Login Form route."""
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # Get Form Fields
        email = request.form.get('email')
        password = request.form.get('password')
        # Validate Login Attempt
        if User.is_login_valid(email, password):
            User.login_user(email)
            return render_template('users/profile.html', email=session['email'])
    # GET: Serve Log-in page
    return render_template('users/login.html',
                           title='Sharpe Digital Solutions | Login Form',
                           template='form-template login',
                           body="Please Login",
                           form=form)


@users_bp.route('/users/profile', methods=('GET', 'POST'))
def profile():
    return render_template('users/profile.html',
                           title='Sharpe Digital Solutions | User Profile',
                           template='success-template',
                           body="Profile Page")


@users_bp.route('/success', methods=('GET', 'POST'))
@login_required
def success():
    return render_template('success.html',
                           template='success-template')


@users_bp.route("/users/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('main.home'))


@login_manager.user_loader
def load_user(id):
    """Check if user is logged-in on every page load."""
    if id is not None:
        return User.get_by_id(int(id))
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('users.login_user'))