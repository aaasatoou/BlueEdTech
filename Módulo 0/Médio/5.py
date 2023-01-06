"""Reajuste salarial: As empresas @.com resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

aumento = 0
salario = float(input("Qual o salário do colaborador (R$)?\n"))

while salario <= 0:
  print("Salario inválido! Insira um novo salário")
  salario = float(input())

if salario <= 280:
  aumento = 20
elif salario <=700:
  aumento = 15
elif salario <=1500:
  aumento = 10
else:
  aumento = 5

print(f"O salário era de R$ {salario:.2f}")
print(f"Será aplicado um aumento de {aumento}%")
print(f"Este salário será aumentado em R$ {(salario*aumento/100):.2f}")
print(f"O novo salário será de R$ {(salario*aumento/100 + salario):.2f}")
