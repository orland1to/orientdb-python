from pyorient import OrientDB
import pyorient
from socket_config import Socket
import db_atributes
socket = Socket("orientDB", 2424)
try:
    socket.connect()
    client = OrientDB(socket)
    session_id = client.connect("root", "password")
    client.db_open("test", "root", "password")
    for item in db_atributes.orient_classes():
            print("CREATE CLASS " + item['name'] + " IF NOT EXISTS EXTENDS "+item['classType'])
            client.command(
                "CREATE CLASS " + item['name'] + " IF NOT EXISTS EXTENDS "+item['classType']
            )
            for prop in item['atributes'] :
                client.command("CREATE PROPERTY " + item['name']  + "." + prop['name'] + " IF NOT EXISTS " + prop['types']
            )
except Exception as e:
    print(e)
    if not client.db_exists("test"):
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
