# Bibliotecas
import os

# Declarando variáveis
num = input("Digite um número: ")
num = int(num)
os.system("cls")

# Cálculo sucessor
suc = num+1
# Cálculo antecessor
ant = num-1

# Exibindo resultado
print(30*'*')
print()
print(f"O sucessor do número é: {suc}")
print(f"O antecessor do número é: {ant}")
print()
print(30*'*')
print("Fim!")