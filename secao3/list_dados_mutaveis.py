lista = ['ze','maria']
lista2 = lista



lista[0] = 'zezinho'

print(lista2)

# Quando eu faço o que está acima, as duas listas apontam para o mesmos dados, porém, ao alterar a 'lista', a 'lista2' acaba apontando para o mesmo dados que foram alterados. 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#APENAS COPIAR OS DADOS PARA OUTRA LISTA:

lista3 = lista.copy()

lista[1] = 'joao'

print(lista3) # A LISTA3 NAO FOI ALTERADA