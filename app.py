from flask import Flask, jsonify, render_template
import numpy as np

app = Flask(__name__)

history = """Título: Tu primer caso como detective.

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

# objetos del tablero
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

emoji_elementos = {
    "ventana": "🪟",
    "cama": "🛏️",
    "mesa": "🍴",
    "planta": "🌱",
}

personajes = {
    (1, 2): "Alejandro",
    (5, 1): "Beatriz",
    (2, 3): "Carolina",
    (3, 5): "Dante",
    (6, 6): "Elisabeth",
}

emoji_personajes = {
    "Alejandro": "👨🏻",
    "Beatriz": "👩🏻",
    "Carolina": "👩🏼",
    "Dante": "👨🏼",
    "Elisabeth": "👩🏽",
}

victima = "Vicente"
emoji_victima = "💀"
TamañoTablero = 6


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/tablero")
def tablero():
    # matriz de strings vacíos, indexada 0..5
    board = np.full((TamañoTablero, TamañoTablero), "", dtype=object)

    # colocar elementos con su emoji
    for (fila, columna), nombre in elementos.items():
        emoji = emoji_elementos.get(nombre, "")
        board[fila - 1, columna - 1] = f"{emoji} {nombre}"

    #calculo de la posicion de la victima pero sin pintar en el frontend
    board_solution = board.copy()
    for (fila, columna), nombre in personajes.items():
        i, j = fila - 1, columna - 1
        board_solution[i, j] == "":
        board_solution[i, j] = nombre
    filas_vacias, columnas_vacias = np.where(board_solution == "")
    if len(filas_vacias) > 0:
        victima_fila, victima_columna = filas_vacias[-1], columnas_vacias[-1]
        board[victima_fila, victima_columna] = f"{emoji_victima} {victima}"

        casillas = [
        {"fila": i + 1, "columna": j + 1, "contenido": board[i, j]}
        for i in range(TamañoTablero)
        for j in range(TamañoTablero)
    ]

    return jsonify({"casillas": casillas, "history": history})

    # colocar personajes con su emoji (concatenando si ya hay algo)
    # for (fila, columna), nombre in personajes.items():
    #     i, j = fila - 1, columna - 1
    #     emoji = emoji_personajes.get(nombre, "")
    #     texto = f"{emoji} {nombre}"
    #     if board[i, j]:
    #         board[i, j] += " - " + texto
    #     else:
    #         board[i, j] = texto

    # # buscar la última casilla vacía para la víctima
    # filas_vacias, columnas_vacias = np.where(board == "")
    # if len(filas_vacias) > 0:
    #     i, j = filas_vacias[-1], columnas_vacias[-1]
    #     board[i, j] = f"{emoji_victima} {victima}"

    # # construir la lista de casillas para el JSON
    # casillas = [
    #     {"fila": i + 1, "columna": j + 1, "contenido": board[i, j]}
    #     for i in range(TamañoTablero)
    #     for j in range(TamañoTablero)
    # ]

    # return jsonify({"casillas": casillas, "history": history})

@app.route("/jugada", methods=["POST"])
def jugada():
    from flask import request
    data = request.get_json()
    personaje = data.get("personaje")
    fila = data.get("fila") 
    columna = data.get("columna")

if __name__ == "__main__":
    app.run(debug=True)