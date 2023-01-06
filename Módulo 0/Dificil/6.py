"""Jogo de dados: Crie um programa onde jogadores joguem um dado e tenham resultados aleatórios.
O programa tem que:
Perguntar quantas rodadas você quer fazer;
Perguntar quantos jogadores vão jogar;
Criar um objeto pra cada jogador com nome e número tirado;
Guarda todos os objetos em uma lista;
Ordenar esses objetos, sabendo que o vencedor tirou o maior número no dado.
Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão."""

import random

dic = {"Jogadores":[],
       "Placar":[]        
}

rodadas = int(input("Quantas rodadas irão ser jogadas? \n"))
numJ = int(input("Quantos jogadores irão jogar? \n"))

for n in range(0,numJ): # Preenche os vetores de jogador e placar, funciona como um setup.
  dic["Jogadores"].append(input(f"Nome do jogador na posição {n+1}: ").strip().capitalize())
  dic["Placar"].append(0)

for i in range (0,rodadas): # Cria, preenche e resolve as rodadas.
  dic[f"Rodada {i+1}"] = []
  for n in range (0,numJ): # Preenche os valores sorteados nos vetores da respectiva rodada.
    dic[f"Rodada {i+1}"].append(random.randint(1,6))

  print(f"\n{dic[f'Rodada {i+1}']}") # Mostra os valores sorteados de cada jogador para o usuario.
  
  if dic[f"Rodada {i+1}"].count(max(dic[f"Rodada {i+1}"])) > 1: # Confere quantas correspondencias há do valor máximo dentro do vetor, sendo maior que 1 há um empate.
    print(f"Rodada {i+1} desconsiderada devido ao empate!")
  else:                                                         # Caso não tenha empate, adiciona 1 ao placar do jogador vencedor.
    print(f"Rodada {i+1} é valida!")
    dic["Placar"][dic[f"Rodada {i+1}"].index(max(dic[f"Rodada {i+1}"]))] += 1



print(f"\n\nO placar final é: {dic['Placar']}") # Exibe o placar final do jogo.

if dic["Placar"].count(max(dic["Placar"])) > 1: # Verifica quantas correspondeicar há do valor maximo dentro do vetor, maior que 1 o resultado final foi um empate.

  print("Empate!")

  vencedores = []
  for x in range(len(dic["Placar"])): # No caso de empate, busca o indice dos jogadores empatados na primeira posição para exibir seus nomes.
    if dic["Placar"][x] == max(dic["Placar"]):
      vencedores.append(x)
      print(f"Parabéns {dic['Jogadores'][x]}")

else:
  print(f"Parabéns {dic['Jogadores'][dic['Placar'].index(max(dic['Placar']))]}, você venceu!") # Caso não tenha empate, exibe o nome do jogador que possui mais pontos. 
