# Biblioteca
import os 

# Criando uma lista vazia
lista_numeros = []

# Adicionando 3 números
for _ in range(3):
    n = int(input('Insira um número: '))
    lista_numeros.append(n)
os.system('cls')

# Descobrindo o maior e o menor número
maior = max(lista_numeros)
menor = min(lista_numeros)

# Imprimindo resultado
print(55*"*")
print()
print(f'O maior número entre os três digitados é: {maior}')
print(f'O menor número entre os três digitados é: {menor}')
print()
print(55*"*")
print("Fim!")