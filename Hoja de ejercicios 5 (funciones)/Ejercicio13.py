import random


def generadorMatrices():
    filas = random.randint(2, 6)
    columnas = random.randint(2, 6)
    matriz = []

    for _ in range(filas):
        row = []
        for _ in range(columnas):
            column = random.randint(0,100)
            row.append(column)
        matriz.append(row)
    return matriz


    
def sumaMatriz(matriz):
    numFilas = len(matriz)
    numColumnas = len(matriz[0])
    suma = 0

    if numFilas != numColumnas:
        return None
    else:
        for i in range(numFilas):
            suma += matriz[i][i]
        return suma

resultado = None
while resultado == None:
    print()
    matriz = generadorMatrices()
    for fila in matriz:
        print("", end="\t")
        for e in fila:
            print(e, end="\t")
        print() 
    resultado = sumaMatriz(matriz)
    if resultado == None:
        print("La funcion de arriba no es cuadrada")
    else:
        print(f"El resultado de la suma de la diagonal es igual a: {resultado}")
    
    
