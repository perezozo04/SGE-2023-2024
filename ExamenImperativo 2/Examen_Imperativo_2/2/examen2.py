from Recortes import recortes
import random

def crearMatriz():
    matriz=[]
    for i in range(4):
        list = []
        for j in range(random.randint(2, 6)):
            list.append(random.randint(0,99))
        matriz.append(list)
        
        for fila in matriz:
            print(fila)
            
    return matriz

def mostrarMatriz(matriz, cadena):
    print(f"\nMatriz {cadena}")
    for fila in matriz:
        print(fila)
matriz= crearMatriz()   

tupla = recortes(matriz) 
matriz_recortes = tupla[0]
matriz_sobrante = tupla[1]
mostrarMatriz(matriz_recortes, "recortada")
mostrarMatriz(matriz_sobrante, "sobrante")