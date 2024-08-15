# Dicionários: são estruturas de dados formadas por
# chave e valor, organizando as informações de forma
# eficiente

meu_dic = {'nome':'Gaspar', 'idade': 8, 'pelo': 'Curto', 'cor': 'cinza'}
print(meu_dic)

print(f'Nome do Gato: {meu_dic["nome"]}')
print(f'Idade do Gato: {meu_dic["idade"]}')
print(f'Pelagem do Gato: {meu_dic["pelo"]}')
print(f'Cor do Gato: {meu_dic["cor"]}')

# Mudando o valor do dicionário
meu_dic['idade'] = 10
print(meu_dic['idade'])

# Adiciona uma chave com valor no dicionário
meu_dic['sexo'] = 'Masculino'
print(meu_dic)

# Exclui elemento do dicionário
del meu_dic['pelo']
print(meu_dic)

# Imprimindo cada chave do dicionário
for chave in meu_dic:
    print(f'Chave: {chave}')
    
# Imprimindo cada valor do dicionário
for valor in meu_dic.values():
    print(f'Valor: {valor}')

# Imprimindo chave e valor 

for x, y in meu_dic.items():
    print(f'Chave: {x} - Valor: {y}')