def masLarga(lista):
    longitudPalabraLarga = 0
    listaPalabrasLargas = []

    
    for palabra in lista:
        longitudPalabra = len(palabra)
        if longitudPalabra > longitudPalabraLarga: 
            listaPalabrasLargas = [palabra]
            longitudPalabraLarga = longitudPalabra
        elif longitudPalabra == longitudPalabraLarga: listaPalabrasLargas.append(palabra)
        
    return listaPalabrasLargas

lista = ["Pepe", "Ana", "Juan", "Paz"]

lisitaPalabrasLargas = masLarga(lista)

print(lisitaPalabrasLargas)