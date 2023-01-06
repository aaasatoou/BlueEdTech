"""
Qual o valor do troco?
Defina uma variável para o valor de uma compra que custou R$100,98;
Defina uma variável para o valor que o cliente pagou R$150,00;
Defina uma variável que calcula o valor do troco e exiba-o no console com o valor final arredondado.
"""

preco = float(input("Qual o preço da compra?\n"))
pago = float(input("Qual o valor recebido\n"))

while pago < preco:
  print("Caloteiro...")
  pago = float(input("Pague o valor correto\n"))

troco = pago - preco
print(f"\nO troco será R$ {troco:.2f} ")
