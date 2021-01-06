import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://neighborlymongodbjmira:93e6tfk4JvB4yqrb1T509j9W3AOR3HmylzteSqgd2JSAVzdCqRtbHq6uyOSjryvwbZDEQoATJgCttZBFSEznFg==@neighborlymongodbjmira.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"  
        client = pymongo.MongoClient(url)
        database = client['neighborlydbjmira']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)