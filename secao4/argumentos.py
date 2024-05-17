

def soma(x,y,z = None): #definição da funcao
    print(f'{x=} {y=}', '|','x + y = ', (x+y))
    if z is not None:
        print('haha')
    else:
        print('kkk')
        
soma(5,3,2)


soma(y=3, x=5) #especificando o argumenti mesmo fora da ordem de parâmetros

print(1,2, sep ='--')

