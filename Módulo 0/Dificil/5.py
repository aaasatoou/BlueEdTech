"""
Jogo Jokenpô: Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você.
Permitir que eu decida quantas rodadas iremos fazer;
Ler a minha escolha (Pedra, papel ou tesoura);
Decidir de forma aleatória a decisão do computador;
Mostrar quantas rodadas cada jogador ganhou;
Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.
"""

import random

def jogo():

  rodadas = int(input("Quantas rodadas quer fazer?\n"))
  vitoriaJ = 0
  vitoriaM = 0

  for n in range(rodadas):
    escolhaJogador = input("Sua escolha (pedra, papel ou tesoura):\n").strip().lower()

    while escolhaJogador != "pedra" and escolhaJogador != "papel" and escolhaJogador != "tesoura":
      escolhaJogador = input("Entrada inválida, insira uma nova escolha:\n").strip().lower()
    
    escolhaMaquina = random.choice(["pedra", "papel", "tesoura"])
    print(f"A maquina escolheu {escolhaMaquina}")

    if escolhaMaquina == escolhaJogador:
      print("EMPATE, ninguem pontua\n")
    elif escolhaMaquina == "pedra" and escolhaJogador == "papel":
      print("PONTO PARA O JOGADOR\n")
      vitoriaJ += 1
    elif escolhaMaquina == "pedra" and escolhaJogador == "tesoura":
      print("PONTO PARA A MAQUINA\n")
      vitoriaM += 1
    elif escolhaMaquina == "tesoura" and escolhaJogador == "pedra":
      print("PONTO PARA O JOGADOR\n")
      vitoriaJ += 1
    elif escolhaMaquina == "tesoura" and escolhaJogador == "papel":
      print("PONTO PARA A MAQUINA\n")
      vitoriaM += 1
    elif escolhaMaquina == "papel" and escolhaJogador == "pedra":
      print("PONTO PARA A MAQUINA\n")
      vitoriaM += 1
    elif escolhaMaquina == "papel" and escolhaJogador == "tesoura":
      print("PONTO PARA O JOGADOR\n")
      vitoriaJ += 1

  if vitoriaJ > vitoriaM:
    print("O JOGADOR VENCEU")
  elif vitoriaM < vitoriaJ:
    print("A MAQUINA VENCEU")
  else:
    print("EMPATOU")

  replay = input("Quer jogar de novo? 'y' para sim e 'n' para não\n")

  while replay != "y" and replay != "n":
    replay = input("Entrada inválida. Quer jogar de novo? 'y' para sim e 'n' para não\n")
  
  if replay == 'y':
    jogo()    

jogo()
