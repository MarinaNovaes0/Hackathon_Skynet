# Bibliotecas
import os

# Variáveis para os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
os.system("cls")

# Variável da soma
soma = num1 + num2 + num3 + num4

# Imprimindo resultado
print(50*'*')
print()
print(f"O número digitados foram: {num1}, {num2}, {num3}, {num4}")
print(f"A soma destes números é igual a: {soma}")
print()
print(50*'*')
print("Fim!")