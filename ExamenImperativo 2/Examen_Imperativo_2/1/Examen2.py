import Modulo as mod

matriz = [
    [1, 2, 3],
    [4, 5],
    [6, 7],
    [8, 9, 10]
]

tupla = mod.Recortes(matriz)

def MostrarMatriz(matrix,nombre):
    
    print(f"Matriz {nombre}")
    
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print("\n")
    
MostrarMatriz(matriz,"Original")
MostrarMatriz(tupla[0],"Recortada")
MostrarMatriz(tupla[1],"Sobrante")

