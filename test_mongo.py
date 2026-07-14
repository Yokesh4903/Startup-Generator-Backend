from pymongo import MongoClient

uri = "mongodb+srv://startupadmin:Startup12345@cluster0.tnavx6z.mongodb.net/startup?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

print(client.admin.command("ping"))