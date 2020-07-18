from database_config import client
import json
def getUser(req):
    #return the content of input.id can be anything valid record
    result = client.command(
        "SELECT  FROM "+req["input"]["id"] 
        )
    response = []
    for item in result:
            response.append(json.dumps(item.__dict__))
    return response
def createUser(req):
    result = client.command(
        "INSERT INTO users"
        "(name)"
        "VALUES('%s')"
        % (
            req["input"]["name"]
        )
        )
    for item in result:
            return json.dumps(item.__dict__)
def getUsers():
    result = client.command(
        "SELECT  FROM users"
        )
    response = []
    for item in result:
            response.append(json.dumps(item.__dict__))
    return response
def updateUser(req):
    result = client.command(
        "UPDATE "+ req["input"]["id"]+
        " SET name = " + "\""+req["input"]["name"]+"\""+ " RETURN AFTER "
        )
    for item in result:
            return json.dumps(item.__dict__)

def deleteUser(req):
    #delete the content of input.id can be anything valid vertex
    result = client.command(
        "DELETE vertex "
        + req["input"]["id"])
    return result