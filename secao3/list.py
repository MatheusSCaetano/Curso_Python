string = 'ABCDE'

lista = []
#print(bool([])) -> falso
#print(lista, type(lista)) -> tipo da lista

lista = [123,True, 'Jose', 1.2,[]]
print(lista)

print(lista[2])

#alterar valor da lista:
lista[2] = 'João'
print(lista)

# variaveis podem receber o valor de uma list
variavel = lista[2]
print(variavel)

#CRUDE

#CREATE:
lista2 = [1,2,3,4]

#UPDATE:
lista2[2] = 6
print(lista2)

#DELETE:
del lista2[2]
print(lista2)

#adicionar dado no final da lista
lista2.append(50)
print(lista2)

#remover do final da lista = pop
lista2.pop() # removve o ultimo item da lista
print(lista2)

