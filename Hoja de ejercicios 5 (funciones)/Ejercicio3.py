import re

def es_nif(nif):
    numeroDNI = nif[:8]
    numletra = int(numeroDNI) % 23
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra = abecedario[numletra]
    if letra != nif[8:]:
        return False
    else:
        return True
    
def validar_dni(dni):
    expresion_regular = "^[0-9]{8}[A-Z]$"
    if re.match(expresion_regular, dni):
        return True
    else:
        return False
    
nif = input("Introduce un dni")

if not validar_dni(nif) : print("DNI no valido")
elif not  es_nif(nif) : print("Letra de DNI no valida")
else : print("El dni es correcto")
    