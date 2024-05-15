#while -> enquanto

"""""
i = 0
while i < 10 : 
    print('Matheus')
    i += 1
"""
#contador = 0

#while contador < 10000000 :
#    contador+=1
#    print(contador)
senha_correta = '123'
acesso = input('[E]ntrar / [S]air')

while acesso != 'E' and acesso != 'S':
    acesso = input('[E]ntrar / [S]air')
    break
if acesso == 'E':
    senha_digitada =input('Digite a senha de acesso: ')
    while senha_correta != senha_digitada:
        senha_digitada =input('Senha incorreta! Digite novamente a senha de acesso: ')
        if senha_digitada == senha_correta:
            print('Acesso permitido!')
            break
else:
    print('Saindo...')