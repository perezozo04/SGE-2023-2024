num = int(input("Introduzca un numero: "))
resultado = 0
if num < 0:
    print("Tienes que introducir un numero positivo")
else:
    for i in range(0, num):
        if i%2 == 0:
            resultado += i
print(f"La suma es: {resultado}")