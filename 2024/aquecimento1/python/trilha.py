distritos, conexoes = [int(n) for n in input().split(" ")]
inicio, final = input().split(" ")

mapa = {}
for conexao in range(conexoes):
    origem, destino, distancia = input().split(" ")
    distancia = int(distancia)

    try:
        mapa[origem].append((destino, distancia))
    except KeyError:
        mapa[origem] = [(destino, distancia)]

caminhos = [[0, inicio]]
caminhos_possiveis = []
while len(caminhos_possiveis) == 0:
    for i in range(len(caminhos)):
        caminho_atual = caminhos.pop(0)
        if caminho_atual[-1] == destino:
            caminhos_possiveis.append(caminho_atual)
            continue

        for vizinho,distancia in mapa[caminho_atual[-1]]:
            if vizinho in caminho_atual:
                continue

            continuacao_caminho = caminho_atual.copy()
            continuacao_caminho.append(vizinho)
            continuacao_caminho[0] += distancia
            caminhos.append(continuacao_caminho)

menor_distancia = min([caminho[0] for caminho in caminhos_possiveis])
melhor_caminho = []
for caminho in caminhos_possiveis:
    if caminho[0] == menor_distancia:
        melhor_caminho = caminho[1:]

print(f"Percurso: {melhor_caminho.pop(0)}", end="")
for cidade in melhor_caminho:
    print(f"--> {cidade}", end="")
print()