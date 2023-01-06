#Faça um programa que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

ano = int(input("Qual seu ano de nascimento?\n"))
if 2022 - ano < 16:
  print("Voto negado!")
elif 2022 - ano < 18 or 2022 - ano >= 70:
  print("Voto opcional!")
else:
  print ("Voto obrigatório")
