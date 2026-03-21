import requests

def obtener_nombres():
    nombres = []

    while True:
        nombre = input("Escribe el nombre de deseas buscar (Enter para terminar): ")

        if not nombre.strip(): #Para cerrar el input con enter, vacío cierro el while y avanzo, el .strip() es para quitar los posibles espacios del user
            break
        nombres.append(nombre) #Agrega cada nombre a la lista
    return nombres

def consultar_api(nombre):
    try:
        respuesta = requests.get(f"https://api.agify.io/?name={nombre}")
    except:
        print("Error de conexión") #Para que no crashee por si perdemos conexión
        return None    
# Estos None, son los que regresan por si falla algo y se van directo al MAIN cuando los llaman en 
    if respuesta.status_code != 200:
        print(f"Error al consultar API, error: {respuesta.status_code}")
        return None

    return respuesta.json()

def mostrar_resultado(data):
    #inicializamos variables con la obtención de los datos del JSON (.get)
    cuenta = data.get('count', 0) #Inicializo en 0, si la clave 'count' no existe, usa 0 en lugar de dar error.
    nombre_api = data.get('name') or 'Desconocido'
    edad = data.get('age')

    print(f"No. de cuenta: {cuenta}")
    print(f"Nombre del cliente: {nombre_api.capitalize()}")

    if edad is None:
        print("Edad no disponible")
    else:
        print(f"Edad del cliente: {edad}")

def main():
    nombres = obtener_nombres()
    print()

    if not nombres: #Si no hay nombres en la lista manda mensaje de despedida
        print("No introdujo nombres, hasta la próxima.")
        return #sale de main() inmediatamente, hasta aquí llega el programa

    for i, name in enumerate(nombres): #recorre todos los nombres
        data = consultar_api(name) #recibe datos JSON

        if data: #if data = False, NO entra al bloque, ese "if data:" evalua si es True or False
    #si no hubo error → muestra resultados / solo si tengo datos válidos, continúa
            mostrar_resultado(data)

        if i < len(nombres) - 1: #Para dividir por bloques, menos el último
            print("-" * 30)

#Ejecutar el programa
main()

"""
main()
  ↓
obtener_nombres()
  ↓
loop nombres:
    consultar_api()
    mostrar_resultado()
"""
