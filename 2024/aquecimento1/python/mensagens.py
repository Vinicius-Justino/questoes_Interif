conjuntos = [input(), input()]
conjunto_atual = 0

mensagem = input()
for i in range(0, len(mensagem), 5):
    caracter = int(mensagem[i : i+5], 2)

    if caracter in [27, 31]:
        conjunto_atual = int((caracter == 31))
        continue

    print(conjuntos[conjunto_atual][caracter], end="")

print()
