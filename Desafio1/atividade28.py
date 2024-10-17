# Biblioteca
import os

# Variável para os 4 digitos da palaca
placa = input('Insira os quatro digitos numéricos da placa do seu carro: ')
os.system("cls")

# Transformando em uma lista
placa_lista = list(placa)

# Deixando apenas o último dígito
ultimo_digito = placa_lista[-1]

# Exibe se o último número for 0 
if ultimo_digito == '0':
    print(40*"*")
    print()
    print('O mês de vencimento é Janeiro')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 1
elif ultimo_digito == '1':
    print(40*"*")
    print()
    print('O mês de vencimento é Fevereiro')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 2
elif ultimo_digito == '2':
    print(40*"*")
    print()
    print('O mês de vencimento é Março')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 3
elif ultimo_digito == '3':
    print(40*"*")
    print()
    print('O mês de vencimento é Abril')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 4
elif ultimo_digito == '4':
    print(40*"*")
    print()
    print('O mês de vencimento é Maio')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 5
elif ultimo_digito == '5':
    print(40*"*")
    print()
    print('O mês de vencimento é Junho')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 6   
elif ultimo_digito == '6':
    print(40*"*")
    print()
    print('O mês de vencimento é Julho')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 7   
elif ultimo_digito == '7':
    print(40*"*")
    print()
    print('O mês de vencimento é Agosto')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 8     
elif ultimo_digito == '8':
    print(40*"*")
    print()
    print('O mês de vencimento é Setembro')
    print()
    print(40*"*")
    print("Fim!")

# Exibe se o último número for 9    
else:
    print(40*"*")
    print()
    print('O mês de vencimento é Outubro')
    print()
    print(40*"*")
    print("Fim!")