class Diccionario():
    def __init__(self, N="Ingeniero", E= "Español", NI="FP"):
        self.Nombre = N
        self.Editorial = E
        self.Nivel = NI
        self.dic = dict()
    def IntroducirPalabras(self, Palabra):
        if Palabra in self.dic:
            return "Ya existe"
        else:
            self.dic[Palabra] = list()
            return "Introducida"
    def IntroducirAcepciones(self, P, A):
        if P in self.dic:
            self.dic[P].append(A)
            return "Acepcion añadida"
        else:
            return "No existe la palabra"
    def Consulta(self, P):
        if P in self.dic:
            return self.dic[P]
    
    def __str__(self):
        cadena=f"Diccionario: {self.Nombre}\n\n"
        palabras=sorted(self.dic.keys())
        for p in palabras:
            cadena +=p + ":\n"
            for a in self.dic[p]:
                cadena += f"\t{a}\n"
        return cadena
        
    def Palabras(self, L):

        i = 0
        palabras=sorted(self.dic.keys)
        while i < len(palabras) and L < palabras[i][0]:
            i+=1
        while i < len(palabras) and L == palabras[i][0]:
            cadena += palabras[i] + " - "
            i+=1

        while i < len(palabras) and L <= palabras[i][0]:
            if L == palabras[i][0]:
                cadena+=palabras[i] + " - "
            i+=1
            
            
print("1.- Crear Diccionario")
print("2.- Introducir Palabras")
print("3.- Introducir Acepcion")
print("4.- ")
print("5.- Mostrar palabras que empieces por una letra")
opcion = int(input("Teclee una opcion (0 salir): "))

while opcion != 0:
    if opcion == 1:
        D = Diccionario()

    elif opcion == 2:
        P = input("Palabra: ")
        print(D.IntroducirPalabras(P))
    elif opcion == 3:
        P = input("Palabra: ")
        A = input("Acepcion: ")
        print(D.IntroducirAcepciones(P, A))
    elif opcion == 4:
        print(D)
    elif opcion == 5:
        letra = input("Introduce una letra: ")
        D.Palabras(letra)
    opcion = int(input("Teclee una opcion (0 salir): "))