n = int(input("Escribe un numero y se mostrará su tabla de multiplicar dos veces: "))
for i in range(0, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
    
j = 0
while j < 11:
    resultado = n * j
    print(f"{n} x {j} = {resultado}")
    j += 1
