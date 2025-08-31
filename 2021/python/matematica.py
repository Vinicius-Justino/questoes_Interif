numero = int(input())

if numero <= 9999996:
    print(9999997 + ((numero - 1) % 4))
elif numero <= 10000000:
    print(10000000 + (numero % 4))
else:
    print(numero - 3)

# if numero >= 10000000:
#     print(numero - 3)
# else:
#     ate_10_milhoes = ceil((10000000 - numero) / 13)
#     fs_acumulados = ate_10_milhoes * 3
#     numero += 13 * ate_10_milhoes
#     while fs_acumulados > 0:
#         if numero < 10000000:
#             numero += 13
#             fs_acumulados += 3
#         else:
#             numero -= 3
#             fs_acumulados -= 1
#     print(numero)
