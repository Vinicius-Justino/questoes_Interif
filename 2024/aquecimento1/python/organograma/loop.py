organograma = {f"{input()}": []}

while True:
    relacao = input().split(" ")
    if relacao == ["fim", "entrada"]:
        break

    try:
        organograma[relacao[1]].append(relacao[0])
    except KeyError:
        organograma[relacao[1]] = [relacao[0]]

saida = [input()]
while len(saida) > 0:
    setor_atual = saida.pop(0)
    print(setor_atual)

    try:
        for setor_abaixo in reversed(sorted(organograma[setor_atual])):
            saida.insert(0, setor_abaixo)
    except KeyError:
        continue