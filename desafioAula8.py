nome = 'Rarikmilkrai'
idade = 34
altura = 1.70
peso = 78.0
anoAtual = 2022
anoNasc = 1988

idade1 = anoAtual - anoNasc
imc = peso / (altura ** 2)

print('Nome: {} tem {} anos e {:.2f} de altura.'.format(nome, idade, altura))
print('Nascido em: ', anoNasc)
print('com {} anos'.format(idade1))
print(f'pesando:{peso} kg, foi calculado seu imc {imc:.2f}')
