# Bibliotecas
import os

# Variável do número 
n = int(input("Digite um número natural: "))
os.system("cls")

# Cálculos
print(45*'*')
print()
print(f"O número ao quadrado é igual a: {n ** 2}")
print(f"O número ao cubo é igual a: {n ** 3}")
print(f"A raiz quadrada do número é igual a: {n ** 0.5:.2f}")
print(f"A raiz cúbica do número é igual a: {n ** (1/3):.2f}")
print()
print(45*'*')
print("Fim!")