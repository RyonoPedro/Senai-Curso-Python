# função sem parametros/argumentos e sem retorno

def imprimir_texto():
    print('É PIQUE')
    print('...')

def mensagem_positiva():
    print('Levanta, sacode a poeira')
    print('Dá a volta por cima')
    
nome = input('Digite seu nome: ')
resposta = input('É seu aniversário S/N? ')
    
if resposta.upper() == 'S':
    for i in range(5):
        imprimir_texto()
else:
    mensagem_positiva()