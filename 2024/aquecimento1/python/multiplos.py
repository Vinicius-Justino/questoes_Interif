numero = input()
somas = [0, 0]

for digito in numero:
    algarismo = int(digito)
    somas[algarismo % 2] += algarismo

for soma in somas:
    print("S" if soma % 3 == 0 else "N")