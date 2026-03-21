# ejecuta el asistente

from services import conectar_api, crear_user
from storage import cargar_historial, guardar_historial

def mostrar_usuario(user):
    print("-" * 30)
    print(f"Bot: No. de cuenta del usuario: {user['count']}")

    edad = user["edad"] if user["edad"] is not None else "No disponible"
    print(f"Bot: Edad del usuario: {edad}")

    print("-" * 30)


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

if __name__ == "__main__":
    asistente()
