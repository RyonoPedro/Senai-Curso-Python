#Trabalhando com a função main() para organizar ocódigo
# Função para calcular o juros composto

def main():
    
    print('Calculadora de juros composto')
    valor_presente = float(input('Digite o valor do emprestimo: '))
    taxa_juros = float(input('Digite a taxa de juros: '))
    tempo_periodos = int(input('Digite o número de parcelas: '))
    
    montante_final = calcular_juros_composto(valor_presente, taxa_juros, tempo_periodos)
    
    valor_parcelas = montante_final / tempo_periodos
    print(f'Valor de cada parcela: R$ {valor_parcelas:.2f}')
    print(f'Montante Final: R$ {montante_final:.2f}')
    
def calcular_juros_composto(vp, j, p):
    # vp = valor presente
    # j = taxa de juros
    # p = tempo em períodos
    
    juros_decimal = j / 100
    expoente = p
    valor_final = vp * (1+juros_decimal)** expoente
    
    return valor_final
    
main()
        