import pymongo

url = 'mongodb+srv://dbUser:visualsync@opera.oup2ihx.mongodb.net/'
client = pymongo.MongoClient(url)

db = client['mongo_opera']