# 1) Crie uma lista com 5 frutas. Adiciona 3 frutas
# no final da lista e remova a 1ª fruta da lista.
#imprima a lista no final.

def fruta():
    frutas = ['maça', 'banana', 'pessego', 'pera', 'melancia']
    print(frutas)
    a = 0
    while a <= 2:
        s = input('ponha mais uma fruta: ')
        frutas.append(s)
        a += 1
    
    print(frutas)
    frutas.remove('maça')
    print(frutas)
    
fruta()

# 2) Crie uma tupla com os dias da semana e imprima o terceiro item da tupla

def semana():
    semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta')
    print(f'{semana[2]}')

semana()

# 3) Crie um dicionário com 4 disciplinas e a nota de 
# cada disciplina de um aluno.
# imprima todas as disciplinas com as respectivas notas

def notas():
    notas = {'Matemática':'8', 'Portugues':'9', 'Geografia':'7', 'História':'10'}
    for x, y in notas.items():
        print(f''' Matéria de {x} : {y}''')

notas()
        