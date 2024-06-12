

pessoa = {
    'nome': 'Zé',
    'idade': 15,
}

pessoa.setdefault('sobrenome', None) # Seta uma chave no seu dicionario com um valor padrão (caso a chave não exista)

print(len(pessoa)) #mostra o tamanho do dicionario

print(list(pessoa.keys())) # keys => retorna as chaves do dicionario (convertemos em lista para poder manipular)
print(list(pessoa.values()))#values => retorna os valores do dicionario

print(pessoa)