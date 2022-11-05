"""""
Funções - def em python(parte 1)
"""""

def funcao(): # se tiver:  def funcao(msg). ia dar erro pq nao teria valor dentro.
    print('rarikmilkrai')

funcao()  # vai ser repetido 4 vezes o: rarikmilkrai
funcao()
funcao()
funcao()  # a importancia da função é facilitar, tudo que estiver dentro da funçãp
          # as funções sao criadas para vc nao ter que repetir as coisas.

""""
parte 2
"""""
def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2
divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta invalida')


