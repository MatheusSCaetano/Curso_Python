salas = [

    ['Maria','helena', 'Claudinha'],

    ['Mario'],

    ['bola','ze'], #(0,1,2,3,4)

]

print(salas[0][1])

print(salas[2][1]) #acessando o dado que esta dentro da tupla que esta dentro da lista que esta dentro de outra lista

#tirar a tupla para executar
for sala in salas:
    print(f"A sala é {sala}")
    for aluno in sala:
        print(aluno)