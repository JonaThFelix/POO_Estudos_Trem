#Estudos sobre dinâmica de POO
#Obs.: Algoritmo criado para andar de 10 em 10, use o bom senso.

x = 0

class Trem:
  def __init__(self,nome,destino):
    self.__nome = nome
    self.__destino = destino
    self.__velocidade = 0

  #Apresentação do Trem até o destino
  def apresentar(self):
    print(f'O trem {self.__nome} está se deslocando até a estação {self.__destino}.')

  #Deslocamento até as estações
  def estacoes(self,x):
    self.__velocidade += x #somador

    if self.__velocidade == 0:
      print('O Maquinista está esperando você sair com o trem\nInsira um valor inicial de 10')
    if self.__velocidade == 10:
      print(f'O trem {self.__nome} andou {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Recife')
    if self.__velocidade == 20:
      print(f'O trem {self.__nome} andou mais {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Joana Bezerra')
    if self.__velocidade == 30:
      print(f'O trem {self.__nome} andou {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Afogados')
    if self.__velocidade == 40:
      print(f'O trem {self.__nome} andou mais {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Ipiranga')
    if self.__velocidade == 50:
      print(f'O trem {self.__nome} andou {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Mangueira')
    if self.__velocidade == 60:
      print(f'O trem {self.__nome} andou mais {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Santa Luzia')
    if self.__velocidade == 70:
      print(f'O trem {self.__nome} andou {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Werneck')
    if self.__velocidade == 80:
      print(f'O trem {self.__nome} andou mais {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Barro')
    if self.__velocidade == 90:
      print(f'O trem {self.__nome} andou {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Tejipió')
    if self.__velocidade == 100:
      print(f'O trem {self.__nome} andou mais {x} Km/h, totalizando {self.__velocidade} Km/h e chegou na estação: Coqueiral')
    elif self.__velocidade >=100:
      print(f'AVISO: O trem {self.__nome} não pode se deslocar ao seus destino, pois ultrapassou todas às estações')
    
    
