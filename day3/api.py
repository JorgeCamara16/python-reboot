#Configuración primera API
# 4 métodos principales a usar en las APIs
"""
GET ----> Obtener información
POST ---> Crear información
PUT ----> Actualizar información
DELETE -> Borrar información
"""
from services import conectar_api, crear_user #Importar la lógica
from storage import cargar_historial, guardar_historial #Importar persistencia
from flask import Flask #instanciarlo

app = Flask(__name__) # crea tu servidor web

@app.route("/") # defines una ruta (endpoint)
def home(): # qué responde esa ruta
    return "API funcionando 🔥"

"""
@app.route("/usuario/<nombre>") #Flask captura lo que escribes en la URL
def obtener_usuario(nombre): #ese valor llega como variable
    return f"Buscando usuario: {nombre}"
#Funcionamiento del módulo: si alguien entra a /usuario/lo_que_sea → lo recibo como variable y lo devuelvo como mensaje.
"""

#Función: Cada vez que me consultan, guardo la información, es como mi MAIN
@app.route("/usuario/<nombre>")
def obtener_usuario(nombre):
    data = conectar_api(nombre)

    if data is None:
        return {"error": "No se pudo obtener datos"}

    if not isinstance(data, dict):
        return {"error": "Respuesta inválida"}

    usuario = crear_user(data)

    #Módulo para guardar la información
    historial = cargar_historial()
    historial.append(usuario)
    guardar_historial(historial)

    return usuario

#Función mostrar el historial de lo pedido
@app.route("/historial")
def ver_historial():
    historial = cargar_historial()

    return historial

if __name__ == "__main__":
    app.run(debug=True) #inicia el servidor
