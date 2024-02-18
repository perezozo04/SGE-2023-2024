import random


class Examen:
    def __init__(self, modulo):
        self.modulo = modulo
        self.preguntas = {}
    
    def InsertarPregunta(self, pregunta, respuesta_correcta, puntuacion, tema="Python"):
        puntuacion = int(puntuacion)
        elementos = (pregunta, respuesta_correcta, puntuacion)
        if puntuacion < 0:
            puntuacion = 1
        elif puntuacion > 10:
            puntuacion = 10
            
        if tema not in self.preguntas:
            self.preguntas[tema] = [(pregunta, respuesta_correcta, puntuacion)]
        else: 
            self.preguntas[tema].append(elementos)

    def __str__(self):
        for i in self.preguntas:
           print(f"Tema: {i}")
           for j in self.preguntas[i]:
                print(f"\n\tPregunta: {j[0]}\n\tRespuesta: {j[1]}\n\tPuntuacion: {j[2]}\n")
    
    def GenerarExamen(self, tema, preguntas):
        numeroPreguntas = 0
        listaPreguntas = list()
        puntacionObtenida = 0
        puntuacionMaxima = 0
        if tema in self.preguntas:
            ## Para cara el numero de pregunta tambien se puede hacer lo siguiente: len(self.preguntas[tema]) en vez de hacer el for
            ##for _ in self.preguntas[tema]:
            ##    numeroPreguntas += 1
            numeroPreguntas = len(self.preguntas[tema])
            if numeroPreguntas < preguntas:
                print("No hay suficientes preguntas")
            else:
                for i in range(preguntas):
                    nPregunta = random.randint(0, numeroPreguntas-1)
                    while nPregunta in listaPreguntas:
                        nPregunta = random.randint(0, numeroPreguntas-1)
                    ## if nPregunta not in listaPreguntas:

                    listaPreguntas.append(nPregunta)
                    print(f"Pregunta {i}: {self.preguntas[tema][nPregunta][0]}")
                    r = input("Tu respuesta es: ")
                    if r == self.preguntas[tema][nPregunta][1]:
                        puntacionObtenida += self.preguntas[tema][nPregunta][2]

                    puntuacionMaxima += self.preguntas[tema][nPregunta][2]
                print(f"\n----------------------------------------------------")
                print(f"\nTotal Preguntas: {numeroPreguntas}" )
                print(f"Puntación Maxima Posible : {puntuacionMaxima}")
                print(f"Puntación obtenida: {puntacionObtenida}")
                    

def menu():

    print("1. Crear Examen")
    print("2. INtroducir pregunta")
    print("3. Imprimir preguntas")
    print("4. Generar examen")
    print("0. Salir")

menu()

opcion = int(input("Teclee una opcion : "))

while opcion != 0:

    if opcion == 1:
        modulo = input("Dime un modulo: ")

        examen = Examen(modulo)
        print("creado")


    elif opcion == 2:

        tema = input("Introduce el tema: ")
        pregunta = input("Introduce la pregunta: ")
        respuestaCorrecta = input("Introduce la respuesta: ")
        puntuacion = input("Introduce la puntuacion: ")

        examen.InsertarPregunta(pregunta, respuestaCorrecta, puntuacion, tema)

        examen.__str__()

    elif opcion == 3:

        examen.__str__()


    elif opcion == 4:
        tema = input("Introduce el tema para el examen: ")
        numeroPreguntas = int(input("Introduce numero de preguntas que quieres contestar: "))

        examen.GenerarExamen(tema, numeroPreguntas)

    opcion = int(input("Teclee una opcion : "))