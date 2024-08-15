idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('você é uma criança')
elif idade <=17:
    print('você é um adolescente ')
elif idade <=64:
    print('você é um adulto')
else:
    print('você é idoso')
    
input('insira qualquer tecla para encerrar')