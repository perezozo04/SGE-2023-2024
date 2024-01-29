import random


def main():
    filas = int(input("Introduce el numero de filas: "))
    columnas = int(input("Introduce el numero de columnas: "))

    matriz = GenerarCiudad(filas, columnas)

    

    Contagiar(matriz)

def GenerarCiudad(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("SANO")
        matriz.append(fila)
    
    filaRandom = random.randint(0, filas-1)
    columnaRandom = random.randint(0, columnas-1)

    matriz[filaRandom][columnaRandom] = "I-0"

    return matriz

def MostrarCiudad(matriz, dia):
    print(f"Dia {dia}", end="\n\n")
    for fila in matriz:
        print("", end="\t")
        for e in fila:
            print(e, end="\t")
        print()    

def Contagiar(matriz):
    dia = 0

    while any("SANO" in fila for fila in matriz):
        dia += 1
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if (matriz[i][j] == f"I-{dia-1}"):
                    if i > 0 and matriz[i-1][j]  == "SANO" : matriz[i-1][j] = f"I-{dia}"
                    if j > 0 and matriz[i][j-1]  == "SANO" : matriz[i][j-1] = f"I-{dia}"
                    if i+1 < len(matriz) and matriz[i+1][j]  == "SANO" : matriz[i+1][j] = f"I-{dia}"
                    if j+1 < len(matriz[0]) and matriz[i][j+1]  == "SANO" : matriz[i][j+1] = f"I-{dia}"
        MostrarCiudad(matriz, dia)

main()