# Exeções de Erro: são eventos que sinalizam que algo deu errado
# durante a execução do programa. Esses erros interrompem o fluxo
# normal e exigem algum tratamento específico

try:
    numero = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    divisao = numero / numero2
    print(f'A divisão dos números é {divisao}')
except ValueError as excecao:
    print(f'Digite apenas numeros inteiros.')
    print(f'Persistindo o erro, informe ao programador a mensagem: ')
    print(excecao)
except ZeroDivisionError:
    print('Não é possível dividir por zero.')