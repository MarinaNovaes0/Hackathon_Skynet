#Bibliotecas
import os
import time

#A calculadora
while True:
    #O menu dela
    os.system("cls")
    print()
    print(30*"*","CALCULADORA",30*"*")
    print("1. SOMA")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPLICAÇÃO")
    print("4. DIVISÃO")
    print("5. POTÊNCIA")
    print("6. SAIR")
    print(73*"*")
    print()
    
    #Escolha do usuário
    escolha = int(input("Escolha uma opção: "))
    os.system("cls")
    
    #Soma
    if escolha == 1:
        num1 = int(input("Escolha um número: "))
        num2 = int(input("Escolha um número: "))
        os.system("cls")
        soma = num1 + num2
        
        print(30*"*")
        print()
        print(f"A soma deu: {soma}")
        print()
        print(30*"*")
        print("Fim!")
        
        time.sleep(3)
        os.system('cls')
        
    #Subtração
    elif escolha == 2:
        os.system("cls")
        num3 = int(input("Escolha um número: "))
        num4 = int(input("Escolha um número: "))
        os.system("cls")
        subt = num3 - num4
        
        print(30*"*")
        print()
        print(f"A subtração deu: {subt}")
        print()
        print(30*"*")
        print("Fim!")
        
        time.sleep(3)
        os.system('cls')
        
    #Multiplicação
    elif escolha == 3:
        os.system("cls")
        num5 = int(input("Escolha um número: "))
        num6 = int(input("Escolha um número: "))
        os.system("cls")
        mult = num5 * num6
        
        print(30*"*")
        print()
        print(f"A multiplicação deu: {mult}")
        print()
        print(30*"*")
        print("Fim!")
        
        time.sleep(3)
        os.system('cls')
        
    #Divisão
    elif escolha == 4:
        os.system("cls")
        num7 = int(input("Escolha um número: "))
        num8 = int(input("Escolha um número: "))
        os.system("cls")
        div = num7 / num8
        
        print(30*"*")
        print()
        print(f"A divisão deu: {div}")
        print()
        print(30*"*")
        print("Fim!")
        
        time.sleep(3)
        os.system('cls')
        
    #Potência
    elif escolha == 5:
        os.system("cls")
        num9 = int(input("Escolha um número: "))
        num10 = int(input("Escolha um número: "))
        os.system("cls")
        pot = num9**num10
        
        print(30*"*")
        print()
        print(f"A potência deu: {pot}")
        print()
        print(30*"*")
        print("Fim!")
        
        time.sleep(3)
        os.system('cls')
        
    #Sair
    elif escolha == 6:
        os.system("cls")
        print(30*"*")
        print()
        print("Fim!")
        print()
        print(30*"*")  
        break
    #Para caso o usuário digite uma escolha inválida
    
    else:
        os.system("cls")
        print(30*"*")
        print()
        print("Escolha opção existente!")
        print()
        print(30*"*")  
        time.sleep(1)