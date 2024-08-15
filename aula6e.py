#Usando bloco de repetição para calcular dois números

resposta = 'S'

while resposta.upper() == 'S':
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número:'))
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma}')
    resposta = input('Deseja somar outros números S/N: ')

print('Fim do programa')
