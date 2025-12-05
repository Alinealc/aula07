livros ={} #dicionario
lista_cadastro = [] #lista

#Cadastro em dicionários
for i in range(3):
   print(30*"**")
    titulo = input('Informe o título: ')
    autor = input('Informe o Autor: ')
    ano = int(input('Informe o Ano: '))
    genero=int(input('Informe o Ano:'))

    livros = {
        'Título': titulo,
        'Autor': autor,
        'Gênero': genero
    }

    lista_cadastro.append(livros)
    print(f'Livro{i+1} Cadastrado')