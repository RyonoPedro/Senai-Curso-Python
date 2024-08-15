# Lista mista

jogador = [2, 'Gaspar', 9.5, True]

print(type(jogador))
print(type(jogador[0]))
print(type(jogador[1]))
print(type(jogador[2]))
print(type(jogador[3]))

print('=========================')
print(f'Posição do jogador: {jogador[0]}')
print(f'Nome do jogador {jogador[1]}')
print(f'Nota do jogador: {jogador[2]}')

if jogador[3]:
    print('O jogador terminou a competição')
else:
    print('O jogador não terminou a competição')

