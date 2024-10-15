# Biblioteca
import os

# Variável número
n = int(input('Insira um número inteiro: '))
os.system("cls")

# Exibe se for par
if n % 2 == 0:
    print(20*"*")
    print()
    print(f'{n} é um número par')
    print()
    print(20*"*")
    print("Fim!")

# Exibe se for ímpar
else:
    print(20*"*")
    print()
    print(f'{n} é um número ímpar')
    print()
    print(20*"*")
    print("Fim!")
