# Usando partes da lista

lista_frutas = ['uva', 'banana', 'maça', 'pera', 'abacaxi', 'abacate']

print(lista_frutas[1:3]) # Banana até maça
print(lista_frutas[::-1]) # Tras para frente um por 1

fruta_predileta = lista_frutas[1] 
print(f'Minha fruta predileta é {fruta_predileta}')
copia_frutas = lista_frutas[:] # Com apenas 1 : faz uma copia exata da lista
print(copia_frutas)

num = 1 
for fruta in lista_frutas:
    print(f'{num} - {fruta}')
    num += 1
    
print(len(lista_frutas)) # conta quantos itens tem em uma lista 
print(len('Constitucionalista')) # ou em uma palavra