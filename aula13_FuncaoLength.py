# so funciona com string e nao com tipos numericos

usuario = input('Digite seu nome: ')
qtd_caracters = len(usuario)

print(f'{usuario}', qtd_caracters)

# podemos somar a quantidade de caracteres tb
string1 = input('Digite seu primeiro nome')
string2 = input('Digite o seu segundo nome')

print(f'a quantidade de caracteres foi {len(string1) + len(string2)}')


