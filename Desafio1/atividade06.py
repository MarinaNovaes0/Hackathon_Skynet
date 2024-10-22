# Bibliotecas
import os

# Variável salário bruto
salario_inicial = float(input("Digite o seu salário base: "))
os.system("cls")

# Calculando o imposto (10% do salário)
imposto = salario_inicial * 0.1

# Cálculo salário líquido
salario_final = (salario_inicial-imposto) + 50

# Imprimindo resultados
print(40*'*')
print()
print(f"O seu salário líquido será: R${salario_final:.2f}")
print()
print(40*'*')
print("Fim!")