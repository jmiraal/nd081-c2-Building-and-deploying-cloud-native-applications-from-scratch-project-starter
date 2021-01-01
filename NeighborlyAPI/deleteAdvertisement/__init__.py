import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborlymongodbjmira:RdG7p7bwK0X2nCrPJeIErucJTVgxMWTg5gPxbpbf6oslgMowInzb3qFkn3tUMcyibldZVMsbqW3myYvDuL8HnA==@neighborlymongodbjmira.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"  
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
