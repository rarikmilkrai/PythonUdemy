if True:
    print("verdadeiro.")

print('A minha expressao nao é verdadeira')  # como esta fora do bloco if vai executar a segunda opção

if False:  # quando há um bloco dizendo que é falso, imediatamente se passa para o proximo bloco
    print("verdadeiro.")
elif True:
    print("Agora é verdadeiro")
elif False:
    print('mais uma verdadeira')
else:
    print