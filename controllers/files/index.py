from database_config import client
import json, base64,io
from flask import send_file
#save a file with name and mimetype in to db, actually does it in base64 so the space in disk is 130% of initial value
def createFile(req):
    file=req.files['file']
    mimetype = file.content_type
    filename =file.filename
    f = file.read()
    f=base64.b64encode(f).decode('ascii')
    result = client.command(
        "INSERT INTO files"
        "(binary,name,mimetype)"
        "VALUES('%s','%s','%s')"
         %(
            f,
            filename,
            mimetype,
        )
        )
    resultArr=[]
    for item in result:
        if "binary" in item.__dict__["_OrientRecord__o_storage"]:#delete the file from result to return to client
            del item.__dict__["_OrientRecord__o_storage"]["binary"]
        resultArr.append(item.__dict__)
    return json.dumps(resultArr)
#return a file from db by id
def getFile(req):
    req_json = req.get_json(force=True)
    return client.record_load(req_json["input"]["rid"],'*:3')
   