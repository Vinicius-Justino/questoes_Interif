preco_pacote = int(float(input()[2:]) * 100)

valores_moedas = [25, 10, 5, 1]
quantidades_moedas = [int(quantidade) for quantidade in input().split(" ")]
dinheiro_total = sum([valores_moedas[i] * quantidades_moedas[i] for i in range(4)])

pacotes_comprados = dinheiro_total // preco_pacote
conta = pacotes_comprados * preco_pacote
for i in range(4):
    while conta >= valores_moedas[i] and quantidades_moedas[i] > 0:
        conta -= valores_moedas[i]
        quantidades_moedas[i] -= 1

print(pacotes_comprados)
print(sum(quantidades_moedas))