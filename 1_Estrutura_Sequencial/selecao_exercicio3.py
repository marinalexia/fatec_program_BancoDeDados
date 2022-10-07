# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um 
# colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#- salários até R$ 280,00 (incluindo) : aumento de 20%
#- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 
#informe na tela:
#- o salário antes do reajuste;
#- o percentual de aumento aplicado;
#- o valor do aumento;
#- o novo salário, após o aumento
salario = float(input("Digite o salário: "))
print("O salário antes do reajuste é R$%.2f" % (salario))

if salario > 1500:
    aumento = (salario * 5) / 100
    salario += aumento
    print("O percentual de aumento foi de %5.")
    print("Em reais, o aumento foi R$%.2f" % aumento)
    print("O novo salário é R$%.2f" % salario)
elif salario >= 700 and salario <= 1500:
    aumento = (salario * 10) / 100
    salario += aumento
    print("O aumento foi de %10.")
    print("Em reais, o aumento foi R$%.2f" % aumento)
    print("O novo salário é R$%.2f" % salario)
elif salario < 700 and salario > 280:
    aumento = (salario * 15) / 100
    salario += aumento
    print("O aumento foi de %15.")
    print("Em reais, o aumenfo foi R$%.2f" % aumento)
    print("O novo salário é R$%.2f " % salario)
else:
    aumento = (salario * 20) /100
    salario += aumento
    print("O aumento foi de %20.")
    print("Em reais, o aumento foi R$%.2f" % aumento)
    print("O novo salário é R$%.2f " % salario)

