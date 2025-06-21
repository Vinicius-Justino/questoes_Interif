padrao_ideal = [int(tipo) for tipo in input().split(" ")]

similaridades = []
for i in range(int(input())):
    tubo = [int(tipo) for tipo in input().split(" ")]
    jujubas_similares = sum([1 if tubo[tipo] == padrao_ideal[tipo] else 0 for tipo in range(8)])

    similaridades.append(jujubas_similares / 8 * 100)

for i in range(int(input())):
    similaridade_minima = int(input())
    tubos_similares = sum([1 if similaridades[tubo] >= similaridade_minima else 0 for tubo in range(len(similaridades))])
    print(f"{(tubos_similares / len(similaridades) * 100):.2f}")