# Tratamento de erro

try:
    valor = input('Digite um número: ')
    numero = int(input('Digite outro número: '))
    total = valor + numero
    print(f'{total}')
except Exception as excecao:
    print(f'Erro: informe a mensagem abaixo ao suporte:\n{excecao}')
