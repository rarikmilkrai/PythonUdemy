string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista = string.split(' ')

print(lista)

lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

for valor in lista1:
    print(f' a palavra {valor} apareceu {lista1.count(valor)} vezes')

# função JOIN tem como objetivo juntar as listas exemplo:
string2 = 'O Brasil é penta.'
lista3 = string.split(' ')
string3 = ','.join(lista)
print(string3)

# função enumerate ela desempacota a lista.

for indice, valor in enumerate(lista3):
    print(indice, valor, lista3[indice])

