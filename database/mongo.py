from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

print("========== MONGO DEBUG ==========")
print("Mongo URI:", mongo_uri)
print("=================================")

if not mongo_uri:
    raise RuntimeError("MONGODB_URI environment variable is not set.")

client = MongoClient(
    mongo_uri,
    serverSelectionTimeoutMS=5000
)

# Test the connection immediately
client.admin.command("ping")

db = client["startup"]

users = db["users"]

history = db["history"]