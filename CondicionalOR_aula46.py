nome = input('qual o seu nome? ')
print(nome or 'voce nao digitou nada')
# um codigo bem mais limpo sem tantos if.

# posso usar para checagem
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'rarik'

variavel = a or b or c or d or e or f or g

print(variavel)
#todas serao falsas exceto f e g, no caso ele vai printar a primeira variavel que tiver valor dentro
