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
#Encoder
json_data = json.JSONEncoder().encode({"Lenguages": ["Python", "JavaScript"]})
print(json_data)
print(type(json_data))

#Decoder
python_dict = json.JSONDecoder().decode(json_data)

print(python_dict)
print(type(python_dict))

### Queda pendiente documentar la parte avanzada de la clase especializada para futuras referencias, video en Youtube