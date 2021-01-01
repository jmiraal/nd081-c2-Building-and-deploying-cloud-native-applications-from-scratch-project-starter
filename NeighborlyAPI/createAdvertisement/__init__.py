import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://neighborlymongodbjmira:RdG7p7bwK0X2nCrPJeIErucJTVgxMWTg5gPxbpbf6oslgMowInzb3qFkn3tUMcyibldZVMsbqW3myYvDuL8HnA==@neighborlymongodbjmira.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"  
            client = pymongo.MongoClient(url)
            database = client['azure']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )