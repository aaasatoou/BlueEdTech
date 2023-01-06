#Faça um programa de cadastro de clientes que mostre um menu de opções e permita com que a pessoa escolha umas das opções, exibindo qual foi a opção escolhida.
clientes = []

while True:
  print("Escolha uma das opções abaixo:\n'c' para cadastro de clientes\n'r' para remocao de clientes\n'l' para listar todos os clientes\n")
  acao = input().lower()

  if acao == 'c':
    clientes.append(input("Digite o nome do cliente: ").strip().capitalize())
  elif acao == 'r':
    clientes.pop(clientes.index(input("Digite o nome a ser excluido: ").strip().capitalize()))
  elif acao == 'l':
    print(clientes)
  else:
    print("Opção não é válida.")
  print("\n")
