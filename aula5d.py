
idade = int(input('digite sua idade: '))

if idade >= 18:
    print('você ja pode tirar a carta de motorista')
    print('dirija-se a uma auto escola mais próxima')
else:
    print('você não pode tirar a carta de motorista')
    print(f'espere mais {18-idade} anos.')

print('''fim do programa
Document results''')