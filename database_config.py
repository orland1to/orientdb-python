from pyorient import OrientDB
import pyorient
from socket_config import Socket
import db_atributes
socket = Socket("orientDB", 2424)
try:
    print("here")
    socket.connect()
    client = OrientDB(socket)
    session_id = client.connect("root", "password")#get session id
    client.db_open("test", "root", "password") #open db
    for item in db_atributes.orient_classes():  #create a classes and atributes of new class if not exists based on db atributes file
            client.command(
                "CREATE CLASS " + item['name'] + " IF NOT EXISTS EXTENDS "+item['classType']
            )
            for prop in item['atributes'] :
                client.command("CREATE PROPERTY " + item['name']  + "." + prop['name'] + " IF NOT EXISTS " + prop['types']
            )
except Exception as e:
    print(e)
    socket.connect()
    client = OrientDB(socket)
    session_id = client.connect("root", "password")#get session id
    if not client.db_exists("test"):#if exeption is for non created db  lets create the db and classes with atributes based on db_atributes file
        client.db_create(
        "test",
        pyorient.DB_TYPE_GRAPH,
        pyorient.STORAGE_TYPE_PLOCAL)
        client.db_open("test", "root", "password")
    for item in db_atributes.orient_classes():
            client.command(
                "CREATE CLASS " + item['name'] + " IF NOT EXISTS EXTENDS "+item['classType']
            )
            for prop in item['atributes'] :
                client.command("CREATE PROPERTY " + item['name']  + "." + prop['name'] + " IF NOT EXISTS " + prop['types']
            )
