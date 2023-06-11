from random import randint
import os
os.system('cls')

lista = []

for i in range(20):
    lista.append(randint(1, 100))

print(f"A lista com 20 números aleatórios é: {lista}")
print(f"O maior elemento da lista é: {max(lista)}")