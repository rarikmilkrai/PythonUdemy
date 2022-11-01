# sem operador ternario

logged_user = True

if logged_user:
    msg = 'Usuario logado'
else:
    msg = 'precisa se logar'
print(msg)

# com operador ternario

logged_user = True
# economiza linhas e fica mais limpo o codigo.
msg = 'usuario logado.' if logged_user else 'usuario precisa se logar.'
print(msg)


# outro caso
idade = 18
demaior = (idade >=18)
msg = 'pode acessar' if demaior else 'nao pode acessar'
print(msg)
