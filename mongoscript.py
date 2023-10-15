from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://test:test12345678!!@cluster0.gncytiu.mongodb.net/")

db = client.scrapy

posts = db.test_collection

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = posts.insert_one(post).inserted_id