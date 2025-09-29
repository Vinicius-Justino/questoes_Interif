circulo = list(range(int(input())))
morte_observada = int(input())
cont_mortos = 0

pode_morrer = False
while len(circulo) > 1:
    pessoa = circulo.pop(0)

    if not pode_morrer:
        circulo.append(pessoa)
    else:
        cont_mortos += 1
        if cont_mortos == morte_observada:
            print(f"Morte {morte_observada}: {pessoa + 1}")
    
    pode_morrer = (not pode_morrer)

print(f"Sobrevivente: {circulo[0] + 1}")