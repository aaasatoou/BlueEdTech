#Faça um programa que peça dois números, imprima o maior deles ou imprima "Números iguais" se os números forem iguais.

num1= float(input("Insira o primeiro numero:\n"))
num2= float(input("insira o segundo numero:\n"))

if num1 == num2:
  print("Numeros iguais")
elif num1 > num2:
  print(f"O primeiro numero ({num1}) é maior")
else:
  print(f"O segundo numero ({num2}) é maior")
