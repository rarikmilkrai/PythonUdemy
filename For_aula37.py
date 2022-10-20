texto = 'Rarikmilkrai'
novastring = ''
print('-----------------------------------------------------------------')
for letra in texto:
    print(letra)
print('-----------------------------------------------------------------')
for numero in range(10):
    print(numero)
print('-----------------------------------------------------------------')
# range(start=0, stop, step=1)

for n in range(0, 10, 1):
    print(n)
print('-----------------------------------------------------------------')

for n in range(20, 10, -1):
    print(n)
    print('-----------------------------------------------------------------')

for n in range(0, 100, 8):
    print(n)

print('-----------------------------------------------------------------')

for n in range(100):
    if n % 8 == 0:
        print(n)
print('-----------------------------------------------------------------')

for letra in texto:
    if letra == 't':
        novastring = novastring + letra.upper()
    else:
        novastring += letra.upper()


# c = 0
# while c < len(texto):
#     print(texto[c])
#  c += 1