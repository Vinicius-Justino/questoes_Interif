mapa = {}
for elo in range(int(input())):
    p1, p2 = [int(n) for n in input().split(" ")]

    try:
        mapa[p1].append(p2)
    except KeyError:
        mapa[p1] = [p2]
    
    try:
        mapa[p2].append(p1)
    except KeyError:
        mapa[p2] = [p1]

caminhos = [[list(mapa.keys())[0]]]
for salto in range(len(mapa.keys()) - 1):
    for i in range(len(caminhos)):
        caminho_atual = caminhos.pop(0)

        for prox_ponto in mapa[caminho_atual[-1]]:
            if prox_ponto in caminho_atual:
                continue

            continuacao_caminho = caminho_atual.copy()
            continuacao_caminho.append(prox_ponto)
            caminhos.append(continuacao_caminho)
        
existe_ciclo = False
while not existe_ciclo and len(caminhos) > 0:
    caminho = caminhos.pop(0)
    existe_ciclo = (caminho[0] in mapa[caminho[-1]])

print("Sim" if existe_ciclo else "Nao")