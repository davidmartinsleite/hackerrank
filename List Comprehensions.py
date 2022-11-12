# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

x = 1
y = 1
z = 1
n = 2

lista = []

for dados_x in range(x+1):
    for dados_y in range(y+1):
        for dados_z in range(z+1):
            lista.append([dados_x, dados_y, dados_z])


nova_lista = []
# for valor_maximo in lista:
#     if max(valor_maximo) <= n and sum(valor_maximo) < n:
#         nova_lista.append(valor_maximo)
# nova_lista.append(lista[-1])
# print(nova_lista)

for soma in lista:
    if not sum(soma) == n:
        nova_lista.append(soma)
print(nova_lista)
