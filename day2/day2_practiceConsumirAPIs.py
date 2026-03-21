# How to connect to an API using Python

import requests

"""
base_url = "https://pokeapi.co/api/v2/"

"""






#Ejercicio Primera API
#Estático
"""
import requests

respuesta = requests.get("https://api.agify.io/?name=george") #hace petición a internet, extrae información de la API

data = respuesta.json() # convierte respuesta a dict

#print(data)
#print(type(data))

#Dos maneras de obtener los datos, sacándolos como dict [] o usando el .get()

#print(f"Nombre del cliente: {data["name"].capitalize()}") #.capitalize() para poner en mayúscula la primera letra del name.
#print(f"Edad del cliente: {data["age"]} años")

# Opto por usar e implementar el get
print(f"Nombre: {data.get('name').capitalize()}")
print(f"Edad estimada: {data.get('age')}")
"""

#Dinámico
"""
nombre = input("Ingresa el nombre a buscar: ")
respuesta = requests.get(f"https://api.agify.io/?name={nombre}") #Ingresa en el request el nombre que deseamos buscar
data = respuesta.json()
print(f"Numero de cuenta: {data.get('count')}")
print(f"Nombre: {data.get('name').capitalize()}")
#if data.get('age') == "None": /// No se utiliza de esta manera porque lo que la API devuelve no es un string, es un valor especial None = tipo NoneType
if data.get('age') is None:
    print("Edad no disponible")
else:
    print(f"Edad estimada: {data.get('age')}")

"""
#Version mejorada del último código
"""
nombre = input("Ingresa el nombre a buscar: ")
respuesta = requests.get(f"https://api.agify.io/?name={nombre}")

if respuesta.status_code != 200:
    print(f"Error al consultar API, error: {respuesta.status_code}")
else:
   data = respuesta.json()

   #inicializamos variables con la obtención de los datos del JSON (.get)
   cuenta = data.get('count', 0) #Inicializo en 0, si la clave 'count' no existe, usa 0 en lugar de dar error.
   nombre = data.get('name') or 'Desconocido'
   edad = data.get('age')

   print(f"No. de cuenta: {cuenta}")
   print(f"Nombre del cliente: {nombre.capitalize()}")

   if edad is None:
      print("Edad no disponible")
   else:
      print(f"Edad del cliente: {edad}")
"""

#Version con varios nombres en input

nombres = []

while True:
    nombre = input("Escribe el nombre de deseas buscar (Enter para terminar): ")

    if not nombre.strip(): #Para cerrar el input con enter, vacío cierro el while y avanzo, el .strip() es para quitar los posibles espacios del user
        break
    nombres.append(nombre) #Agrega cada nombre a la lista
    
print() #Salto de línea para separar la terminal
#print(nombres)

if not nombres: #Si no hay nombres en la lista manda mensaje de despedida
    print("No introdujo nombres, hasta la próxima.")
else:
    for i, name in enumerate(nombres): # índice + valor al mismo tiempo
    # enumerate(nombres) significa: “recorre la lista y dime también en qué posición estás”
        try:
            respuesta = requests.get(f"https://api.agify.io/?name={name}")
        except:
            print("Error de conexión") #Para que no crashee por si perdemos conexión
            continue    

        if respuesta.status_code != 200:
            print(f"Error al consultar API, error: {respuesta.status_code}")
        else:
            data = respuesta.json()

            #inicializamos variables con la obtención de los datos del JSON (.get)
            cuenta = data.get('count', 0) #Inicializo en 0, si la clave 'count' no existe, usa 0 en lugar de dar error.
            nombre = data.get('name') or 'Desconocido'
            edad = data.get('age')

            print(f"No. de cuenta: {cuenta}")
            print(f"Nombre del cliente: {nombre.capitalize()}")

            if edad is None:
                print("Edad no disponible")
            else:
                print(f"Edad del cliente: {edad}")
            if i < len(nombres) - 1: #Para dividir por bloques, menos el último
                print("-" * 30)












