"""
Crie um programa em Python que peça a nota do aluno, que deve ser um real entre 0.00 e 10.0
Se a nota for menor que 6.0, deve exibir a nota F.
Se a nota for de 6.0 até 7.0, deve exibir a nota D.
Se a nota for entre 7.0 e 8.0, deve exibir a nota C.
Se a nota for entre 8.0 e 9.0, deve exibir a nota B.
Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A.
"""

nota = float(input("Insira a nota do aluno:\n"))

while nota < 0 or nota > 10:
  print(f"{nota} não está em um intervalo válido, insira uma nota no intervalo de 0 a 10:") 
  nota = float(input())

if nota < 6:
  print("Nota F")
elif nota < 7:
  print("Nota D")
elif nota < 8:
  print("Nota C")
elif nota < 9:
  print("Nota B")
else:
  print("Nota A")
