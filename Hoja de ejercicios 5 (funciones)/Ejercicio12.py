import random

def generadorMatrices():
    filas = random(2, 6)
    columnas = random(2, 6)
    matriz = []

    for _ in range(filas):
        row = []
        for _ in range(columnas):
            column = random(0,100)
            row.append(column)
        matriz.append(row)

