from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

print("Mongo URI:", mongo_uri)

client = MongoClient(
    mongo_uri,
    tls=True,
    tlsAllowInvalidCertificates=False,
    serverSelectionTimeoutMS=10000,
)

client.admin.command("ping")

db = client["startup"]

users = db["users"]
history = db["history"]