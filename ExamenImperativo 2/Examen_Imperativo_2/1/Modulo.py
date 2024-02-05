import copy

def Recortes(matriz):
    
    columnas_mas_pequeño = float('inf')  # Inicializar con infinito para asegurarse de que cualquier longitud de fila sea menor
    
    for i in range(len(matriz)):
        if len(matriz[i]) < columnas_mas_pequeño:
            columnas_mas_pequeño = len(matriz[i])
         
    filas = len(matriz)
    columnas = columnas_mas_pequeño
                
    
    
    Matriz_recorte = []
    Matriz_sobrante = copy.deepcopy(matriz)
    for i in range(columnas):
        Matriz_recorte.append([])
        for j in range(columnas):
            if j < len(matriz[i]):
                    Matriz_recorte[i].append(matriz[i][j])
                
                    Matriz_sobrante[i].remove(matriz[i][j])

   # Filtrar las filas que contienen elementos
    Matriz_sobrante = [fila for fila in Matriz_sobrante if fila]
    
    tupla = (Matriz_recorte, Matriz_sobrante)

    return tupla
            
                

