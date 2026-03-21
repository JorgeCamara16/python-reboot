#Mini proyecto (Asistente tipo IA)
import requests
import json
import os #Para la creación de rutas/carpetas y evitar fallos de guardado

def conectar_api(nombre):
    try:
        response = requests.get(f"https://api.agify.io/?name={nombre}")
    except:
        print("Error de conexión") #Para que no crashee por si perdemos conexión
        return None    

    if response.status_code != 200:
        print(f"Error al consultar API, error: {response.status_code}")
        return None

    return response.json() #Desde aquí, el JSON ya es convertido dict


def crear_user(data): #Creación diccionario controlado
    return {
        "nombre": data.get("name") or "Desconocido",
        "edad": data.get("age"),
        "count": data.get("count", 0)
    }

def mostrar_usuario(user):
    print("-" * 30)
    print(f"Bot: No. de cuenta del usuario: {user['count']}")
    if user["edad"] is None:
        print("Bot: Edad no disponible")
    else:
        print(f"Bot: Edad del usuario: {user['edad']}")
    print("-" * 30)

def guardar_historial(historial):
    os.makedirs("data", exist_ok=True)
    with open("data/historial.json", "w") as f:
        json.dump(historial, f, indent=4)

def cargar_historial():
    try:
        with open("data/historial.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError: #asume los errores con el archivo JSON
        print("Bot: Archivo corrupto, reiniciando...")

        with open("data/historial.json", "w") as f:
            json.dump([], f) #Repara el archivo de historial desde 0

    return []

def asistente():
    #Ahora vamos a ponerle memoria al asistente y que guarde/cargue historial
    historial = cargar_historial()

    print("Bot: Hola, escribe un nombre, 'historial' para ver consultas realizadas o 'salir' para terminar.")

    while True:
        nombre_input = input("Usuario: ")
                                        #Este if es super importante, lee el input y si después de quitar los espacios no hay nada el boot pide de nuevo el usuario a buscar. WOW. 
                                        # Es igual a if nombre.strip() == "":
        if not nombre_input.strip(): #“si después de quitar espacios no queda nada…”
            continue #"salta esta iteración y vuelve al inicio del loop"

        entrada = nombre_input.strip().lower() #lower para que esté siempre en minúsculas

        if entrada == "salir": 
            print("Bot: Hasta luego :)")
            break
        
        if entrada == "historial":
            if not historial:
                print("Bot: No hay historial aún")           
            else:
                print("-" * 30)
                for user in historial: 
                    edad = user["edad"] if user["edad"] is not None else "No disponible" #se valida si está disponible la edad user
                    print(f"- {user['nombre'].capitalize()} ({edad})")
                print("-" * 30)
            continue    

        print("Bot: Perfecto dame un momento...")

        data = conectar_api(nombre_input)

        if data:
            usuario = crear_user(data)
            historial.append(usuario)
            guardar_historial(historial)
            mostrar_usuario(usuario)

asistente()