lista = [
    ['rarik', 'rarikmilkrai', 'monik'],
    ['debora', 'carlos', 'matheus'],
    ['felix', 'monica', 'cicero']
]
enumerada = enumerate(lista)
print(list(enumerada))

# caso queira colocar essa lista dentro de uma variavel so fazer assim:
enumerada = list(enumerate(list))
print(enumerada[1][1][2]) # lista 1, posição 1 e posição 2
