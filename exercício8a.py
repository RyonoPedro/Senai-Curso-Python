# Usando listas crie um programa que recebe as quatro notas de um aluno
# Adicione essas notas em uma lista e calcule a media desse aluno
# imprima a lista gerada e a média do aluno

nome_alunos = []
media_alunos = []
nome = input('Qual o nome do aluno: ')
nome_alunos.append(nome)

while True:
    nota = int(input('Digite a nota: '))
    media_alunos.append(nota)
    contar = len(media_alunos)
    
    if contar >= 4:
        média = sum(media_alunos)/4
        print(f'{nome_alunos} - {média}')
        break
    

        
    
    