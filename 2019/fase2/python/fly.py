OESTE, SUL, NORTE, LESTE = -1, -2, -3, -4

direcoes = {
    -1: "oeste",
    -3: "norte",
    -2: "sul",
    -4: "leste"
}

avioes = {
    "oeste": [],
    "norte": [],
    "sul": [],
    "leste": []
}

direcao = ""
while True:
    entrada = input()
    if entrada[0] == "0":
        break
    elif entrada[0] == "-":
        direcao = direcoes[int(entrada)]
    else:
        avioes[direcao].append(entrada)

fila = []
while True:
    ordem = [direcao for direcao in avioes.keys() if len(avioes[direcao]) > 0]
    if len(ordem) == 0:
        break

    for direcao in ordem:
        fila.append(avioes[direcao].pop(0))

print(" ".join(fila))