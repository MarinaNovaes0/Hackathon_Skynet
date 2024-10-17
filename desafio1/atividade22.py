# Biblioteca
import os

# Criando um dicionário
dias_da_semana = {
    1 : 'Domingo',
    2 : 'Segunda',
    3 : 'Terça',
    4 : 'Quarta',
    5 : 'Quinta',
    6 : 'Sexta',
    7 : 'Sábado'
}

# Número do dia
n = int(input('Digite um número entre 1 e 7: '))
os.system("cls")

# Exibe se o número digitado não estiver entre 1 e 7
if n < 1 or n > 7:
    print(45*"*")
    print()
    print('Não existe dia da semana com esse número')
    print()
    print(45*"*")
    print("Fim!")

# Exibe o nome do dia conforme o número   
else:
    dia_da_semana = dias_da_semana[n]
    print(45*"*")
    print()
    print(f'O dia da semana que você escolheu é: {dia_da_semana}')
    print()
    print(45*"*")
    print("Fim!")
