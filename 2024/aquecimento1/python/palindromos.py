entrada = input()

contadores = {}
for letra in entrada:
    try:
        contadores[letra] += 1
    except KeyError:
        contadores[letra] = 1

cont_pares = len(entrada) % 2
for cont in contadores.values():
    cont_pares += (cont + 1) % 2

print(1 if len(contadores.keys()) == cont_pares else 0)