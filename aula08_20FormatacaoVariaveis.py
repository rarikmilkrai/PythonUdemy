nome = 'Rarikmilkrai'
print(nome)

idade = 34
altura = 1.70
e_maior = idade > 18
peso = 80
print('nome: ', nome)
print('idade: ', idade)
print('altura: ', altura)
print('é maior?: ', e_maior)


imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc))
