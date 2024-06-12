import copy

d1={
    'nome':'Joao',
    'idade':15,
    'list':[0,1,2]
}


#d2 = d1 # fazendo isso as duas vvvao apontar para o mesmo local da memória => caso altere um dado em uma, alterará na outra


d2 = d1.copy() #=> efetua uma cópia rasa, porém os valores mutáveis recebem apenas o apontamento

d2['list'][0] = 3
# o valor foi alterado nas duas listas, já que as listas sao mutaveis

print(d1)
print(d2)

#PARA ISSO É NECESSÁRIO O - IMPORTAR O METODO COPY - PARA PODER FAZER --> DEEP COPY <-- 

d3={
    'nome':'carlos',
    'idade':16,
    'list':[0,1,2]
}

d4 = copy.deepcopy(d3) # FAREMOS UMA CÓPIA PROFUNDA DOS VALORES SEM APONTAMENTOS

d4['list'][2] = 15

print(d3)
print(d4)

# APENAS O VALOR DA LISTA DO DICIONARIO D4 FOI ALTERADO
