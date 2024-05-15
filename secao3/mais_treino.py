

lista = []

while True:
    opcao = input('Digite [i] inserir | [l] listar | [d] deletar')
    if opcao == 'i':
        produto = input('Digite o nome do produto:')
        lista.append(produto)
    elif opcao == 'l':
        for i, nome in enumerate(lista):
            print(i, nome)        
            print('----------')
    elif opcao == 'd':
        try:
            indice = int(input('Digite o indice do produto que quer deletar:'))
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro.')
        except IndexError:
            print("Indice inexistente.")            