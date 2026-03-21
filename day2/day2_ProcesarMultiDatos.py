#Manejo de multidatos
import requests

def pedir_nombres():
    
    nombres = []
    while True:
        nombre = input("Introduce el nombre que buscas (enter para terminar): ")
        if not nombre.strip():
            break
        nombres.append(nombre)
    return nombres
             

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

def mostrar_usuarios(resultados): #función para imprimir acomodado el diccionario
    for i, usuario in enumerate(resultados):
        print(f"Nombre: {usuario['nombre'].capitalize()}")

        if usuario["edad"] is None:
            print("Edad: No disponible")
        else:
            print(f"Edad: {usuario['edad']}")

        print(f"Count: {usuario['count']}")

        if i < len(resultados) - 1:
            print("-" * 30)

def main():
    names = pedir_nombres()
    print()

    if not names:
        print("No introdujo nombres, hasta la próxima")
        return

    resultados = []

    for name in names:
        data = conectar_api(name)

        if data: 
            usuario = crear_user(data)
            resultados.append(usuario)

    mostrar_usuarios(resultados)


main()