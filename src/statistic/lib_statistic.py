from calculo_statistic import StatisticCalculate



class Statistic:


  __statistic = StatisticCalculate()
  def media(self, numeros: list) -> float:
    """
    esta função recebe como parametro uma lista de numeros,
    ou matriz de numeros e retorna a media dos números da
    cadeia de números informada
    """
    return self.__statistic.media(numeros)


  def mediana(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a mediana dos numeros
    informados
    """
    return self.__statistic.mediana(numeros)


  def moda(self, numeros: list) -> list:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna uma lista com a moda
    dos números
    """
    return self.__statistic.moda(numeros)


  def variancia(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a variância desta amostra
    """
    return self.__statistic.variancia(numeros)


  def desvio_padrao(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna o desvio padrão desta amostra
    """
    return self.__statistic.desvio_padrao(numeros)


  def amplitude(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna sua amplitude
    """
    return self.__statistic.amplitude(numeros)


  def desvio_medio(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna seu desvio médio
    """
    return self.__statistic.desvio_medio(numeros)

  def erro_padrao(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna seu erro padrão
    """
    return self.__statistic.erro_padrao(numeros)


  def coeficiente_variacao(self, numeros: list) -> float:
    """
    esta função recebe como paremetro uma lista de números,
    ou uma matriz de números e retorna a porcentagem do 
    coeficiente de variação
    """
    return self.__statistic.coeficiente_variacao(numeros)