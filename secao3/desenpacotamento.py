string = 'ABCD'
lista = ['Marta', 'Juliana','Craudin', 1,2,3]

tupla = ['python', 'é', 'legal']

"""
p,b,*__, u = lista
print(p,u)
"""

for nome in lista:
    print(nome, end=(' ')) #o end nao ira quebrar a linha ->  vai apenas colocar um espaço


print(*lista) #faz a mesma coisa que o for acima

