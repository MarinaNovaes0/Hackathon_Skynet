# Biblioteca
import os

# Variável de distância e combustível
distancia_viagem = float(input('Insira a distância a ser percorrida nessa viagem em Km: '))
preço_combustivel = float(input('Insira o preço do combustivel em reais: '))
os.system("cls")

# quilometragem por litro de cada veículo
km_l_A = 16
km_l_B = 12
km_l_C = 8

# Cálculo veículo A
combustivel_A = distancia_viagem / km_l_A
preco_viagem_A = combustivel_A * preço_combustivel

# Cálculo veículo B
combustivel_B = distancia_viagem / km_l_B
preco_viagem_B = combustivel_B * preço_combustivel

# Cálculo veículo C
combustivel_C = distancia_viagem / km_l_C
preco_viagem_C = combustivel_C * preço_combustivel

# Imprimindo os resultados
print(55*"*")
print()
print(f'O preço estimado da viagem no veículo A é de R${preco_viagem_A:.2f}')
print(f'O preço estimado da viagem no veículo B é de R${preco_viagem_B:.2f}')
print(f'O preço estimado da viagem no veículo C é de R${preco_viagem_C:.2f}')
print()
print(55*"*")
print("Fim!")