from flask import Flask, jsonify, render_template
import numpy as np
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
(1,2): "ventana": "🪟",
#dormitorio
(2,5): "cama": "🛏️",
(3,5): "cama": "🛏️",
(1,5): "ventana": "🪟",
#salón
(4,1): "mesa": "🍴",
(6,1): "mesa": "🍴",
(5,3): "planta": "🌱",
#comedor
(4,6):"mesa": "🍴",
(5,6):"planta": "🌱",
}

personajes = {
(1,2): "Alejandro": "👨🏻",
(5,1): "Beatriz": "👩🏻",
(2,3): "Carolina": "👩🏼",
(3,5): "Dante": "👨🏼",
(6,6): "Elisabeth": "👩🏽"
}

victima = "Vicente": "💀"
tamaño_tablero = 6

@app.route("/")
def game():
    return render_template("index.html")

@app.route("/tablero")
def tablero():
 from flask import Flask, jsonify, render_template
import numpy as np

app = Flask(__name__)

history = """...""" # (tu texto igual)

elementos = {
    (1, 2): "ventana",
    (2, 5): "cama",
    (3, 5): "cama",
    (1, 5): "ventana",
    (4, 1): "mesa",
    (6, 1): "mesa",
    (5, 3): "planta",
    (4, 6): "mesa",
    (5, 6): "planta",
}

personajes = {
    (1, 2): "Alejandro",
    (5, 1): "Beatriz",
    (2, 3): "Carolina",
    (3, 5): "Dante",
    (6, 6): "Elisabeth",
}

victima = "Vicente"
TamañoTablero = 6

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/tablero")
def tablero():
    # matriz de strings vacíos, indexada 0..5
    board = np.full((TamañoTablero, TamañoTablero), "", dtype=object)
    #coloca emojis con los elementos
    for (fila, columna), nombre in elementos.items():
        emoji = emoji_elementos.get(nombre, "")
        board[fila - 1, columna - 1] = f"{emoji} {nombre}"
    # colocar elementos (restando 1 porque coordenadas empiezan en 1)
    for (fila, columna), nombre in elementos.items():
        board[fila - 1, columna - 1] = nombre

    # colocar personajes (concatenando si ya hay algo)
    for (fila, columna), nombre in personajes.items():
        i, j = fila - 1, columna - 1
        if board[i, j]:
            board[i, j] += " - " + nombre
        else:
            board[i, j] = nombre

    # buscar la última casilla vacía para la víctima (vectorizado)
    filas_vacias, columnas_vacias = np.where(board == "")
    if len(filas_vacias) > 0:
        i, j = filas_vacias[-1], columnas_vacias[-1]
        board[i, j] = victima

    # construir la lista de casillas para el JSON
    casillas = [
        {"fila": i + 1, "columna": j + 1, "contenido": board[i, j]}
        for i in range(TamañoTablero)
        for j in range(TamañoTablero)
    ]

    return jsonify({"casillas": casillas, "history": history})

if __name__ == "__main__":
    app.run(debug=True)
   