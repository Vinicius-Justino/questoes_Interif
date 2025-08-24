altura, largura = [int(n) for n in input().split(" ")]

movimentos_horizontais = largura - 1
movimentos_verticais = altura - 1
quadrados = movimentos_horizontais + movimentos_verticais + 1

menor_eixo = min(altura, largura)
maior_eixo = max(altura, largura)
if maior_eixo == (menor_eixo * 2 + 1) or maior_eixo == menor_eixo:
    quadrados -= menor_eixo

print(quadrados)