from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter(object):

    #Define initialization
    def __init__(self):

        # Connection Variables
        USER = 'accUser'
        PASS = 'OMG123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32182
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        try:
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("Connected successfully to MongoDB")
        except errors.ConnectionError as e:
                print(f"Could not connect to MongoDB: {e}")

            
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                #inserts data and returns true.
                self.collection.insert_one(data)
                return True
            #exception that returns false when error occures during insert.
            except errors.PyMongoError as e:
                print(f"An error occurred while inserting data: {e}")
                return False
                    
        else:
            raise ValueError("Data parameter is empty")
                
    def read(self,query):
        if query is not None:
                try:
                    #Lists the serch of the collection returns true
                    documents = list(self.collection.find(query))
                    return documents
                #Returns falls when there is an error.
                except errors.PyMongoError as e:
                     print(f"An error occurred while reading data: {e}")
                return[]
        #Error for empty query.
        else:
            raise ValueError("Query parameter is empty")
            
    def update(self, query, update_data):
        try:
            #sets update to all in a query returns number updated
            updated_count = self.collection.update_many(query, update_data)
            return updated_count.modified_count
        #error updating
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0

    def delete(self, query):
        try:
            #sets delete to all in specific query returns number deleted
            deleted_count = self.collection.delete_many(query)
            return deleted_count.deleted_count
        #error deleting
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0
            