while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá{nome}!')

print("nao sera executada!")

x = 0
while x < 100:
    print(x)         # imprimir ate 100
    x = x + 1
print("ACABOU")

# se colocar a palavra: continue ele pula para o proximo laço
xx = 0
while xx < 10:
    if x == 3:
        x = x + 1
        continue

while xx < 10:
    if x == 3:
        x = x + 1
        break

x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e y vale {y}')
        y += 1
    print(x)
    x = x + 1  # ou x += 1

print("acabou")

while True:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('escolha um operador(+ , - , / , * ): ')
    sair = input('Deseja sair: [S] ou [N]')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um  numero.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('operador invalido')