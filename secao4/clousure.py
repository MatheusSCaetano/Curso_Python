# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao} {nome}'
#     return saudar #o fechamento da funcao sera feito na chamada


# falar_bom_dia = criar_saudacao('Olá, bom dia!')
# falar_boa_noite = criar_saudacao('Olá, boa noite!')

# print(falar_bom_dia('Matheus')) #adiando o parametro para ser passado aqui
# print(falar_boa_noite('Matheus')) 


# for nome in ['Mario', 'marua', 'zé']:
#     print(falar_boa_noite(nome))


def criar_pessoa():
        def pessoa(nome, idade):
            return f'Nome: {nome} , Idade: {idade}'
        return pessoa
    
create_pessoas = criar_pessoa()

#print(create_pessoas('Matheus', 22))

lista_pessoas = [
    ['mario', 12],
    ['maria', 22],
    ['ze', 31],
]

for nome, idade in lista_pessoas:
    print(create_pessoas(nome,idade)) 
