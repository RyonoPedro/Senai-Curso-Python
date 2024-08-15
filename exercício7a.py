#faça um programa que solicita um numero ao usuario e imprime a tabuada desse 

tabuada = 1
n = int(input('Qual numero você quer ver a tabuada: '))

while tabuada <= 10:
    print(f'{n} x {tabuada} = {n*tabuada}')
    tabuada += 1