#Escreva um programa que conta a quantidade de vogais em uma string e armazena
#tal quantidade em um dicionário, onde a chave é a vogal considerada.

palavra = input("Digite uma palavra: ")
mapa_vogais = {}
for vogal in 'aeiou':
    mapa_vogais[vogal] = 0
    
for letra in palavra:
    if letra in 'aeiou':
        mapa_vogais[letra] += 1

print(mapa_vogais)