# Pablo Perez Martinez 19/1/2024
# Ejercicio 8
listaAlumnos = ["Ana", "Pau", "Luis", "Mar", "Paz"]
listaNotas = [10, 5.5, 2.0, 8.5, 7.0]

def menu(): 
    print("1) Añadir estudiante y calificacion")
    print("2) Mostrar lista de estudiantes con sus calificaciones")
    print("3) Mostrar estudiantes aprobados")
    print("4) Número de aprobados")
    print("5) Estudiantes con máxima nota")
    print("6) Estudiantes con nota mayor o igual a la media")
    print("7) Nota estudiante")
    print("8) Finalizar ejecución del programa")

    opcion = int(input("Elige una opcion del 1 al 8"))
    if opcion == 1:
        nombre = input("Nombre del alumno que quieres añadir: ")
        nota = int(input("Nota del alumno añadido"))
        listaAlumnos.append(nombre)
        listaNotas.append(nota)
        menu()
    if opcion == 2:
        for i in range(len(listaAlumnos)):
            print(f"Alumno: {listaAlumnos[i]} Nota: {listaNotas[i]}")
    if opcion == 3:
        alumnmosAprobados()

def alumnmosAprobados(listaAlumnos, listaNotas):
    listaAprobados = []
    for i in range(len(listaAlumnos)):
        if listaNotas[i] >= 5: listaAprobados.append(listaAlumnos[i])

def numAprobados(listaNotas):
    aprobados = 0
    for i in range(len(listaNotas)):
        if listaNotas[i] >= 5: aprobados += 1

def aluMaxNota(listaAlumnos, listaNotas):
    notaMax = 0
    listaAlumnosMax = []
    for i in range(len(listaNotas)):
        if listaNotas[i] > notaMax: 
            istaAlumnosMax = listaNotas[i]
            notaMax = listaNotas[i]
        elif notaMax == listaNotas[i]:
            listaAlumnosMax.append(listaNotas[i])
    return listaAlumnosMax


def aluMedNota(listaAlumnos, listaNotas): 
    notasTotal = 0
    notaMedia = 0
    for i in range(len(listaNotas)):
        notasTotal += listaNotas[i]
    notaMedia = notasTotal/len(listaNotas)
    return notaMedia

def estaEnClase(listaAlumnos, listaNotas, nombre):
    notaAlumno = 0
    nombreAlumno = "none"
    i = 0
    while i < len(listaAlumnos):
        if nombre == listaAlumnos[i]:
            nombreAlumno = listaAlumnos[i]
            notaAlumno = listaNotas[i]
            i = len(listaAlumnos)+1
        i += 1
    if nombreAlumno != none:
        return nombreAlumno, notaAlumno 
    else: return nombreAlumno


    