from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config

from routes.auth import auth_bp
from routes.startup import startup_bp


def create_app():

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize JWT
    JWTManager(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(startup_bp)

    @app.route("/")
    def home():

        return {

            "message": "🚀 Multi-Agent Startup Simulator API Running",

            "database": "MongoDB Atlas",

            "status": "success"

        }

    return app


app = create_app()

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )