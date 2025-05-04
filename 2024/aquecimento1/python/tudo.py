quantidade_canais, bytes_por_slot = [int(n) for n in input().split(" ")]
bytes_por_fluxo = int(input())

canais = []
for i in range(quantidade_canais):
    canais.append([])

canal_atual = 0
bytes_transmitidos = 0
for i in range(bytes_por_fluxo * quantidade_canais):
    numero = int(input())

    canais[canal_atual].append(numero)
    bytes_transmitidos += 1

    if bytes_transmitidos == bytes_por_slot:
        canal_atual = (canal_atual + 1) % 2
        bytes_transmitidos = 0

for canal in canais:
    for byte in canal:
        print(byte)
    
    print(sum(canal) % 256)
