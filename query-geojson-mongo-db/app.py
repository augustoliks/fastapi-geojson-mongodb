from pymongo import MongoClient

mongo = MongoClient(
    '127.0.0.1',
    27017,
    username='admin',
    password='senha@123'
)
db = mongo['test_database']
db['testcol'].insert_one({'1': '2'})
