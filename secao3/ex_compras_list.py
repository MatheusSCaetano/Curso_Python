"""
FAÇA UMA LISTA DE COMPRAR COM LISTAS
O USUARIO DEVE TER A POSSIBILIDADE DE
INSERIR, APAGAR, LISTAR VVALORES DA SUA LISTA
NAO PERMITA QUE O PROGRAMA QUEBRE COM
ERROS DE INDICES INEXISTENTES NA LISTA
"""
import os
lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]inserir | [a] apagar | [l]listar: ')

    if opcao == 'i':
        #os.system('clear') #limpar terminal
        valor = input('Digite o nome do produto:')
        lista.append(valor)
    elif opcao == 'a':
        try: #serve para colocar o except e corrigir um erro.
            indice_str = input('Digite o numero do produto que ira apagar: ')    
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um numero intero.')
        except IndexError:
            print('Esse indice nao existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nao ha itens na lista')
        for indice, nome in enumerate(lista):
           print(indice, nome)                  
    else:
         print('Escolha uma opção')