jogador1 = input()[2:]
jogador2 = input()[2:]

tabuleiro = [[simbolo for simbolo in input().split(" ")] for _ in range(3)]

def procura_vencedor(tabuleiro):
    for linha in range(len(tabuleiro)):
        sequencia_linha = ""
        for coluna in range(len(tabuleiro)):
            sequencia_linha += tabuleiro[linha][coluna]
        
        if sequencia_linha == "XXX":
            return 0
        elif sequencia_linha == "OOO":
            return 1
        
    for coluna in range(len(tabuleiro)):
        sequencia_coluna = ""
        for linha in range(len(tabuleiro)):
            sequencia_coluna += tabuleiro[linha][coluna]
        
        if sequencia_coluna == "XXX":
            return 0
        elif sequencia_coluna == "OOO":
            return 1
    
    for diagonal in [[range(3), range(3)], [range(3), range(2, -1, -1)]]:
        sequencia_diagonal = ""
        for i in range(3):
            sequencia_diagonal += tabuleiro[diagonal[0][i]][diagonal[1][i]]
        
        if sequencia_diagonal == "XXX":
            return 0
        elif sequencia_diagonal == "OOO":
            return 1
    
    return 2

mensagens = [
    f"{jogador1} Ganhou",
    f"{jogador2} Ganhou",
    "Empatou!"
]

print(mensagens[procura_vencedor(tabuleiro)])