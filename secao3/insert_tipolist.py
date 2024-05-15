"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
"""
lista = ['Joao','Ze', 'Xuxa', 'Mariazinha']
print(lista)

lista.append('Cascao') #inserir no ultimo indice
print(lista)

lista.pop() #deleta o ultimo dado da lista
print(lista)

del lista[2] # deleta o indice indicado 
print(lista)

# lista.clear() -> limpa a lista

#insert: 
lista.insert(0, 'Lula') #(indice, dado)
print(lista)
# o insert pode inserir o dado no lugar de outro sem apagar esse outro, apenas move-lo
lista.insert(1, 'Lula')
print(lista) #inseriu o dado no indice e moveu os outros uma cada a direita na lista
"""
#concatenando listas:

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_a , '\n')
print(lista_b , '\n')
print(lista_c )

#metodo extend:
lista_a.extend(lista_b)
print(lista_a) # a lista A foi extendida recebendo os valores da lista B