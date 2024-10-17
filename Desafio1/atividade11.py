# Biblioteca
import os

# Variáveis para os números
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
os.system("cls")

# Cálculo potenciação
resultado = n1**n2

# Imprimindo resultado
print(50*"*")
print()
print(f'{n1:.0f} elevado a {n2:.0f} é igual a {resultado:.0f}')
print()
print(50*"*")
print("Fim!")