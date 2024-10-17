# Biblioteca
import os

# Variável do peso
peso = float(input('Digite o seu peso: '))
os.system("cls")

# Variável após engordar
peso_gordo = peso * 1.15

# Variável após emagrecer
peso_magro = peso * 0.8

# Imprimindo resultado
print(60*"*")
print()
print(f'O seu novo peso, caso engorde 15% do seu peso é: {peso_gordo:.2f} kg')
print(f'O seu novo peso, caso emagreça 20% do seu peso é: {peso_magro:.2f} kg')
print()
print(60*"*")
print("Fim!")