#construa um programa que recebe do usuario o seu nome, valor do salário mínimo atual, e o valor do salário do usuário.
#em seguida calcule quantos salários mínimos o usuário recebe
#imprima o nome do usuário e quantos salarios minimos ele recebe

nome_funcionario = input('Nome do funcionário muito bem pago: ')
salario_minimo = int(input('Salário minimo atual: '))
salario_vendedor = int(input('Ele recebe quanto por mes: '))
valor_acima_do_minimo = salario_vendedor / salario_minimo
print(f'o funcionário {nome_funcionario} recebe cerca de {valor_acima_do_minimo:.1f} salários mínimos')
