import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://neighborlymongodbjmira:RdG7p7bwK0X2nCrPJeIErucJTVgxMWTg5gPxbpbf6oslgMowInzb3qFkn3tUMcyibldZVMsbqW3myYvDuL8HnA==@neighborlymongodbjmira.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"  
        client = pymongo.MongoClient(url)
        database = client['neighborlydbjmira']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)