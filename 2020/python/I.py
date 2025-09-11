numeros = [int(n) for n in input().split(" ")]
numeros.append(1)

coeficientes = [
    [5, 5, 3, 4],
    [25, 25, 13, 34],
    [129, 129, 64, 226],
    [681, 681, 321, 1388],
    [3653, 3653, 1683, 8240]
]

conta = numeros[0] % 5
print(sum([numeros[i] * coeficientes[conta][i] for i in range(4)]))