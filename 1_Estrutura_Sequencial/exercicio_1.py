#Escreva um programa que mostra ao usuário seu novo salário, dado que este sofreu um aumento de 32%.
salario = float (input("Digite seu salario: "))
aumento = (salario * 32) / 100
print(aumento)
salario = salario + aumento
print("Com o aumento, seu novo salario é: R$%.2f" % (salario))