"""
Faça um programa que pergunte ao usuário um número e valide se o numero é par ou impar:
Crie uma variável para receber o valor, com conversão para inteiro
Para um número ser par, a divisão dele por 2 tem que dar resto 0
"""

numero = int(input("Insira um numero para verificar se é par ou impar (apenas inteiros):\n"))
if numero%2 == 0:
  print(f"O numero {numero} é par")
else:
  print(f"O numero {numero} é impar")
