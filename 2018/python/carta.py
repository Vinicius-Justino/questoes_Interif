sequencia = input()

dimensoes_matriz = int(len(sequencia)**0.5)

if len(sequencia) / dimensoes_matriz == dimensoes_matriz:
    mensagem = ""
    for i in range(0, len(sequencia), dimensoes_matriz + 1):
        mensagem += sequencia[i]
    
    print(mensagem)
else:
    print("invalido")