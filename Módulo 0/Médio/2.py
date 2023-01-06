# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo e implemente a funcionalidade de não aceitar o número 0.

numero = float(input("Insira um nº qualquer (exceto 0)\n"))

while numero == 0:
  print("0 não vale! Insira um novo nº")
  numero = float(input())

if numero > 0:
  print(f"O numero {numero} é positivo.")
elif numero < 0:
  print(f"o numero {numero} é negativo.")
