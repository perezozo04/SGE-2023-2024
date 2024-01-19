import re

def es_nif(nif):
    caracteres = nif.split()
    
    total = 0
    
    for i in caracteres:
        if i < 8: digito = int(caracteres[i])
        total += digito
    if total/23 < 23 : return True
    else: return False
    
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
    