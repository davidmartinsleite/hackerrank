import itertools

lista_A = map(int, input().split())
lista_A = list(lista_A)
lista_A.sort()

lista_B = map(int, input().split())
lista_B = list(lista_B)
lista_B.sort()


print(*list(itertools.product(lista_A, lista_B)))
