num = int(input("Introduzca un numero: "))
resultado = 0
if num < 0:
    print("Tienes que introducir un numero positivo")
else:
    for i in range(0, num, 2):
        resultado += i
print(f"La suma es: {resultado}")