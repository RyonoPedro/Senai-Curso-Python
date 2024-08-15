#simulando um sistema de pagamento 
print('''Forma de Pagamento
1 - Cartão de Crédito
2 - Boleto Bancário
3 - Dinheiro
4 - PIX ''')

pgmt = int(input('Escolha o método de pagamento: '))

if pgmt == 1 or pgmt == 4:
    print('Processando pagamento...')
    contato_banco = True
    if contato_banco:
        print('Transação Aprovada')
    else:
        print('Erro com o pagamento. Contate sua operadora ou banco')
    
elif pgmt == 2:
    print('Você receberá o boleto no seu endereço')
    
elif pgmt == 3:
    print('Transação Aprovada')
    
else:
    print('Método de pagamento inválido. Tente novamente')
