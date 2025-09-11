from copy import deepcopy

for resto_divisao in range(5):
    dimensoes_tabela = resto_divisao + 3

    tabela = [[{"dia": 0, "mes": 0, "ano": 1, "acrescimo": 0}, {"dia": 0, "mes": 1, "ano": 0, "acrescimo": 0}],
              [{"dia": 1, "mes": 0, "ano": 0, "acrescimo": 0}]]
    
    while len(tabela[0]) < dimensoes_tabela:
        novo_valor = deepcopy(tabela[0][-1])
        novo_valor["acrescimo"] += len(tabela[0])
        tabela[0].append(novo_valor)
    
    while len(tabela) < dimensoes_tabela:
        novo_valor = deepcopy(tabela[-1][0])
        novo_valor["acrescimo"] += len(tabela)
        tabela.append([novo_valor])
    
    for linha in range(1, dimensoes_tabela):
        for coluna in range(1, dimensoes_tabela):
            novo_valor = {"dia": 0, "mes": 0, "ano": 0, "acrescimo": 0}

            for mod_coords in [[-1, -1], [-1, 0], [0, -1]]:
                novo_valor["dia"] += tabela[linha + mod_coords[0]][coluna + mod_coords[1]]["dia"]
                novo_valor["mes"] += tabela[linha + mod_coords[0]][coluna + mod_coords[1]]["mes"]
                novo_valor["ano"] += tabela[linha + mod_coords[0]][coluna + mod_coords[1]]["ano"]
                novo_valor["acrescimo"] += tabela[linha + mod_coords[0]][coluna + mod_coords[1]]["acrescimo"]
            
            tabela[linha].append(novo_valor)
    
    numero_premiado = tabela[-1][-1]
    print(f"Tabela {dimensoes_tabela}x{dimensoes_tabela}: {numero_premiado['dia']}d + {numero_premiado['mes']}m + {numero_premiado['ano']}a + {numero_premiado['acrescimo']}")