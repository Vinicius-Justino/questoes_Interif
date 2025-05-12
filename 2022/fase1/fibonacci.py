from math import ceil

tamanho_matriz = int(input())
camadas = []
quantidade_termos = ceil(tamanho_matriz / 2)
camada_atual = 0
for linha in range(tamanho_matriz):
    if (linha < quantidade_termos):
        camadas.append([])
        camada_atual = linha
    else:
        camada_atual -= 1

    petalas = [int(n) for n in input().split(" ")]
    for camada_exterior in range(camada_atual):
        camadas[camada_exterior].append(petalas.pop(0))
        camadas[camada_exterior].append(petalas.pop(-1))
    
    for petala in petalas:
        camadas[camada_atual].append(petala)

sequencia = [1, 1]
for i in range(quantidade_termos - 2):
    sequencia.append(sequencia[-1] + sequencia[-2])

fibonacci = True
for i in range(quantidade_termos):
    if not fibonacci:
        break

    camada = camadas[(i + 1) * -1]
    termo = sequencia[i]

    for petala in camada:
        if not fibonacci:
            break

        fibonacci = (petala == termo)

print("Fibonacci" if fibonacci else "Nao fibonacci")