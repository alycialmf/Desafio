import os
os.system('cls')

with open('Parte1/numeros.csv', 'r') as arquivo:
    numeros = arquivo.read().split(',')

numeros = [int(num) for num in numeros]

soma_impares = sum(num for num in numeros if num % 2)

print(f"Os números presentes no arquivo são: {numeros}")
print(f"A soma dos números ímpares é: {soma_impares}")

arquivo.close()