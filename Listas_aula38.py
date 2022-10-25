lista = ['A', 'B', 'C', 'D', 'E']
print(lista[:2])
print(lista[::-1])

l1 = [1,2,3]
l2 = [4,5,6]


print(l2)
l2.insert(0, 'rarikmilkrai')
print(l2)
l2.pop() #remove um elemento
print(l2)

l2 = [1,2,3,4,5,6,7,8,9]
del (l2[3:5])  #excluindo o 4 e 5 lembrando que a contagem começa em 0

l2.insert(0, 'Banana')
print(l2)
del(l2[0])
print(l2)

#caso queira pegar o maximo valor
print(max(l2))
print(min(l2))


#jogo de advinhação

secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma Letra: ')

    if len(letra) > 1:
        print('Ahhhh isso não vale, digite apenas uma letra. ')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhulllll, a letra"{letra}" existe na palavra secreta.')
        print('------------------------------------------------------')
    else:
        print(f'Poxa vida a letra: "{letra}" NÃO EXISTE na palavra secreta.')
        print('-----------------------------------------------------------')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!!! A palavra era: {secreto_temporario}')
    else:
        print(f'Apalavra secreta está assim: {secreto_temporario}')
