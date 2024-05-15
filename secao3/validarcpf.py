"""
cpf = [7,4,6,8,2,4,8,9,0]

i = 0
multiplicador = 10

while i <= 8:
    cpf[i] = cpf[i] * multiplicador
    i +=1
    multiplicador -=1

for num in cpf:
    print(num)

soma = 0
i=0
while i <= 8:
    soma = soma +cpf[i] 
    i = i+1
    if i == 9:
        break       

soma = soma *10

soma = soma % 11

print(f'Primeiro digito: {soma}')

digitos = []
if soma <= 9:
    digitos.append(soma)
else: 
    digitos.append(0)
print(digitos[0])
"""

#resolução do professor: 

import re
import sys

entrada = input("CPF:")

cpf = re.sub(
    r'[^0-9]', #Substituir tudo que não for numero "^" entre o indice 0 e 9
    '',    #por nada
    entrada
)

entrada_e_sequencial= entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Voce enviou dados sequenciais')
    sys.exit()

print(cpf) #podemos verificar aqui que o cpf continua no padrão


nove_digitos = cpf[:9] #pegando os primeiros 9 indices/ digitos do cpf
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

cpf_gerado_pelo_calculo = (f'{nove_digitos}{digito}{digito2}')

if cpf_gerado_pelo_calculo != cpf:
    print('CPF inválido')
else:
    print('CPF validado.')