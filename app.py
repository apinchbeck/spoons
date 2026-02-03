"""
Main entry point for the Spoons app.

Sets up the Flask application, registers blueprints, and initializes extensions (e.g., database).
"""

from flask import Flask
from config import Config
from models import db
from routes.main import main_bp

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints (modular route structure)
    app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
    # Run the app in development mode
    app = create_app()
    app.run(debug=True)

