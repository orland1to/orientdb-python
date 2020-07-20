#Links vs Edges: If you don't have properties on your arch you can use a link, instead if you have it use edges.
#define clases that usually represents a basic type of record
#usually extends from Vertex "V" or EDGE "E"
#EDGE is a conexion betwen vertexs
#alternativally you can use link if you dont need any attibute in the conexion


#define the classes in database
# it is an array of 
#name
#type    ---most common are E or V for ede or vetex 
#atributes --array of attrributes  with name and type 
def orient_classes():
    return[
        {
            "name":"users",
            "classType":"V",
            "atributes":[
                {
                    "name":"name",
                    "types":"String"
                    }
                    ]
        },
        {
            "name":"companies",
            "classType":"V",
            "atributes":[
                {"name":"name",
                "types":"String"
                }]
        },
        {
            "name":"relationships",
            "classType":"E",
            "atributes":
            [
                {
                    "name":"relationship",
                    "types":"String"
                    }
            ]
        },
        {
            "name":"files",
            "classType":"V",
            "atributes":[
                {
                    "name":"filename",
                    "types":"STRING"
                },
                {
                    "name":"binary",
                    "types":"BINARY"
                },
                {
                    "name":"mimetype",
                    "types":"STRING"
                }
            ]
        }
    ]