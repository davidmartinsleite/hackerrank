import numpy

numeros_matriz = map(int, input().split())
numeros_matriz = list(numeros_matriz)

change_array = numpy.array(numeros_matriz)
change_array.shape = (3, 3)
print(change_array)
