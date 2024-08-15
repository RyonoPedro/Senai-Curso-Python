n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
n3 = float(input('Digite a 3 nota: '))
n4 = float(input('Digite a 4 nota: '))
med = (n1+n2+n3+n4) / 4

if med >= 9:
    print('Aprovado com Louvor')
elif med >= 7:
    print('Aprovado')
elif med >= 5:
    print('Recuperação')
elif med >= 3:
    print('Conselho de classe')
else: 
    print('Reprovado')
    
input('Tecle Enter para encerrar')