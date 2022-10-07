# Crie um programa que recebe uma lista de números e
#- retorne o maior elemento
lista = [10, 54, 7, 2, -3, 0, 4, -12, 10 ]
print("O maior elemento da lista é ", max(lista))

#- retorne a soma dos elementos
soma = 0
for soma_num in lista:
    soma += soma_num
print("A soma dos elementos da lista é ",soma)

#- retorne o número de ocorrências do primeiro elemento da lista
contador = 0
for ocorrencia in lista:
    if ocorrencia == lista[0]:
        contador += 1
print("O primeiro elemento ocorre ", contador, " vezes.")

#- retorne a média dos elementos
media = sum(lista)/len(lista)
print("A média dos elementos é ", media)

#- retorne o valor mais próximo da média dos elementos

#- retorne a soma dos elementos com valor negativo
negativo = 0
for menor in lista:
    if menor < 0:
        negativo += menor
print("A soma dos elementos negativos é ", negativo)

#- retorne a quantidade de vizinhos iguais

