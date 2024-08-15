#lista de tarefas 


tarefa = ''
contador = 1

while True:
    resposta = input('Digite uma tarefa para hoje: ')
    tarefa += str(contador) + ' - ' + resposta + '\n'
    contador += 1
    pergunta = input('Deseja lançar outra tarefa S/N: ')
    if pergunta.upper() == 'N':
        break

print('''    
      Lista de Tarefas para hoje

''')
print(tarefa)