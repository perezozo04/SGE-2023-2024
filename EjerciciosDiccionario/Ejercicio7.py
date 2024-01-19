matriz = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
  for j in range(5):
    print(f"Introduzca el valor para la fila {i + 1} columna {j + 1}: ")
    matriz[i][j] = int(input())

columna = list(range(5))
fila = list(range(5))

for i in range(5):
    columnas = 0
    filas = 0
    for j in range(5):
        columnas += matriz[i][j]
        filas += matriz[j][i]
        columna[i] = columnas
        fila[i] = filas

print(matriz)

print(columna)
print(fila)