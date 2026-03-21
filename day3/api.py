#Configuración primera API

from flask import Flask #instanciarlo

app = Flask(__name__) # crea tu servidor web

@app.route("/") # defines una ruta (endpoint)
def home(): # qué responde esa ruta
    return "API funcionando 🔥"

@app.route("/usuario/<nombre>")
def obtener_usuario(nombre):
    return f"Buscando usuario: {nombre}"

if __name__ == "__main__":
    app.run(debug=True) #inicia el servidor
