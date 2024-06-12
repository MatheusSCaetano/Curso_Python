# Existem funções que executam tarefas -> print

#Existem funções que retornam valores -> return

"""
def soma(x,y):
    return x+y

soma1 = soma(3,6)
soma2 = soma(5,2)

print(soma1 + soma2)

def num(x):
    if x >=10:
        return 'top'
    
numero = num(10)    

print(numero)
"""

def soma(*args): # args vai empacotar o que está sendo envviado para dentro de uma tupla
    total = 0
    for numero in args:
            total += numero
    return total


soamr_total = soma(1,2,3,4,5,6)
print(soamr_total)

numeros = 0,5,6,7,89,2,4
outra_soma = soma(*numeros) # desempacotando a tulpa para usar como parâmetro na função "soma"              
print(outra_soma)