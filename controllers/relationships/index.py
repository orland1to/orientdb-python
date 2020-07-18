from database_config import client
import json

def createRelationship(req):
    result = client.command(
        "create edge relationships from "+
            req["input"]["from"]+ " TO "+ req["input"]["to"]+ " SET relationship = "+"\""+ req["input"]["relationship"] +"\""
        
        )
    for item in result:
            return json.dumps(item.__dict__)
