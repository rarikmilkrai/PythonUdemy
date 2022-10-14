
num = input('Digite um numero inteiro: ')


if not num.isdigit(): # confere se é numero inteiro caso digite uma letra.
    print('Isso nao é um numero inteiro.')

else:
    num = int(num)

    if not  num % 2 == 0:
        print(f'{num} é ímpar')
    else:
        print(f'numero é par')


