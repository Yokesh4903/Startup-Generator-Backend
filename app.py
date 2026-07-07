from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from database import db

from routes.auth import auth_bp
from routes.startup import startup_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize JWT
    JWTManager(app)

    # Initialize Database
    db.init_app(app)

    # Register Authentication Routes
    app.register_blueprint(auth_bp)
    app.register_blueprint(startup_bp)

    # Home Route
    @app.route("/")
    def home():
        return {
            "message": "🚀 Multi-Agent Startup Simulator API Running",
            "status": "success"
        }

    # Create Database Tables
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )