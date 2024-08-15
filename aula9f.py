# Função com argumento e com retorno

def classificar_triangulo(l_a,l_b,l_c):
    
    if l_a == 0 or l_b == 0 or l_c == 0:
        mensagem = 'Triângulo Inválido. Todos os lados devem ser maiores do que 0'
    elif l_a == l_b and l_b == l_c:
        mensagem = 'Triângulo Equilátero'
    elif l_a == l_b or l_b == l_c or l_a == l_c:
        mensagem = 'Triângulo Isósceles'
    else:
        mensagem = 'Triângulo Escaleno'

    return mensagem

print('Classificação de Triângulos')
l_1 = float(input('Digite o comprimento do 1 lado: '))
l_2 = float(input('Digite o comprimento do 2 lado: '))
l_3 = float(input('Digite o comprimento do 3 lado: '))

classificacao = classificar_triangulo(l_1,l_2,l_3)

print(f'os lados informados formam um {classificacao}')