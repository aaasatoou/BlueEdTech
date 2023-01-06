"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

numeros = []
print("Digite os numeros 1 por vez, digite 'c' para concluir a inserção de valores numéricos")

while True:
  n = input().strip().lower()
  if n == 'c':
    break

  elif n.isnumeric():
    n = int(n)

    if numeros.count(n)>0:
      continue
    else:
      numeros.append(n)

  else:
    print("Entrada inválida!!!!")

numeros.sort()
print(f"Os numeros digitados foram: {numeros}")
