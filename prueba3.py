curso1=set(["Juan", "Pedro", "Antonio"])
curso2=set(["Luis", "María", "Lola"])
curso3=set(["Manolo", "Lucía", "Enrique"])

instituto=[curso1, curso2, curso3]

equipo=set(["Juan", "Antonio"])
pertenece=False
for curso in instituto:
    if equipo.issubset(curso):
        print("Todo el equipo pertenece a una clase")
        pertenece=True
i=0


while i < len(instituto) and not equipo.issubset(instituto[i]):
        i+1

if i < len(instituto):
    print("pertenece")
else:
    print("No pertence")
