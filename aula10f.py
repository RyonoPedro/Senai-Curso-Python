#Tratamento de erro 

while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(num1 + num2)
        break
    except ValueError:
        print('Erro: Digite apenas números inteiros')
        print('Tente novamente')