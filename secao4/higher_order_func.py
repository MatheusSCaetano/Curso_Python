

#FUNÇÕE DE PRIMEIRA CLASSE


def saudacao(mensagem):
    return 'Oi' +' ' +  mensagem 

print(saudacao('Você é legal'))


saucadao2 = saudacao

msg = saucadao2('BOA TARDE')

print(msg)



def executa(funcao, msg): #uma func e uma coisa qualquer como parametro        
    return funcao(msg) # function que retorna outra function

msg = executa(saudacao, 'BOM DIA!')  #executando a func e a msg

print(msg)