placar = {}

while True:
    nome_pais = input()
    if nome_pais == "FIM":
        break

    ouro,prata,bronze = [int(n) for n in input().split(" ")]

    placar[nome_pais] = {
        "ouro": ouro,
        "prata": prata,
        "bronze": bronze
    }

colocacao = 1
while len(placar) > 0:
    criterios_desempate = ["ouro", "prata", "bronze"]
    melhores = placar.keys()

    for criterio in criterios_desempate:
        mais_medalhas = max([placar[pais][criterio] for pais in melhores])
        melhores = [pais for pais in melhores if placar[pais][criterio] == mais_medalhas]

        if len(melhores) == 1:
            break
    
    for pais in sorted(melhores):
        print(f"{colocacao}: {pais}")
        placar.pop(pais)

    colocacao += 1