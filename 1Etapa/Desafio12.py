# Biblioteca
import os

# Variável do valor em pés
pes = float(input('Digite um valor em pés: '))
os.system("cls")

# Cálculo para polegada, jardas e milhas
pol = pes / 12
jar = 3 * pes
mil = 5.28 * pes

# Imprimindo resultado
print(50*"*")
print()
print(f'{pes} pés é igual a {pol:.2f} polegadas.')
print(f'{pes} pés é igual a {jar:.2f} jardas.')
print(f'{pes} pés é igual a {mil:.2f} milhas.')
print()
print(50*"*")
print("Fim!")