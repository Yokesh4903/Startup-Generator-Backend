import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY")

    # JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # SQLite (Optional - can keep for now)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MongoDB Atlas
    MONGODB_URI = os.getenv("MONGODB_URI")

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")