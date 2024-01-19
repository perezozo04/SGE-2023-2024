def es_primo(n):
    contador = 0
    if n == 2 or n == 3: return True
    for i in range(1, n+1):
        if n % i == 0 : contador += 1
    if contador > 2 : return False
    else : return True

n = int(input("Introduzca un numero: "))
cadena = "Numeros primos primos [2-" + str(n) + ": "
for i in range(2, n+1):
    if es_primo(i) : cadena += str(i) + ", "

print(cadena)