tamanho_sequencia = int(input())
sequencia = [int(n) for n in input().split(" ")]
maiores_subsequencias = [1] * tamanho_sequencia

for i in range(tamanho_sequencia):
    maiores_subsequencias[i] = max([maiores_subsequencias[j] for j in range(i) if sequencia[j] < sequencia[i]], default=0) + 1

print(max(maiores_subsequencias))