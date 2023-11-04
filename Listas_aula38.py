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


"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

######################################################

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


# usando for
lista = ['rarik', 'monik', 'miguel']

for nome in lista:
    print(nome, type(nome))
    
    """
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))