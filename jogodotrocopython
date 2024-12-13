'''
* Autor: Rafaela Cardoso
* Linguagem: Python
* Data: 10/12/2024
* Descrição: JOGO - TROCO. O Jogo Troco tem como objetivo do computador(personagem) escolher os itens que o mesmo deseja comprar e o quanto de dinheiro que o mesmo irá dar para realizar a compra. O jogador tem como objetivo verificar o valor e aplicar o troco. 
* Funcionalidades: No console será mostrado o nome do personagem, o que ele comprou e o quanto de dinheiro o mesmo deu para efetuar o pagamento. Cabe ao usuário verificar o troco que o computador deve receber digitando - o no console. Se o troco estiver correto, a mensagem "TROCO CORRETO!" irá aparecer, se não "TROCO ERRADO!" e o jogador deverá digitar o valor até o recebimento estar correto. 
* Versão: [1.0]
'''
import random #importei a biblioteca random para utilizar choice e randint
#criei uma lista para facilitar o código colocando o valor das váriaveis 
itens = {
    'Batata': 4,
    'Arroz': 3,
    'Feijão': 5
}
#função do jogo do troco, é nela que está a estrutura do jogo
def JogoTroco():
  #fiz uma lista "personagens" e utilizei random.choice para que o computador escolhesse um nome entre "Joao, Maria e Jose"
  personagens=random.choice(['Joao', 'Maria', 'Jose'])
  #Comando que faz aparecer o nome do personagem escolhido no console. 
  print(personagens)
  #Fiz uma lista chamada "compras"
  compras=[]
  #o comando "append" faz com que  vá para o ultimo elemento do lista. Dentro de append entre parentese está o random.choice, que é utilizado para que o computador consiga escolher os itens aleatoriamente. Entre parenteses usei o comando "itens(a lista que eu criei os variaveis batata, arroz e feijao).items(da biblioteca random), ou seja, ela puxa essa lista para dentro do código.
  compras.append(random.choice(list(itens.items())))
  #Copiei o comando para que dois itens fossem escolhidos. O comando "append" faz com que  vá para o ultimo elemento do lista. Dentro de append entre parentese está o random.choice, que é utilizado para que o computador consiga escolher os itens aleatoriamente. Entre parenteses usei o comando "itens(a lista que eu criei os variaveis batata, arroz e feijao).items(da biblioteca random), ou seja, ela puxa essa lista para dentro do código.
  compras.append(random.choice(list(itens.items())))
  # Para explicar essa parte, funciona da seguinte forma:
  # compras[0][0] - nome do primeiro item escolhido da lista. compras[0][1] - preço do primeiro item escolhido da lista. compras[1][0] - nome do segundo item escolhido da lista. compras[1[1] - preço do segundo item escolhido da lista
  # totalcompras é equivalente ao preço do primeiro item com o preço do segundo item
  totalcompras = compras[0][1] + compras[1][1]
  # Mostra no console os item comprados, o primeiro e o segundo item escolhido aleatoriamente a partir da lista com a mensagem "Itens comprados: nome do primeiro item e o seu preço e o nome do segundo item e o seu preço"
  print(f'Itens comprados: {compras[0][0]} = {compras[0][1]} e {compras[1][0]} = {compras[1][1]}')
  # A variavel dinheiro irá variar entre 9 e 20
  dinheiro=random.randint(9, 20)
  # Mostra no console o dinheiro que o cliente deu para pagar
  print(f'Dinheiro recebido: {dinheiro}')
  # Variavel trococerto é equivalente a variavel dinheiro menos o total de compras 
  trococerto = dinheiro - totalcompras
  # Comando de entrada que faz o usuario digitar o numero de troco
  troco=int(input('Troco: '))
  # Enquanto o troco for diferente de trococerto a mensagem "TROCO ERRADO! Tente novamente." irá aparecer no console
  while troco != trococerto:
    print("TROCO ERRADO! Tente novamente.")
    #Dentro do laço, da continuidade para que o usuario digite NOVAMENTE o troco até ele estar correto 
    troco = int(input('Qual o valor do troco? '))
  # Fora do laço, quando o troco for correto, no console aparecerá "TROCO CORRETO!"
  print("TROCO CORRETO!\n")
  ReninciaJogo()
  
  
# Função que faz a inicialização da entrada do jogo
def IniciaJogo():
  # Quando a função IniciaJogo for chamada, irá aparecer no console a mensagem abaixo
  print('Deseja iniciar o jogo?\n',
       'SIM [0]\n',
       'NAO [1]\n')
  # Comando de entrada para validar a opção do usuário
  UserOption = int(input())
  # Se a resposta do usuario for igual a 0, vai ser chamada a função "JogoTroco" e o jogo começa
  if UserOption == 0:
    JogoTroco()
    # Se a opção do usuário for igual a 1 a mensagem "Até a próxima..." aparecerá no console
  if UserOption == 1:
    print('Até a próxima...')
    
# Função que da a opção de continuar jogando
def ReninciaJogo():
  # Quando a função ReninciaJogo for chamada, irá aparecer no console a mensagem abaixo
  print('Deseja continuar o jogo?\n',
     'SIM [0]\n',
     'NAO [1]\n')
  # Comando de entrada para validar a opção do usuário
  UserOption = int(input())
  # Se a resposta do usuario for igual a 0, vai ser chamada a função "JogoTroco" e o jogo começa
  if UserOption == 0:
    JogoTroco()
    # Se a opção do usuário for igual a 1 a mensagem "Até a próxima..." aparecerá no console
  if UserOption == 1:
    print('Até a próxima...')


# Chamo a função IniciaJogo para que ela funcione dentro do código
IniciaJogo()
