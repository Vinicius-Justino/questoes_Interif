capacidade_mala = int(input())
mala = [int(input()) for n in range(int(input()))]
macos_fora = []

while sum(mala) > capacidade_mala:
    mais_leve = min(mala)

    mala.remove(mais_leve)
    macos_fora.append(mais_leve)

while len(macos_fora) > 0:
    menor_maco = macos_fora.pop(0)
    if sum(mala) + menor_maco > capacidade_mala:
        break

    mala.append(menor_maco)

print(sum(mala))
