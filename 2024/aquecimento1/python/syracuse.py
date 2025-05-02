saida = []
while True:
    try:
        entrada = int(input())

        cont_passos = 0
        while entrada != 1:
            entrada = (entrada / 2) if (entrada % 2 == 0) else (entrada * 3 + 1)
            cont_passos += 1
        
        saida.append(cont_passos)
    except EOFError:
        break

for i in saida:
    print(i)