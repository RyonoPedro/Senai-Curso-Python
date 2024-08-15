# Crie um programa que solicita o peso em quilos ao usuário e 
# a altura em metros. Em seguida, calcule o IMC desse usuários 
# usando a formula: imc = peso / (altura * altura).
# Utilize a tabela de IMC, imprima em qual categoria o usuário 
# se encontra.

alt = float(input('Digite sua altura: '))
pes = float(input('Digite seu peso:  '))
imc = pes/(alt **2)

if imc >= 40:
    print('você esta com obesidade grau III ou mórbida.')
elif imc >= 35:
    print('você esta com obesidade grau II ou severa.')
elif imc >= 30:
    print('você esta com obesidade grau I. ')
elif imc >= 25:
    print('você esta com sobrepeso.')
elif imc >= 18.6:
    print('você esta com o peso ideal.')
elif imc >= 17:
    print('você esta com magreza leve')
elif imc >= 16:
    print('você esta com magreza moderada')
elif imc <16:
    print('você esta com magreza grave')
    
input('Aperte Enter para encerrar')