# Biblioteca
import os

# Prestação em atraso
v_i = float(input('Insira o valor da prestação em atraso: '))

# Taxa de juros
taxa = float(input('Insira a taxa de juros a ser cobrado por dia, em porcentagem: '))

# Tempo
tempo = int(input('Insira o número de dias em que a prestação está atrasada: '))
os.system("cls")

# Cálculo prestação
prest = v_i + v_i*(taxa/100)*tempo

# Imprimindo resultado
print(40*"*")
print()
print(f'A prestação a ser paga é de: R${prest:.2f}')
print()
print(40*"*")
print("Fim!")