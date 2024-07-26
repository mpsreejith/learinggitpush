import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://sreejithmp007:anandam007@cluster0.x9rrkbe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client['mongotest']

collection=db['learningDay1']

document={
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Elm St",
        "city": "Somewhere",
        "state": "CA",
        "zip": "90210"
    }
}

result=collection.insert_one(document)

print(result.inserted_id)