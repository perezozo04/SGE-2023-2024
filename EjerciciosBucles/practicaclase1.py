row = int(input("Dime el numero de filas: "))
colums = int(input("Dime el numero de columnas: "))
l = []
i = 0
j = 0
for i in range(row):
    l.append([])
    for j in range(colums):
        val = int(input(f"Dime el valor de la columna {j} dentro de la fila {i}: "))
        l[i].append(val)
print(l)