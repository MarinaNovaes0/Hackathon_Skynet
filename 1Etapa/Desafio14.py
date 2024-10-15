# Biblioteca
import os

# Valores da base e da altura
base = float(input('Insira o valor da base do retângulo: '))
altura = float(input('Insira o valor da altura do retângulo: '))
os.system("cls")

# Cálculo área
area = base * altura

# Cálculo perímeto
perimetro = 2 * (base + altura)

# Cálculo diagonal
diagonal = (base ** 2 + altura ** 2) ** 0.5

# Imprimindo resultados
print(50*"*")
print()
print(f'A área do retângulo é de: {area:.2f}')
print(f'O perimetro do retângulo é de: {perimetro:.2f}')
print(f'A diagonal do retângulo vale: {diagonal:.2f}')
print()
print(50*"*")
print("Fim!")