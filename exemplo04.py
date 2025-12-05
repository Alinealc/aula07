#Dicionario - Estutura chave e valor 
#Símbolo {}
#notas={} #dicionário vazio 
#notas['Matemática'] = 8.5
#notas['Português'] = 7.0
#notas['História'] = 9.2


#notas['Matemárica'] = 8.0 #para alterar o valor é só repitir a chave com o novo valor
#notas['Geografia'] = 9.2  #para incluir e só digitar uma nova chave
#del notas['História'] #deleta a chave
#print(notas)

livros ={} #dicionario
lista_cadastro = [] #lista

#Cadastro em dicionários
for i in range(3):
    titulo = input('Informe o título: ')
    autor = input('Informe o Autor: ')
    ano = int(input('Informe o Ano: '))
    genero = stn(input('Informe o Gênero': ))

    livros = {
        'Título': titulo,
        'Autor': autor,
        'Gênero': genero
    }

    lista_cadastro.append(livros)
    print(f'Livro{i+1} Cadastrado')

