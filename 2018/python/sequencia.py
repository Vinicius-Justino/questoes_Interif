maior_inteiro, tamanho_sequencia = [int(n) for n in input().split(" ")]

cont_repeticoes = {}
for _ in range(tamanho_sequencia):
    numero = input()
    try:
        cont_repeticoes[numero] += 1
    except KeyError:
        cont_repeticoes[numero] = 1

contadores = list(cont_repeticoes.values())

def determina_jogada_vencedora():
    global cont_repeticoes, contadores, tamanho_sequencia

    numeros_menor_repeticao = [numero for numero in cont_repeticoes.keys() if cont_repeticoes[numero] == min(contadores)]
    numeros_maior_repeticao = [numero for numero in cont_repeticoes.keys() if cont_repeticoes[numero] == max(contadores)]

    if abs(max(contadores) - min(contadores)) == 1:
        if len(numeros_menor_repeticao) == 1:
            return f"+{numeros_menor_repeticao[0]}"
        elif len(numeros_maior_repeticao) == 1:
            return f"-{numeros_maior_repeticao[0]}"
    elif abs(max(contadores) - min(contadores)) == 2:
        if len(numeros_menor_repeticao) == len(numeros_maior_repeticao) == 1:
            return f"-{numeros_maior_repeticao[0]} +{numeros_menor_repeticao[0]}"
    
    return "*"

print(determina_jogada_vencedora())