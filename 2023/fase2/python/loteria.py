def fatorial(x):
    return 1 if x <= 1 else x * fatorial(x - 1)

def arranjo(n, p):
    cancela = max(p, n - p)
    divide = min(p, n - p)

    n_fatorial = 1
    for fator in range(n, cancela, -1):
        n_fatorial *= fator
    
    return n_fatorial / fatorial(divide)

max_numeros, min_escolha, max_escolha, preco = input().split(" ")
max_numeros = int(max_numeros)
min_escolha = int(min_escolha)
max_escolha = int(max_escolha)
preco = float(preco)

total_possibilidades = arranjo(max_numeros, min_escolha)

for escolha in range(min_escolha, max_escolha + 1):
    possibilidades_escolha = arranjo(escolha, min_escolha)

    probabilidade_fracao = round(total_possibilidades / possibilidades_escolha)
    probabilidade_decimal = possibilidades_escolha / total_possibilidades
    valor_aposta = possibilidades_escolha * preco

    print(f"Quantidade numeros jogados: {escolha}")
    print(f"Probabilidade: 1 em {probabilidade_fracao}")
    print(f"Probabilidade: {(probabilidade_decimal * 100):.6f} %")
    print(f"Valor aposta: {possibilidades_escolha} X R$ {preco:.2f} = R$ {valor_aposta:.2f}")

    if escolha < max_escolha:
        print()