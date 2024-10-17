# Bibliotecas
import os

# Variável do primeiro cateto
b = float(input("Digite o valor do cateto b em centímetros: "))

# Variável do segundo cateto
c = float(input("Digite o valor do cateto c em centímetros: "))
os.system("cls")

# Cálculo da hipotenusa
a = (b ** 2 + c ** 2) ** 0.5

# Imprimindo resultado
print(40*'*')
print()
print(f"O valor da hipotenusa será: {a:.2f}cm")
print()
print(40*'*')
print("Fim!")