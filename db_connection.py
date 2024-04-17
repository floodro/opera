import pymongo

url = 'mongodb+srv://dbUser:visualsync@opera.oup2ihx.mongodb.net/'
#offline_url = 'mongodb://localhost:27017'

client = pymongo.MongoClient(url)

db = client['mongo_opera']