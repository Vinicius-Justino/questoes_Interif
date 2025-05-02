organograma = {f"{input()}": []}

while True:
    relacao = input().split(" ")
    if relacao == ["fim", "entrada"]:
        break

    try:
        organograma[relacao[1]].append(relacao[0])
    except KeyError:
        organograma[relacao[1]] = [relacao[0]]
    
def mostra_abaixo(setor):
    print(setor)

    try:
        for setor_abaixo in sorted(organograma[setor]):
            mostra_abaixo(setor_abaixo)
    except KeyError:
        return

mostra_abaixo(input())