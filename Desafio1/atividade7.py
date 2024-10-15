# Bibliotecas
import os

# Variável da temperatura em Fahrenheit
f = float(input("Digite a temperatura em Fahrenheit: "))
os.system("cls")

# Cálculo para Celsius
c = 5 / 9 * (f - 32)

# Imprimindo resultados
print(40*'*')
print()
print(f"A temperatura em Celsius será: {c:.1f}°C")
print()
print(40*'*')
print("Fim!")