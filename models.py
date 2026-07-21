import numpy as np

class Murdoku:
    def_init_self(self):
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
    self.personajes = {
            (1, 2): "Alejandro",
            (5, 1): "Beatriz",
            (2, 3): "Carolina",
            (3, 5): "Dante",
            (6, 6): "Elisabeth",
        }

    self.victima = "Vicente"