nomes = ['Matheus', 'Zé', 'joao']
nome1,nome2,nome3 = nomes

print(nome2)

#pegar um valor especifico

_, nome2, *_ = ['Maria', 'ze', 'joao'] # nome1 recebeu a primeira variavel e a variavel resto tem uma lista dentro dela com o resto todo da lista.

print(_) # a variavel resto que nao sera utilizada foi transformada em '_'.

print(nome2)