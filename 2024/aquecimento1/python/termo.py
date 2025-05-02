espiral = [1, 1, 1, 2, 2]
while True:
    try:
        termo = int(input())
        print(espiral[termo - 1])

    except IndexError:
        termo_atual = len(espiral)
        while termo_atual < termo:
            espiral.append(espiral[-1] + espiral[-5])
            termo_atual += 1
        
        print(espiral[-1])
        
    except EOFError:
        break