#Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece
# a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre
# a mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida
# para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.
peso_saco_de_racao = float (input("Qual o peso do saco de ração em kgs: "))
quantidade_individual = float (input("Quantidade de raçao para cada gato em gramas: "))

quantidade_kg = quantidade_individual / 1000
quantidade_kg = (quantidade_kg * 2 ) * 5
peso_saco_de_racao = peso_saco_de_racao - quantidade_kg  

if peso_saco_de_racao < quantidade_kg:
    print("Não sobrou ração")
else:
    print("Após cinco dias, sobrará ", peso_saco_de_racao, " KGs no saco de ração.")
