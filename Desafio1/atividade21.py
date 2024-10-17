# Bibliotecas
import os

# Input do usuário
num1 = int(input("Digite o numerador: "))
num2 = int(input("Digite o denominador: "))
os.system("cls")

# Verificando o resto da divisão
y = num1%num2

# Exibe se o resto da divisão não for 0  
if y != 0:
    print(40*"*")
    print()
    print(f"{num1} não pode ser divisível por {num2}")
    print()
    print(40*"*")
    print("Fim!")
    
# Exibe se o resto for 0  
else:
    print(40*"*")
    print()
    print(f"{num1} pode ser divisível por {num2}")
    print()
    print(40*"*")
    print("Fim!")