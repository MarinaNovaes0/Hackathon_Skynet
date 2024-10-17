# Biblioteca
import os

# Input da palavra do usuário
pal = input("Escreva uma palavra: ")
os.system("cls")

# Exibe se a quantidade de letras for par
if len(pal)%2==0:
    print(45*"*")
    print()
    print('A quantidade de letras da palavra é par')
    print()
    print(45*"*")
    print("Fim!")
    
# Exibe se a quantidade de letras for impar    
else:
    print(45*"*")
    print()
    print("A quantidade de letras da palavra é impar")
    print()
    print(45*"*")
    print("Fim!")

