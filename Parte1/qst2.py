import os
os.system('cls')

palavra = input("Digite a palavra: ")

palavra_inversa = palavra.strip()[::-1]

if(palavra == palavra_inversa):
    print(f'Sim, a palavra "{palavra}" é palíndroma')
else:
    print(f'Não, a palavra "{palavra}" não é palíndroma')


