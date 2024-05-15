
import re
import sys
import random

nove_digitos = ''
for i in range(9): # fazendo um for 9 vezes
    nove_digitos += str(random.randint(0,9)) # "nove-digitos" recebendo numeros aleatorios entre 1 e 9 


contador_regressivo = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo #pegando a variavel nove_digitos, acessando pelo for e transformando em int para podermos multiploicar os valores e ja somando com os proximos (+=)
    contador_regressivo -=1

digito = (resultado * 10) % 11    
digito = digito if digito <= 9  else 0 #(digito = digito se digito <= 9 else digito = 0) 


#gerando o segundo digito:

dez_digitos = nove_digitos + str(digito)

contador_regressivo = 11
resultado2 = 0

for digito2 in dez_digitos:
    resultado2 += int(digito2) * contador_regressivo
    contador_regressivo -+1

digito2 = (resultado2 * 10) %11
digito2 = digito2 if digito2 <= 9 else 0 

print(f'{nove_digitos}{digito}{digito2}')