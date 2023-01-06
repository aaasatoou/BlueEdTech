"""
Conversor de moedas: Crie um programa que solicite um um valor em real ao usuário e converta esse valor, para:
DOLAR
EURO
LIBRA ESTERLINA
DÓLAR CANADENSE
PESO ARGENTINO
PESO CHILENO
Para esse exercício você precisará realizar uma pesquisa para saber a cotação de cada moeda em real. Mostrar o resultado no formato U$9999.99
"""

valorReal = float(input("Insira o valor que deve ser convertido (em R$)\n"))
print(f"O  valor convertido para dolar é $ {(valorReal/5.06):.2f}")
print(f"O  valor convertido para euro é $ {(valorReal/5.73):.2f}")
print(f"O  valor convertido para libra esterlina é $ {(valorReal/6.87):.2f}")
print(f"O  valor convertido para dolar canadense é $ {(valorReal/3.96):.2f}")
print(f"O  valor convertido para peso argentino é $ {(valorReal/0.047):.2f}")
print(f"O  valor convertido para peso chileno é $ {(valorReal/0.0064):.2f}")
