#Escreva um programa que obtém o ano de nascimento de uma pessoa e mostra
# Sua idade (aproximada) atual
# Quantos dias (aproximadamente) essa pessoa viveu
# Quantos anos ela terá no ano de 2052
# Quantos anos ela terá em um ano arbitrário que informar
nascimento = int (input("Digite o seu ano de nascimento:"))

idade_atual = 2022 - nascimento
print("A idade atual é ", idade_atual, " anos")

dias_vividos = idade_atual * 365
print("Você viveu ", dias_vividos, " dias.")

anos_2052 = 2052 - nascimento
print("Em 2052, você terá ", anos_2052, " anos.")

ano_arbitrario = int(input("Informe um ano aleatório: "))

if ano_arbitrario <= nascimento:
    print("O ano informado é anterior ao seu nascimento.")
else:
    idade_eventual = ano_arbitrario - nascimento
    print("Em ", ano_arbitrario, ", sua idade será ", idade_eventual, " anos.")