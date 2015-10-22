from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

class DatabaseWriter:
    """DatabaseClient is used to interact with the database for simple
    operation which allow environments to be created and queried
    """

    def __init__(self,collection,uri='mongodb://localhost:27017/turing_development'):
        """Access the environments collection from the mongodb client
        for access in database manipulation
        """

        client = MongoClient(uri,
                             connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             socketKeepAlive=True)

        db = client.get_default_database()
        self.collection = db[collection]


    def create(self,entry):
        """Create an entry in the collection
        """

        return self.collection.insert_one(entry)

    def update(self,query,entry):
        """Update the item with the given entry which matches the
        provided query
        """

        updated = self.collection.find_one_and_update(
            query,
            {'$set' : entry },
            return_document=ReturnDocument.AFTER
            )

        return updated

    def query(self):
        """Find a list of the items in the collection
        """

        return self.collection.find({})

if (__name__ == "__main__"):
    databaseWriter = DatabaseWriter('projects')

    for project in databaseWriter.query():
        print(project['title'])

    databaseWriter.update({'title':'Flappy Parrot'},{'link':'LINKEY'})

    for project in databaseWriter.query():
        print(project.get('link',''))