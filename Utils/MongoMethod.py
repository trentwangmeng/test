
import pymongo


uri = "mongodb://127.0.0.1:27017"


def connect_mongo(db, table):
    connection = pymongo.MongoClient(uri)
    col = connection[db][table]
    return col


if __name__ == '__main__':
    db = "test"
    table = "test_table"
    mongo = connect_mongo(db,table)
    mongo.insert({"test":"t123"})




from Utils.MongoServer import connect_mongo

mongo = connect_mongo("AutoTest","YiXingApp")

mongo.insert({"name":name,"address":"上海市"})
