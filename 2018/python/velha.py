tabuleiro = [input() for _ in range(3)]

def determina_resultado(tabuleiro):
    for linha in tabuleiro:
        sequencia = ""
        for simbolo in linha:
            sequencia += simbolo
        
        if sequencia == "XXX":
            return "X venceu!"
        elif sequencia == "OOO":
            return "O venceu!"
    
    for coluna in range(3):
        sequencia = ""
        for linha in tabuleiro:
            sequencia += linha[coluna]
        
        if sequencia == "XXX":
            return "X venceu!"
        elif sequencia == "OOO":
            return "O venceu!"
    
    for diagonal in [[[i, i] for i in range(3)], [[i, 2-i] for i in range(3)]]:
        sequencia = ""
        for linha,coluna in diagonal:
            sequencia += tabuleiro[linha][coluna]
        
        if sequencia == "XXX":
            return "X venceu!"
        elif sequencia == "OOO":
            return "O venceu!"
    
    for linha in tabuleiro:
        for simbolo in linha:
            if simbolo == "#":
                return "Jogo em andamento"
    
    return "Velha"

print(determina_resultado(tabuleiro))