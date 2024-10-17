# Variáveis
nome_livro = input('Insira o nome do livro: ')
data_emprestimo = int(input('Insira a dia do empréstimo: '))
tipo_usuario = input('Insira o tipo de usuário (professor ou aluno): ')

# Situação da devolução do livro se o tipo for aluno
if tipo_usuario == 'aluno':
    data_devolucao = data_emprestimo + 15
    if data_devolucao > 31:
        data_devolucao = data_devolucao - 31
        print(f'Nome do livro: {nome_livro}')
        print(f'Tipo do usuário: {tipo_usuario}')
        print(f'Data de empréstimo: {data_emprestimo}')
        print(f'Data de devolução: {data_devolucao} do mês que vem')
    else:
        print(f'Nome do livro: {nome_livro}')
        print(f'Tipo do usuário: {tipo_usuario}')
        print(f'Data de empréstimo: {data_emprestimo}')
        print(f'Data de devolução: {data_devolucao}')
# Situação da devolução do livro se o tipo for professor
elif tipo_usuario == 'professor':
    data_devolucao = data_emprestimo + 20
    if data_devolucao > 31:
        data_devolucao = data_devolucao - 31
        print(f'Nome do livro: {nome_livro}')
        print(f'Tipo do usuário: {tipo_usuario}')
        print(f'Data de empréstimo: {data_emprestimo}')
        print(f'Data de devolução: {data_devolucao} do mês que vem')
    else:
        print(f'Nome do livro: {nome_livro}')
        print(f'Tipo do usuário: {tipo_usuario}')
        print(f'Data de empréstimo: {data_emprestimo}')
        print(f'Data de devolução: {data_devolucao}')
# Situação se o tipo não existe
else: 
    print('Não existe este tipo de usuário.')
