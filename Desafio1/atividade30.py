import time
import os

#A lista de nomes
lista = ["Bundão", "Philipi", "Kleber", "João", "JJ", "Spider Man", "Mary Jane", "Exclói da Silva", "Teobaldo", "Bizerra"]

#Mostrando a sequência e ordem pedida dos nomes

print(30*"*")
print()
print("O primeiro elemento da lista:")
print(lista[0])
print()
print(30*"*")
time.sleep(3)
os.system('cls')

print(30*"*")
print()
print("Apenas o 5° elemento da lista:")
print(lista[4])
print()
print(30*"*")
print()
print()
time.sleep(3)
os.system('cls')

print(40*"*")
print()
print("Somente o 2° e 3° elemento da lista:")
print(lista[1:3])
print()
print(40*"*")
print()
print()
time.sleep(3)
os.system('cls')

print(60*"*")
print()
print("Os 6 primeiros elementos da lista:")
print(lista[:6])
print()
print(60*"*")
print()
print()
time.sleep(3)
os.system('cls')

print(50*"*")
print()
print("Os 3 últimos elementos da lista:")
print(lista[-3:])
print()
print(50*"*")
print("Fim!")
time.sleep(3)
os.system('cls')