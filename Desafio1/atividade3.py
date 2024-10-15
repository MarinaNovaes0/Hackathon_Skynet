# Bibliotecas
import os

# Variáveis para os números
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
os.system("cls")

# Cálculo média
media=(num1 + num2 + num3) / 3

# Imprimindo resultados
print(30*'*')
print()
print(f"A média é igual a: {media}")
print()
print(30*'*')
print("Fim!")