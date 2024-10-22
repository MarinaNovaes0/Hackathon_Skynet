# Bibliotecas
import os

# Variável para o salário sem aumento
salario_inicial = float(input("Digite o seu salário antes do aumento: "))

# Variável da porcentagem de aumento
porcentagem = float(input("Digite a porcentagem de aumento: "))
os.system("cls")

# Transformando em decimal
decimal = porcentagem / 100

# Aplicando no salário
aumento = salario_inicial * decimal

# Imprimindo resultados
print(55*'*')
print()
print(f"Você irá ganhar R${aumento:.2f} a mais!")
print(f"Seu salário depois do aumento será: R${salario_inicial + aumento:.2f}")
print()
print(55*'*')
print("Fim!")