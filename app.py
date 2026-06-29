from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

history = """
Título: Tu primer caso como detective.

Era una noche oscura y tormentosa. La lluvia golpeaba con fuerza las ventanas de la oficina del detective. De repente, el teléfono sonó, interrumpiendo el silencio. Al otro lado de la línea, una voz temblorosa pedía ayuda.
El detective acudió al bloque de pisos que le indicaban. Al llegar encontró una pequeño piso compuesto de una sala, un dormitorio, un salón principal y el comedor.
Cuando llegó se encontró que Alejandro estaba delante de la ventana.
Beatriz estaba en el salón.
Carolina estaba sobre la alfombra.
Dante estaba sobre la cama.
Elisabeth estaba junto a la planta.
Y Vicente era la victima estaba en la última casiilla libre. Ayuda al detective a esclarecer los hechos porque un sospechoso lo noqueó y no se acuerda de nada. ¡Espero que tengas más suerte!
(recuerda que los personajes no pueden estar en la casilla de una mesa o planta, pero si en una alfombra o en una cama).
"""

#objetos del tablero 
elementos = {
#sala
(1,2): "ventana",
#dormitorio
(2,5): "cama",
(3,5): "cama",
(1,5): "ventana",
#salón
(4,1): "mesa",
(6,1): "mesa",
(5,3): "planta",
#comedor
(4,6):"mesa",
(5,6):"planta",
}

personajes = {
(1,2): "Alejandro",
(5,1): "Beatriz",
(2,3): "Carolina",
(3,5): "Dante",
(6,6): "Elisabeth"
}

victima = "Vicente"

@app.route("/game")
def game():
    return render_template('game.html', history=history, elementos=elementos, personajes=personajes)

@app.route("/tablero")
def tablero():
    casillas = []
    for fila in range(1, 7):
        for columna in range(1, 7):
            contenido = ""
            #si hay algún elemento en alguna casilla
            if (fila, columna) in elementos:
                contenido = elementos[(fila, columna)]
            #si hay personajes en alguna casilla
            if (fila, columna) in personajes:
                if contenido != "":
                    contenido += " - "
                    contenido += personajes[(fila, columna)]
            #añadimos todas las casillas al tablero
            casillas.append({
                    "fila": fila,
                    "columna": columna,
                    "contenido": contenido                 
                })
           
        #última casilla libre para la víctima
        for casilla in reversed(casillas):
            if casilla["contenido"] == "":
                casilla["contenido"] = victima
                break

        return jsonify({
             "casillas": casillas,
             "history": history})
    
if __name__ == "__main__":
 app.run(debug=True)