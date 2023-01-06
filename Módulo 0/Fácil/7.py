"""
Você está na flor da idade?
Defina uma variável para o valor do ano do nascimento;
Defina uma variável para o valor do ano atual;
Defina uma variável que calcula o valor final da idade da pessoa;
Exiba uma mensagem final dizendo a idade da pessoa e a mensagem "Você está na flor da idade".
"""

anoNasc = int(input("Em qual ano você nasceu??\n"))
anoAtual = 2022

while anoAtual < anoNasc:
  print("Você ainda nem nasceu??? Insira um ano de nascimento válido")
  anoNasc = int(input())

idade = anoAtual-anoNasc
print(f"Você deve ter/fazer {idade} anos e está na flor da idade!")
