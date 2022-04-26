import motor.motor_asyncio
from fastapi_users.db import MongoDBUserDatabase
from .models import UserDB

# 引入密碼
path = "mongodb_password"
with open(path) as f:
    word = f.readline().split(',')
    account = word[0]
    password = word[1]

# mongodb connection
DATABASE_URL = f"mongodb+srv://{account}:{password}@getdata.dzc20.mongodb.net/getdata?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL, uuidRepresentation="standard")
db = client.getdata
collection = db.users


async def get_user_db():
    yield MongoDBUserDatabase(UserDB, collection)
