print("Introduzca las notas, ENTER para terminar: ")
notatotal = 0
contalumnos = 0
aprobado = 0
suspenso = 0
listNotas = []

while True:
    nota = float(input(f"Nota del alumno {contalumnos}: "))  
    if nota == "":
        break
    contalumnos += 1
    nota = float(nota)
    notatotal += nota
    listNotas.append(nota)
    if nota >= 5:
        aprobado += 1
    else: 
        suspenso += 1
print("Se han introducido las siguientes notas: ")
lista_size = len(listNotas)
for i in range(lista_size):
    print(f"Nota de alumno  + {i}: {listNotas[nota]}")

print("Resumen: ")
print(f"Numero de alumnos: " + lista_size)
print(f"Numero de aprobados: {aprobado}")
print(f"NUmero de suspensos: {suspenso}")
print(f"La nota media es: {notatotal/contalumnos}")