# guardar/cargar historial
import json
import os

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

