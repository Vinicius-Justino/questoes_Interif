quantidade_equipes = int(input())
quantidade_jogos = int(input())

placar = {}
for jogo in range(quantidade_jogos):
    time1, gols1, x, gols2, time2 = input().split(" ")
    gols1 = int(gols1)
    gols2 = int(gols2)

    try:
        placar[time1]["saldo"] += gols1 - gols2
    except KeyError:
        placar[time1] = {
            "pontos": 0,
            "vitorias": 0,
            "saldo": gols1 - gols2
        }
    
    try:
        placar[time2]["saldo"] += gols2 - gols1
    except KeyError:
        placar[time2] = {
            "pontos": 0,
            "vitorias": 0,
            "saldo": gols2 - gols1
        }
    
    if gols1 > gols2:
        placar[time1]["pontos"] += 3
        placar[time1]["vitorias"] += 1
    elif gols2 > gols1:
        placar[time2]["pontos"] += 3
        placar[time2]["vitorias"] += 1
    else:
        placar[time1]["pontos"] += 1
        placar[time2]["pontos"] += 1

while len(placar) > 0:
    times = list(placar.keys())
    melhor_time = times.pop(0)

    for time in times:
        criterios_desempate = ["pontos", "vitorias", "saldo"]
        while True:
            criterio = criterios_desempate[0]
            if placar[time][criterio] == placar[melhor_time][criterio]:
                criterios_desempate.pop(0)
                continue

            if placar[time][criterio] > placar[melhor_time][criterio]:
                melhor_time = time
            
            break
    
    stats_melhor_time = placar.pop(melhor_time)
    print(f"{melhor_time} {stats_melhor_time['pontos']} {stats_melhor_time['vitorias']} {stats_melhor_time['saldo']}")