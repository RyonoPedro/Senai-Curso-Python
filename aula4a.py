nome_vendedor = input('digite o nome do vendedor: ')
modelo_carro = input('digite o modelo do carro vendido: ')
salario = float(input('digite o salário do vendedor: '))
qtde_vendido = int(input('quantos carros foram vendidos: ')) 
valor_carro = float(input('qual o valor do carro vendido: '))
comission = float(input('qual porcentagem de comissão: '))
comission /= 100 #comissao = comissao / 100
total_vendido = valor_carro * qtde_vendido
valor_comission = total_vendido * comission
salario_receber = salario + valor_comission
print(f'O vendedor {nome_vendedor} recebera R${salario_receber:.2f} de salário esse mes.')
print(f'Ele vendeu {qtde_vendido} carros do modelo {modelo_carro} cujo o valor é de {valor_carro} assim rendendo {total_vendido} para a companhia Letal')
print('ps não toque o sino do vendedor varias vezes')
 
