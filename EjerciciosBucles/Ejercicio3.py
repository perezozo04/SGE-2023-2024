print("Introduzca las notas, ENTER para terminar: ")
notatotal = 0
contalumnos = 1
aprobado = 0
suspenso = 0
while True:
    nota = input(f"Nota del alumno {contalumnos}: ")  
    if nota == "":
        break
    contalumnos += 1
    nota = float(nota)
    notatotal += nota
    if nota >= 5:
        aprobado += 1
    else: 
        suspenso += 1
print(f"Numero de aprobados: {aprobado}")
print(f"NUmero de suspensos: {suspenso}")
print(f"La nota media es: {notatotal/contalumnos}")
