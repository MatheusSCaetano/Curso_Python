
#num1 = 1
#um2 = 1
#num3 = 1

#if num1 == num2 and num2 == num3 : 
  #  print('Todos os valores sao iguais.')
#else: 
 #   print('Os valores sao diferentes.')    

entrada = input('[E]ntrada | [S]aida')
if entrada == 'E' :
    senha_digitada = input('Digite a senha: ')
    senha_correta = '123'
    if senha_correta == senha_digitada :
        print('Sucesso!')
    else: 
        print('Senha incorreta.')
elif entrada == 'S':
    print('SAIR')
else: 
    print('Voce nao digitou E OU S.')    