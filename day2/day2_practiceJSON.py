import json
#Ejercicio 1
"""
data = '{"nombre": "George", "edad": 25}'

obj = json.loads(data) #loads para poder cargar desde JSON un diccionario de Python

print(obj["nombre"]) 
"""

#Ejercicio 2
#Convierte esto a JSON, diccionario a JSON, usando la función dumps:
"""
usuario = {
    "nombre": "George",
    "edad": 25
}
jsonnew = json.dumps(usuario) #dumps para apartir de un diccionario de Python crear un objeto de JSON
print(jsonnew)
"""

#Ejercicio 3
"""
perfil_valo = {
    "Nombre": "Jorge Camara",
    "Edad": 24,
    "NickName": "TheKingJorge16",
    "Rango": "Platino",
    "Agentes": ["Clove", "Reyna", "Jett", "Astra", "Yoru"]
}

#json_pvalo = json.dumps(perfil_valo, indent=4, separators=(", ", ": "))
#ident sirve para los espacios que quiero que deje el código al imprimirse

json_pvalo = json.dumps(perfil_valo, indent=4, separators=(", ", ": "), sort_keys=True)
#sort_keys para acomodar alfabéticamente las keys al imprimirlas
print(json_pvalo)
print(type(json_pvalo)) #para verificar que sea un objeto JSON, son string (str)
"""
#Usando los codificadores de JSON
"""
#Encoder, pasar diccionarios a JSON
json_data = json.JSONEncoder().encode({"Lenguages": ["Python", "JavaScript"]})
print(json_data)
print(type(json_data))

#Decoder, pasar JSON a diccionarios
python_dict = json.JSONDecoder().decode(json_data)

print(python_dict)
print(type(python_dict))
"""

#Parte avanzada POO - Trabajar JSON en una clase personalizada, convertir la instancia de una clase personalizada en un objeto JSON

class Curso():

    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

curso_1 = Curso("4567", "Programacion", 4)
print(curso_1) #Vemos que se ha creado la instancia del objeto JSON
json_object_data = json.dumps(curso_1.__dict__) #Creamos el objeto JSON
print(json_object_data) 
print(type(json_object_data))
python_dicc = json.loads(json_object_data) #Transformamos el JSON a Dict Python
print(python_dicc)
print(type(python_dicc))

