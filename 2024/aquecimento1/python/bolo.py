quantidade_fatias = int(input())
precos = [float(preco) for preco in input().split(" ")]

def compara_precos(fatias_restantes):
    global precos

    menor_preco = precos[fatias_restantes - 1]
    if fatias_restantes == 1:
        return menor_preco

    for fatias_proximo_pedido in range(1, fatias_restantes):
        menor_preco = min(menor_preco, precos[fatias_proximo_pedido - 1] + compara_precos(fatias_restantes - fatias_proximo_pedido))

    return menor_preco
    
print(f"{compara_precos(quantidade_fatias):.2f}")