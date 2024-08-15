lista_gatos = []
idade_gatos = []

while True:
    gato = input('Digite o nome do seu gato: ')
    lista_gatos.append(gato)
    idade = int(input('digite a idade do seu gato: '))
    idade_gatos.append(idade)
    resposta = input('Deseja inserir outro gato S/N? ')
    if resposta.upper() == 'N':
        break

print(lista_gatos)
print(idade_gatos)
soma_idades = sum(idade_gatos)
print(f'A soma da idade dos seus gatos é {soma_idades}')

