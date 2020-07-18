from flask import Flask, jsonify,request
from inspect import getmembers
import json,pickle
from database_config import client
import controllers.users.index as users
import controllers.relationships.index as relationships
app = Flask(__name__)
app.config['TESTING'] = True
@app.route('/users/', methods=['GET'])
def root():
    result = users.getUsers()       
    return jsonify({'status': 200,"result":result})

@app.route('/user/', methods=['POST','PUT','GET','DELETE'])
def User():
    req_json = request.get_json(force=True)
    result=None
    if request.method == 'POST':
        result = users.createUser(req_json)
    else:
        if  request.method == 'PUT':     
            result = users.updateUser(req_json) 
        else:
           if request.method == 'GET':
               result = users.getUser(req_json) 
           else:
               if request.method == 'DELETE':
                   result = users.deleteUser(req_json)

    return jsonify({'status': 200,"result":result})
@app.route('/relationship/', methods=['POST','PUT','GET','DELETE'])
def relationship():
    req_json = request.get_json(force=True)
    result=None
    if request.method == 'POST':
        result = relationships.createRelationship(req_json)

    return jsonify({'status': 200,"result":result})



@app.errorhandler(404)
def notFound(error=None):
    return jsonify({'status': 404})
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)