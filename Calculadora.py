# CALCULADORA COM WHILE

while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    n1_float = 0
    n2_float = 0
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. confira o resultado abaixo: ')
    ###
    if operador == '+':
        print(n1_float + n2_float)
    if operador == '-':
        print(n1_float - n2_float)
    if operador == '/':
        print(n1_float / n2_float)
    if operador == '*':
        print(n1_float * n2_float)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break