#programa para adivinhar um número sorteado pelo computador.
# nesse jogo o usuário terá três chances de acertar o número.
#a cada erro, o sistema dá uma dica para ajudar o jogador

import random

secret = random.randint(0,10)
print('Jogo Adivinhe o número.')
print('Você terá 3 chances de acertar o meu número.')
print('Boa sorte!')
tentativas = 1
venceu = False

while tentativas <= 3:
    escolha = int(input('Advinhe o número de 0 a 10: '))
    if escolha == secret:
        venceu = True
        break
    elif escolha > secret:
        print('Seu número é maior que o meu número')
        print('Tente novamente')
        tentativas += 1
    else:
        print('Seu número é menor do que o meu número.')
        print('Tente novamente')
        tentativas += 1

if venceu:
    print('PARABÉNS!!! Você acertou o número secreto.')
else:
    print(f'PERDEU!!! O numero sorteado foi {secret}')