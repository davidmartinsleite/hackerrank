import numpy

dimensao_matriz = map(int, input().split())
dimensao_matriz = list(dimensao_matriz)
fileira_de_numeros_01 = map(int, input().split())
fileira_de_numeros_01 = list(fileira_de_numeros_01)
fileira_de_numeros_02 = map(int, input().split())
fileira_de_numeros_02 = list(fileira_de_numeros_02)



change_array = numpy.array([fileira_de_numeros_01, fileira_de_numeros_02])
transpor_numero = numpy.transpose(change_array)
change_array.shape = (dimensao_matriz)
print(transpor_numero)
achatar_numeros = change_array.flatten()
print(achatar_numeros)
