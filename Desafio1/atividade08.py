# Bibliotecas
import os

# Variável da base
base = float(input("Digite o valor da base do triângulo em centímetros: "))

# Variável da altura
altura = float(input("Digite o valor da altura do triângulo em centímetros: "))
os.system("cls")

# Cálculo da área
area = (base * altura) / 2

# Imprimindo resultado
print(40*'*')
print()
print(f"A área do triângulo é igual a {area:.2f}cm ")
print()
print(40*'*')
print("Fim!")