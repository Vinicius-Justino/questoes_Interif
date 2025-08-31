organograma = {f"{input()}": []}
while True:
    subordinado, responsavel = input().split(" ")
    if " ".join([subordinado, responsavel]) == "fim entrada":
        break

    try:
        organograma[responsavel].append(subordinado)
    except KeyError:
        organograma[responsavel] = [subordinado]

def mostra_setor(setor):
    print(setor)

    try:
        for subordinado in sorted(organograma[setor]):
            mostra_setor(subordinado)
    except KeyError:
        return

mostra_setor(input())