from collections import Counter
from calculate import Calculate



class StatisticCalculate:


  def media(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    return float(sum(numeros) / len(numeros))


  def mediana(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    numeros.sort()
    if len(numeros) % 2 == 0:
      return (numeros[int(len(numeros) / 2)] + numeros[int(len(numeros) / 2) - 1]) / 2
    return numeros[int(len(numeros) / 2)]


  def moda(self, numeros: list) -> list:
    lista = []
    numeros = Calculate.get_numeros(numeros)
    counter = Counter(numeros).most_common()
    for numero in counter:
      if numero[1] == counter[0][1]:
        lista.append(numero[0])
      else:
        break

    if counter[0][1] == counter[-1][1]:
      return []
    return lista


  def variancia(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    media = self.media(numeros)
    for index in range(len(numeros)):
      numeros[index] -= media
      numeros[index] *= numeros[index]
    soma = sum(numeros)
    return soma / (len(numeros) - 1)


  def desvio_padrao(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    return self.variancia(numeros) ** 0.5

  
  def amplitude(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    return max(numeros) - min(numeros)

  
  def desvio_medio(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    media = self.media(numeros)
    for index in range(len(numeros)):
      numeros[index] = abs(numeros[index] - media)
    return sum(numeros) / len(numeros)


  def erro_padrao(self, numeros: list) -> float:
    numeros = Calculate.get_numeros(numeros)
    desvio = self.desvio_padrao(numeros)
    return desvio / (len(numeros) ** 0.5)


  def coeficiente_variacao(self, numeros: list) -> float:
    desvio = self.desvio_padrao(numeros)
    media = self.media(numeros)
    variacao = (desvio / media) * 100
    return variacao