def changeToTuple(matrix):
    tupleList = tuple(matrix)
    print(tupleList)



matrix = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]
colEnCadaFila = []

for i in range(len(matrix)):
    counter = 0
    for j in range(len(matrix[i])):
        counter += 1
    colEnCadaFila.append(counter)

numMin = min(min(colEnCadaFila), len(matrix))

matrix_recorte = [["x" for _ in range(numMin)] for _ in range(numMin)]
print(matrix_recorte)

matrix_sobrante = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
       if i < len(matrix_recorte) and j < len(matrix_recorte[i]):
           matrix_recorte[i][j] = matrix[i][j]
       else:
           matrix_sobrante.append(matrix[i][j])

print(matrix_recorte)
print(matrix_sobrante)
changeToTuple(matrix_recorte)


