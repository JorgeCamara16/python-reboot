#lógica (API + transformación)
import requests
import json 

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
