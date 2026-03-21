import requests
import json
import os

API_URL = "https://api.agify.io/"

def conectar_api(nombre):
    try:
        response = requests.get(API_URL, params={"name": nombre}, timeout=5) #Timeout evita que el programa se quede colgado
        response.raise_for_status()  # Lanza error si status != 200
        #Si status ≠ 200 → lanza excepción automáticamente, librería trabajando
    except requests.exceptions.RequestException as e: #Solo captura errores reales de red/API
        print(f"Bot: Error de conexión -> {e}")
        return None

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Bot: Error al interpretar la respuesta de la API")
        return None

    return data


def crear_user(data):
    return {
        "nombre": data.get("name") or "Desconocido",
        "edad": data.get("age"),
        "count": data.get("count", 0)
    }


def mostrar_usuario(user):
    print("-" * 30)
    print(f"Bot: No. de cuenta del usuario: {user['count']}")

    edad = user["edad"] if user["edad"] is not None else "No disponible"
    print(f"Bot: Edad del usuario: {edad}")

    print("-" * 30)


def guardar_historial(historial):
    os.makedirs("data", exist_ok=True)

    with open("data/historial.json", "w") as f:
        json.dump(historial, f, indent=4)


def cargar_historial():
    if not os.path.exists("data/historial.json"):
        return [] #Evita error al iniciar por primera vez

    try:
        with open("data/historial.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Bot: Archivo corrupto, reiniciando...")
        return []


def asistente():
    historial = cargar_historial()

    print("Bot: Hola, escribe un nombre, 'historial' o 'salir'.")

    while True:
        entrada = input("Usuario: ").strip()

        if not entrada:
            continue

        comando = entrada.lower()

        if comando == "salir":
            print("Bot: Hasta luego :)")
            break

        if comando == "historial":
            if not historial:
                print("Bot: No hay historial aún")
            else:
                print("-" * 30)
                for user in historial:
                    edad = user["edad"] if user["edad"] is not None else "No disponible"
                    print(f"- {user['nombre'].capitalize()} ({edad})")
                print("-" * 30)
            continue

        print("Bot: Consultando API...")

        data = conectar_api(entrada)

        # VALIDACIÓN MEJORADA
        #if data: No diferencia entre error y respuesta vacía
        if data is None: #Esto es EXACTO
            continue

        if not isinstance(data, dict): #Verificas que realmente sea JSON válido
            print("Bot: Respuesta inválida de la API")
            continue

        usuario = crear_user(data)

        historial.append(usuario)
        guardar_historial(historial)

        mostrar_usuario(usuario)


asistente() 
