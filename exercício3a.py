#faça um programa que recebe quatro notas digitadas pelo user
#usando as quatro notas calcule a média das notas
#o seu programa deve solicitar e imprimir o nome do aluno e sua média

aluno = input('Digite o nome do aluno: ')
n1 = int(input('Digite a 1 nota: '))
n2 = int(input('Digite a 2 nota: '))
n3 = int(input('Digite a 3 nota: '))
n4 = int(input('Digite a 4 nota: '))
média = (n1 + n2 + n3 + n4)//4
print('O aluno', aluno, 'tirou a média de', média)

if média >=5:
    print('Ele passou. Parabéns', aluno)
else:
    print('Ele bombou. Que triste {}'.format(aluno))