# Operadores Lógicos: and(e), or(ou), not(nao)

idade = int(input('Digite sua idade: '))
sexo = input('Qual seu sexo M/F: ')

if idade == 18 and sexo.upper() == 'M':
    print('''Você está na fase do exército, poderá servir.
Procure uma base militar para fazer o alistamento''')

elif idade < 18 or idade > 18:
    print('Você não está na fase do exército')
    
elif not(sexo.upper() == 'M'):
    print('Mulheres não se alistam para o serviço militar nesse país')
    