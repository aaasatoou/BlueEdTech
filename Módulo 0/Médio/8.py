# Agora, imprima todas as tabuadas do número 1 ao 10.

for n in range(1,11):
  for x in range(11):
    print(f"{n} * {x} = {n*x}")
  print("")
