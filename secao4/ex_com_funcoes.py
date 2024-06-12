

#crie func que multiplica os argumentos não nomeados recebvidos
#retorne o total em uma variavel e mostre o valor

#criar funçãp retornar se o num é par ou impar


def multip (*args):
    total = 1
    for numero in args:
        total *=numero
    return total
    
valortotalmult = multip(7,7,7,7) 
print(valortotalmult)   

def denifir_par_impar(num):
    if num % 2 == 0: 
        return f'{num} é par'
    
    return f'{num} é ímpar'
    

numero_par_ou_impar = denifir_par_impar(valortotalmult)

print(numero_par_ou_impar)