# Função sem argumento e com retorno
import random

def gerar_numero_aleatorio():
    numero_a = random.randint(1, 60)
    return numero_a

while True:
    resposta = input('Deja gerar um número aleatório S/N ')
    if resposta.upper() == 'N':
        break
    else:
        numero = gerar_numero_aleatorio()
        print(f'Número gerado: {numero}')