""""
*String indices
fatiamento de strings[inicio:fim:passo]
funções built-in len, abs, type, print...]
"""""
# positivos [012345678]
texto     = 'Python s2'

print(texto[3]) #imprime o indice de acordo, no caso vai ser o "h"

# negativos
texto1 = "python s2"
#       -[9876543210]

nova_string = texto[1:7] # fatiando uma string pegando os indices
print(nova_string)

nova_string1 = texto1[7:]  # começa pelo indice 7 e vai ate o final

print(len(texto1))
