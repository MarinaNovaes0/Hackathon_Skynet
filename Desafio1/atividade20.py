# Biblioteca
import os

# Variável do número
n = int(input('Insira um número: '))
os.system('cls')

# Exibe se o número for múltiplo de 3
if n % 3 == 0:
    print(20*"*")
    print()
    print('É múltiplo de 3')
    print()
    print(20*"*")
    print("Fim!")

# Exibe se o número não for múltiplo de 3   
else:
    print(20*"*")
    print()
    print('Não é múltiplo de 3')
    print()
    print(20*"*")
    print("Fim!")