def calcular_facotorial(n):
    resultado = 1
    for i in range(0, n + 1):
        if i == 0 or i == 1:
            print(f"{i}! = 1")
        else:
            resultado *= i
            print(f"{i}! = {resultado}")


n = int(input("Introduce un numero: "))
calcular_facotorial(n)