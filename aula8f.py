# Inserindo e removendo itens da lista

lista_estados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais']

#o comando append() adiciona um elemento ao final da lista

lista_estados.append('Espirito Santos')
print(lista_estados)

# O comando insert adiciona um elemento na posição indicada no primeiro parâmetro da função

lista_estados.insert(1, 'Paraná') # insere 'Paraná' na posição 1 da lista
print(lista_estados)
lista_estados.insert(3, 'Paraná') # Insere 'Paraná' na posição 3 da lista
print(lista_estados)

# O comando remove exclui a primeira ocorrência do item na lista

lista_estados.remove('Paraná') # removeu a primeira ocorrência do nome Paraná
print(lista_estados)

# O comando pop remove o item de acordo com o indice no parâmetro da função

lista_estados.pop(1) # removeu Rio de Janeiro da lista
print(lista_estados)