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
    tipos = np.full((TamañoTablero, TamañoTablero), "vacio", dtype=object)

    # colocar elementos con su emoji
    for (fila, columna), nombre in elementos.items():
        i, j = fila - 1, columna - 1
        emoji = emoji_elementos.get(nombre, "")
        board[i, j] = f"{emoji} {nombre}"
        tipos[i, j] = nombre #cama, mesa, planta, ventana

    #calculo de la posicion de la victima pero sin pintar en el frontend
    board_solution = board.copy()
    for (fila, columna), nombre in personajes.items():
        i, j = fila - 1, columna - 1
        if board_solution[i, j] == "":
         board_solution[i, j] = nombre
    filas_vacias, columnas_vacias = np.where(board_solution == "")
    if len(filas_vacias) > 0:
        vi, vj = filas_vacias[-1], columnas_vacias[-1]
        board[vi, vj] = f"{emoji_victima} {victima}"
        tipos[vi, vj] = "victima"

        casillas = [
        {"fila": i + 1, "columna": j + 1, "contenido": board[i, j], "tipo": tipos[i, j]}
        for i in range(TamañoTablero)
        for j in range(TamañoTablero)
    ]

    return jsonify({"casillas": casillas, "history": history})

@app.route("/jugada", methods=["POST"])
def jugada():
    from flask import request
    data = request.get_json()
    personaje = data.get("personaje")
    fila = data.get("fila") 
    columna = data.get("columna")
    #validación de la jugada(errores)
    if personaje is None or fila is None or columna is None:
        return jsonify({"error": "Faltan datos de la jugada"}), 400
    if personaje not in personajes.values():
        return jsonify({"error": "Personaje no válido"}), 400
    if not (1 <= fila <= TamañoTablero) or not (1 <= columna <= TamañoTablero):
        return jsonify({"error": "Coordenadas fuera del tablero"}), 400
    #ningun personaje se coloca en planta o mesa
    tipo_casilla = elementos.get((fila, columna))
    if tipo_casilla in ["mesa", "planta"]:
        return jsonify({"error": f"No se puede colocar {personaje} en una {tipo_casilla}"}), 400
    
    #comparación con la solución real
    posicion_real = personajes.get((fila, columna))
    if posicion_real == personaje:
        return jsonify({
            "resultado": "correcto", 
            "mensaje": f"{personaje} está en la posición correcta.",
            "contenido": f"{emoji_personajes[personaje]} {personaje}"
            })
    else: 
        return jsonify({
            "resultado": "incorrecto", 
            "mensaje": f"{personaje} no está en la posición ({fila}, {columna}).",
            "contenido": f"{emoji_personajes[personaje]} {personaje}"
            })

if __name__ == "__main__":
    app.run(debug=True)