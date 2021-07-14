class Calculate:


  @staticmethod
  def get_numeros(numeros: list) -> list:
    lista = []
    for numero in numeros:
      if type(numero) is list:
        for sub in Calculate.get_numeros(numero):
          lista.append(sub)
      else:
        lista.append(numero)
    return lista
