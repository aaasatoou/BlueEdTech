"""
Caixa eletrônico: Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
import math

saque = int(input("Quanto deseja sacar? (minimo R$ 10 e maximo R$ 600 )\n"))

while saque < 10 or saque > 600:
  print("Valor fora do intervalo permitido, insira um novo valor:")
  saque = int(input())

print(f"{math.floor(saque/100)} notas de 100 fornecida")
saque = saque%100
print(f"{math.floor(saque/50)} notas de 50 fornecida")
saque = saque%50
print(f"{math.floor(saque/10)} notas de 10 fornecida")
saque = saque%10
print(f"{math.floor(saque/5)} notas de 5 fornecida")
saque = saque%5
print(f"{math.floor(saque/1)} notas de 1 fornecida")
