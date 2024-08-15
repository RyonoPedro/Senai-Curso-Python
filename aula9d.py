# Função com argumento e com retorno

def calcular_area_retangulo(base, altura):
    area = base*altura
    return area

tamanho_base = float(input('Digite o tamanho da base do retângulo: '))
tamanho_altura = float(input('Digite o tamanho da altura do retângulo: '))
area_retangulo = calcular_area_retangulo(tamanho_base, tamanho_altura)
print(f'A área do retângulo é {area_retangulo}')