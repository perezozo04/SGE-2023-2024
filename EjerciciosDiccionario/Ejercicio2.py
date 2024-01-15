FEMPLE = [{'N':15, 'Nombre':'Pepe', 'Cate':'A', 'Pais':"España"},
          {'N':16, 'Nombre':'Pepe2', 'Cate':'C', 'Pais':"España"},
          {'N':17, 'Nombre':'Pepe3', 'Cate':'A', 'Pais':"Alemania"},
          {'N':18, 'Nombre':'Pepe4', 'Cate':'B', 'Pais':"España"}]

SumaCate = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
SumaPais = {'España':0, 'Francia':0, 'Alemania':0, 'China':0}

for E in FEMPLE:
    SumaCate[E['Cate']] += 1
    SumaPais[E['Pais']] += 1
    
# for i in range(len(FEMPLE)):
#     SumaCate[FEMPLE[i]['Cate']] += 1
#     SumaPais[FEMPLE[i]['Pais']] += 1
    
Maximo = 0
MaxPais = ""



for i in SumaPais:
    if SumaPais[i] > Maximo:
        Maximo = SumaPais[i]
        MaxPais = i

print(SumaPais)
print(max(SumaPais))
