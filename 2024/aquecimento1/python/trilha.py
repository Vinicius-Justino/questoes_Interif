quantidade_conexoes = int(input().split()[1])
origem,destino = input().split()

conexoes = {}
for i in range(quantidade_conexoes):
    caminho = input().split()
    distancia = int(caminho.pop(2))

    for i in range(2):
        cidade1 = caminho[i]
        cidade2 = caminho[(i + 1) % 2]

        try:
            conexoes[cidade1].append((cidade2, distancia))
        except KeyError:
            conexoes[cidade1] = [(cidade2, distancia)]

trilhas = [[0, origem]]
melhor_trilha = []
while len(melhor_trilha) == 0:
    for i in range(len(trilhas)):
        trilha = trilhas.pop(0)

        caminhos_completos = []
        for conexao in conexoes[trilha[len(trilha) - 1]]:
            salto = trilha.copy()

            salto.append(conexao[0])
            salto[0] += conexao[1]

            if (conexao[0] == destino):
                caminhos_completos.append(salto)
            else:
                trilhas.append(salto)

        if len(caminhos_completos) > 0:
            menor_distancia = caminhos_completos[0][0]
            melhor_trilha = caminhos_completos[0]

            for caminho in caminhos_completos:
                if caminho[0] < menor_distancia:
                    melhor_trilha = caminho
            
            break

saida = f"Percurso: {origem}"
for i in range(2, len(melhor_trilha)):
    saida += f"--> {melhor_trilha[i]}"

print(saida)