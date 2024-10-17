# Biblioteca
import os

# Input dos 2 nomes e sobrenomes dos 2 usuários 
nome1 = input("Escreva um nome: ")
sobrenome1 = input("Escreva um sobrenome: ")
nome2 = input("Escreva outro nome: ")
sobrenome2 = input("Escreva outro sobrenome: ")
os.system('cls')

# Mostrando a mistura entre o sobrenome do segundo com o nome do primeiro, 
# e o nome 2 do segundo com o sobrenome do primeiro
print(45*"*")
print()
print(f"Primeiro nome: {nome1} {sobrenome2}")
print(f"Segundo nome: {nome2} {sobrenome1}")
print()
print(45*"*")
print("Fim!")