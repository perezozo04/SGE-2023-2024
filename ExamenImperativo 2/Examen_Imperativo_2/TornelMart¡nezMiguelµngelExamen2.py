def Recortes(matrixRecortes):
    fila = len(matrixRecortes)
    for x in range(fila):
        if fila > len(matrixRecortes[x]):
            columna = fila = len(matrixRecortes[x])
    
    matriz_recorte = [[_ for _ in range(columna)]for _ in range(fila)]
    matriz_sobrante = []

    for x in range(len(matrixRecortes)):
        for y in range(len(matrixRecortes[x])):
            if x < fila and y < columna:
                matriz_recorte[x][y] = matrixRecortes[x][y]
    
    for x in range(len(matrixRecortes)):
        listaSobrantes = []
        for y in range(len(matrixRecortes[x])):
            if x > fila-1 or y > columna-1:
                listaSobrantes.append(matrixRecortes[x][y])
        if len(listaSobrantes) > 0:
            matriz_sobrante.append(listaSobrantes)
    
    return (matriz_recorte,matriz_sobrante)

def MostrarMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print(matriz[fila][columna],end="\t")
        print()

#PROGRAMA PRINCIPAL POR MIGUEL ÁNGEL TORNEL MARTÍNEZ
matrix = [[1,2,3],[4,5],[6,7],[8,9,10]]
resultado = Recortes(matrix)

print("Matriz Original")
MostrarMatriz(matrix)
print()
print("Matriz Recortada")
MostrarMatriz(resultado[0])
print()
print("Matriz Sobrante")
MostrarMatriz(resultado[1])