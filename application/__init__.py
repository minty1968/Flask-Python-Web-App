"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from application.common.database import Database

login_manager = LoginManager()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    # Initialize Plugins
    Database.initialize()
    login_manager.init_app(app)

    # Application Configuration
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from application.views.admin import admin_bp
        from application.views.main import main_bp
        from application.views.blog import blog_bp
        from application.views.convert import convert_bp
        from application.views.lottery import lottery_bp
        from application.views.quiz import quiz_bp
        from application.views.password import password_bp
        from application.views.users import users_bp

        # Register Blueprints
        app.register_blueprint(admin_bp)
        app.register_blueprint(main_bp)
        app.register_blueprint(blog_bp)
        app.register_blueprint(convert_bp)
        app.register_blueprint(lottery_bp)
        app.register_blueprint(quiz_bp)
        app.register_blueprint(password_bp)
        app.register_blueprint(users_bp)
        return app
