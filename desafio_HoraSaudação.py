horario = input('Digite um horario: ')

if horario.isdigit():
    horario = int(horario)

    if horario <= 11:
        print('bom  dia')
    elif horario <= 17:
        print('boa tarde')
    else:
        print('boa noite')

else:
    print("Digite um horario entre 0 e 23")