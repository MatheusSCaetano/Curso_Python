frase = 'hoje eu acordei com o pé direito'

lista_palavras = frase.split() #cada espaco corta as palavaras em indices da lista

print(lista_palavras)
print(lista_palavras[1])

for i, frase in enumerate(lista_palavras):
    print(i, frase)
