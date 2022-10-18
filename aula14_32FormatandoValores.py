""""
Formatando valores com modificadores

:s - texto(strings)
:d - Inteiros(int)
:f - numeros de ponto flutuante(float)
:.(numero)f- quantidade de casas decimais (float)
:(caractere) (> ou< ou ^)(quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro

"""""

num1 = 3
num2 = 10
divisao = num1 / num2
print(f'{divisao:.2f}')

nome = 'rarikmilkrai souza'
print(f'nome:s') #so estou informando que é uma string

num_1 = 1
print(f'{num_1:0>10}') #aqui vai criar 09 zeros a esquerda do numero 10 contando com a variavel

num_2 = 1160
print(f'{num_2:0<8}')

num3 = 1150
print(f'{num3:0^10}')

print(f'{nome:#^30}') # meu nome no centro e 30 cerquilhas na esquerda e direita

nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome_formatado = '{n} {n}'.format(n=nome)
print(nome_formatado)

nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

sobrenome = 'jose souza'
nome_formatado = '{0:$>50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

nome1 = 'Rarikmilkrai'
nome1 = nome1.ljust(50, '#')
print(nome1)
print(nome1.lower()) # tudo minusculo
print(nome1.upper()) # tudo maiusculo
print(nome.title()) # primeiras letras maiusculas