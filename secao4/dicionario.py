
#pessoa1 = dict(nome='Matheuis', sobrenome='Caetano')

#-------------------------------------------------------------------
# pessoa = {
#     'nome': 'Matheus',
#     'sobrenome': 'Caetano',
#     'idade': 22,
#     'CPF': '07785581185',
#     'enderecos':[
#         {'rua': '123', 'bairro': 'santo amaro'},
#         {'rua': '1234', 'bairro': 'santo ze'},
#     ],
# }

# print(pessoa)
# print(' ')

# print(pessoa['nome'])
# print(' ')

# for chave in pessoa:
#     print(chave,':', pessoa[chave])

#-------------------------------------------------------------------


#chave dinamica:

#create:
chave = 'nome'
chave_sobrenome = 'sobrenome'
pessoa = {}

pessoa[chave] = 'Matheus'
pessoa[chave_sobrenome] = 'Caetano'


print(pessoa[chave_sobrenome])

del pessoa[chave_sobrenome]

print(pessoa)


if pessoa.get(chave_sobrenome) is None:
    pessoa[chave_sobrenome] = 'Caetano'
else:
    print(pessoa[chave_sobrenome])

print('isso:', pessoa)    