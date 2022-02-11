import pymongo
from bson import ObjectId

db_name = "term_project_db"
db_connection = pymongo.MongoClient("mongodb://localhost:27017/")


def insertData(collection_name, colldata):
    try:
        mydb = db_connection[db_name]
        mycol = mydb[collection_name]
        mycol.insert_one(colldata)
        print('data inserted into collection')
    except:
        print('data not inserted')


def get_data(collection_name, query):
    try:
        mydb = db_connection[db_name]
        mycol = mydb[collection_name]
        data = mycol.find(query)
        if mycol.find(query).count() == 0:
            return {'data': data, 'check': False}
        else:
            return {'data': data, 'check': True}
        print('data retrieved')
    except:
        print('data not retrieved')


def get_data_byID(collection_name, id_num):
    try:
        mydb = db_connection[db_name]
        mycol = mydb[collection_name]
        data = mycol.find_one({"_id": ObjectId(str(id_num))})
        print('data retrieved')
        return data
    except:
        print('data not retrieved')


def update_data(collection_name, data_coll, query):
    try:
        mydb = db_connection[db_name]
        mycol = mydb[collection_name]
        myquery = {"_id": query}
        newvalues = {"$set": data_coll}
        mycol.update_one(myquery, newvalues)
        print('collection updated')
    except:
        print('collection not updated')


def delete_data(collection_name, query):
    try:
        mydb = db_connection[db_name]
        mycol = mydb[collection_name]
        mycol.delete_one(query)
        print('data deleted from collection')
    except:
        print('data not deleted from collection')
