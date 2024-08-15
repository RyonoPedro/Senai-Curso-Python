# Função com argumento e sem retorno

def soma(x, y):
    total = x + y
    print(f'A soma dos números é {total}')

while True:
    x = int(input('Digite um número inteiro: '))
    y = int(input('Digite outro número inteiro: '))
    soma(x,y)
    resposta = input('Deseja fazer outro calculo S/N? ')
    if resposta.upper() == 'N':
        break
print('Fim do Programa')