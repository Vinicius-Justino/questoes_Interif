valores_varetas = [5, 10, 15, 20, 50]

cont_rodadas = 1
while True:
    jogador_atual = int(input())
    if jogador_atual == -1:
        break

    jogador_atual -= 1
    pontuacoes  = [0, 0, 0]
    for vareta_pega in [int(n) for n in input().split(" ") if n != "-1"]:
        if vareta_pega == 0:
            jogador_atual = (jogador_atual + 1) % 3
            continue

        pontuacoes[jogador_atual] += valores_varetas[vareta_pega - 1]
    
    vencedores = []
    for i in range(3):
        if pontuacoes[i] == max(pontuacoes):
            vencedores.append(i + 1)

    if (cont_rodadas > 1):
        print()

    print(f"RODADA {cont_rodadas}")
    print(f"{'Ganhador' if len(vencedores) == 1 else 'Empate'} com {max(pontuacoes)} pontos")
    for i in range(len(vencedores)):
        print(f"{', ' if i > 0 else ''}Jogador {vencedores[i]}", end="")
    print()

    cont_rodadas += 1