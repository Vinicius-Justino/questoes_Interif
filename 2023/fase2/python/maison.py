capacidade_mala = int(input())
mala = [int(input()) for n in range(int(input()))]
macos_fora = []

while sum(mala) > capacidade_mala:
    mais_leve = min(mala)

    mala.remove(mais_leve)
    macos_fora.append(mais_leve)

while True:
    mais_leve = min(macos_fora)
    if sum(mala) + mais_leve > capacidade_mala:
        break
    
    macos_fora.remove(mais_leve)
    mala.append(mais_leve)

print(sum(mala))