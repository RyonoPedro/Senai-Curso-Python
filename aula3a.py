print('Curso de Fundamentos do Python 1')

escola = 'Senai Celso Charuri'

nome_aluno = input('Qual seu nome: ')

print(f'{nome_aluno} a escola, {escola} tem vagas para o curso de python')

ano_atual = 2024
dia_atual = 5
mes_atual = 8
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
mes_aniversario = int(input('Digite o mes do seu aniversário: '))
dia_aniversario = int(input('Digite o dia do seu aniversário: '))
idade = ano_atual - ano_nascimento

if dia_aniversario > dia_atual and mes_aniversario > mes_atual:
    print(f'sua idade é {idade - 1}')
else:
    print(idade)