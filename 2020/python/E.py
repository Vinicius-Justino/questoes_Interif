quantidade_operacoes = int(input())
conta = input()
resposta_joca = int(input())

"""
resultado = eval(conta)

erro_comum = int(conta[0])
for i in range(1, len(conta), 2):
    erro_comum = eval(f"{erro_comum}{conta[i]}{conta[i + 1]}")
"""

erro_comum = int(conta[0])
termos = [int(conta[0])]
for i in range(1, len(conta), 2):
    numero = int(conta[i + 1])
    if conta[i] == "+":
        termos.append(numero)
        erro_comum += numero
    else:
        termos[-1] *= numero
        erro_comum *= numero

resultado = sum(termos)

if resposta_joca == resultado:
    print("Correto, Joca!")
elif resposta_joca == erro_comum:
    print("Multiplicar antes de somar, Joca.")
else:
    print("Errado.")