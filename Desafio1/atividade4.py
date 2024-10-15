# Bibliotecas
import os

# Variável para o salário sem aumento
salario_inicial = float(input("Digite o seu salário antes do aumento: "))
os.system("cls")

# Cálculo do aumento
aumento = salario_inicial * 0.25

# Acrescentando no salário
salario_final = salario_inicial + aumento

# Imprimindo resultado
print(53*'*')
print()
print(f"O seu salário depois do aumento irá ficar: R${salario_final:.2f}")
print()
print(53*'*')
print("Fim!")