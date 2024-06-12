def multiplicar_num():
    def multiplicar(num, multiplicador):
        return num * multiplicador
    return multiplicar

numero = multiplicar_num()
print(numero(5,6))


numero_recebido = input('Digite o numero que será multiplicado: ')
multiplicador = input('Digite o multiplicador:')
num_recebido_convvertido = int(numero_recebido)
multiplicador_convertido = int(multiplicador)

resposta_1 = multiplicar_num()
print(resposta_1(num_recebido_convvertido,multiplicador_convertido))

