"""
E os 10% do garçom?
Defina uma variável para o valor de uma refeição que custou R$ 42,54;
Defina uma variável para o valor da taxa de serviço que é de 10%;
Defina uma variável que calcula o valor total da conta e exiba-o no console com essa formatação: R$ 9999.99.
"""

preco = float(input("Qual o preço da refeição?\n"))
desc = float(input("Quanto de desconto? (em %)\n"))

ValorRefeicao = preco + (preco*desc/100)
print(f"\nO total será R$ {ValorRefeicao:.2f} ")
