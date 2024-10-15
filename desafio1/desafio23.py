#Bibliotecas
import os

# Input de altura e peso do usuário
altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))
os.system("cls")

# Cálculo do IMC
imc = peso/(altura**2)

# Resultado do IMC

if imc <= 18.5:
    print(10*"*")
    print()
    print("Magreza")
    print()
    print(10*"*")
    print("Fim!")
    
elif 18.5 < imc <= 24.9:
    print(10*"*")
    print()
    print("Saudável")
    print()
    print(10*"*")
    print("Fim!")
    
elif 25 < imc <= 29.9:
    print(10*"*")
    print()
    print("Sobrepeso")
    print()
    print(10*"*")
    print("Fim!")
    
elif 30 < imc <= 34.9:
    print(20*"*")
    print()
    print("Obesidade grau 1")
    print()
    print(20*"*")
    print("Fim!")
      
elif 35 < imc <= 39.9:
    print(20*"*")
    print()
    print("Obesidade grau 2")
    print()
    print(20*"*")
    print("Fim!")
       
elif imc >= 40:
    print(20*"*")
    print()
    print("Obesidade grau 3")
    print()
    print(20*"*")
    print("Fim!")