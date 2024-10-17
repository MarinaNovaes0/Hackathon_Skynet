# Bibliotecas
import os

# Variável letra
letra = input('Digite uma letra: ').upper()
os.system("cls")

# Exibe se a letra for uma vogal
if letra in ['A','E','I','O','U']:
    print(20*"*")
    print()
    print(f'{letra} é uma vogal')
    print()
    print(20*"*")
    print("Fim!")

# Exibe se a letra não for uma vogal   
else:
    print(20*"*")
    print()
    print(f'{letra} é uma consoante')
    print()
    print(20*"*")
    print("Fim!")
