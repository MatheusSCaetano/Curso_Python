#create:
nome = ['Matehus','Julio', 'Junior']

nome.append('Mariazinha') #inserir no final
print(nome)

#update:
nome.insert(0,'cascao') # inserir em qualquer lugar movvendo os outros indices 
print(nome)

#delete:
del nome[1] #deletando o indice desejado

# nome.clear() limpar todos os valores da lista
print('i', nome)


# mostrar toda a lista
indices = range(len(nome))  #pegando os numeros de cada indice e enumerando

for item in indices:
    print(item, nome[item])


    #enumerate faz tbm:
#for item in enumerate(nome):
 #       indice, nome = item # isso pode ir ali encima como poderemos ver abaixo:
  #      print(indice,' - ', nome)

for indice, nome in enumerate(nome):
      print(indice, ' // ', nome)
      
