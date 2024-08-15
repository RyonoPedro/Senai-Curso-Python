# Função com argumento e sem retorno

def analisar_texto(texto):
    
    # Função para analisar um texto e contar letras maiúsculas, 
    # minúsculas, espaços e caracteres especiais.
    # Argumento:
    # texto: String contendo o texto a ser analisado

    maiuscula = 0
    minuscula = 0
    espacos = 0
    especiais = 0
    
    for caracter in texto:
        if caracter.isupper():
            maiuscula += 1
        elif caracter.islower():
            minuscula += 1
        elif caracter.isspace():
            espacos += 1
        else:
            especiais += 1
    
    print(f'''          Letras maiúsculas: {maiuscula}
          Letras minúsculas: {minuscula}
          Espaços: {espacos}
          Caracteres especiais: {especiais}''')
    
print('''     Analisador de frases    
      ''')
frase = input('''Digite a frase a ser analisada: ''')
print()
analisar_texto(frase)
print('''
     Fim do Analisador de Frases''')