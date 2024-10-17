# Biblioteca
import os

# Variaveis de horas trabalhadas e o salário mínimo
hr_trbds = float(input('Digite o número de horas trabalhadas: '))
slr_min = float(input('Digite o salário mínimo: '))
os.system("cls")

# Variável valor da hora trabalhada
vl_hr_trbd = 0.5 * slr_min

# Salário bruto
slr_brt = vl_hr_trbd * hr_trbds

# Imposto
imposto = 0.03 * slr_brt

# Salário líquido
slr_rcb = slr_brt - imposto

# Imprimindo resultado
print(40*"*")
print()
print(f'Salário Líquido: R${slr_rcb:.2f}')
print()
print(40*"*")
print("Fim!")