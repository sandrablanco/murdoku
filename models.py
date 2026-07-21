import numpy as np

class Murdoku:
    def __init__(self):
        self.tamano = 6

        self.elementos = {
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

        self.emoji_elementos = {
            "ventana": "🪟",
            "cama": "🛏️",
            "mesa": "🍴",
            "planta": "🌱",
        }

        self.personajes = {
            (1, 2): "Alejandro",
            (5, 1): "Beatriz",
            (2, 3): "Carolina",
            (3, 5): "Dante",
            (6, 6): "Elisabeth",
        }

        self.emoji_personajes = {
            "Alejandro": "👨🏻",
            "Beatriz": "👩🏻",
            "Carolina": "👩🏼",
            "Dante": "👨🏼",
            "Elisabeth": "👩🏽",
        }

        self.victima = "Vicente"
        self.emoji_victima = "💀"

    def crear_tablero(self):

        # matriz de strings vacíos
        board = np.full((self.tamano, self.tamano), "", dtype=object)
        tipos = np.full((self.tamano, self.tamano), "vacio", dtype=object)

        # colocar elementos con su emoji
        for (fila, columna), nombre in self.elementos.items():
            i, j = fila - 1, columna - 1
            emoji = self.emoji_elementos.get(nombre, "")
            board[i, j] = f"{emoji} {nombre}"
            tipos[i, j] = nombre

        # calcular la posición de la víctima
        board_solution = board.copy()

        for (fila, columna), nombre in self.personajes.items():
            i, j = fila - 1, columna - 1

            if board_solution[i, j] == "":
                board_solution[i, j] = nombre

        filas_vacias, columnas_vacias = np.where(board_solution == "")

        if len(filas_vacias) > 0:
            vi, vj = filas_vacias[-1], columnas_vacias[-1]
            board[vi, vj] = f"{self.emoji_victima} {self.victima}"
            tipos[vi, vj] = "victima"

        casillas = [
            {
                "fila": i + 1,
                "columna": j + 1,
                "contenido": board[i, j],
                "tipo": tipos[i, j],
            }
            for i in range(self.tamano)
            for j in range(self.tamano)
        ]

        return casillas