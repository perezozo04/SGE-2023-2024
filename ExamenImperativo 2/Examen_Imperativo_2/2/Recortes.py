
def recortes(matriz):
    
    maxfilas = len(matriz)
    minColumnas = len(matriz[0])
    tamañoMaximo =0
    
    for fila in matriz:
        if len(fila)<minColumnas:
            minColumnas=len(fila)  
    if maxfilas > minColumnas:
        tamañoMaximo = minColumnas
    else:
        tamañoMaximo = maxfilas
    matriz_recorte=[]
    matriz_sobrante=[]
    i=0
    for valor in matriz:
        listRecorte=[]
        listSobrante=[]
        j=0
        for numero in valor:
            if j<tamañoMaximo and i<maxfilas:
                listRecorte.append(numero)
            else:
                try:
                    listSobrante.append(numero)
                except:
                    pass
            j+=1
        i+=0
        if listRecorte:
            matriz_recorte.append(listRecorte)
        if listSobrante:
            matriz_sobrante.append(listSobrante)
        
    tupla = (matriz_recorte, matriz_sobrante)
    return tupla