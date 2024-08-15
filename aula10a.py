# Tuplas: são estruturas de dados imutáveis, ou seja, seu conteúdo
# não pode ser alterado

minha_tupla = (1, 2, 3, 4, 5)
print(type(minha_tupla))
print(minha_tupla)

for i in minha_tupla:
    print(i)

# Acessando elementos da tupla
print(minha_tupla[1:3]) # 2, 3
print(minha_tupla[0]) # 1
print(minha_tupla[-1]) # 5 --  - significa tras para frente
print(minha_tupla[:3]) # 1, 2, 3 -- nada na esquerda apos 2 pontos entende como 0
print(minha_tupla[2:]) # 4, 5 nada na direita vai até o final
