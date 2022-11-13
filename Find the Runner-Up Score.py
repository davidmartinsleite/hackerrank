n = int(input())
arr = map(int, input().split())  # essa entrada é bem interessante,
                                 # dados inteiros saparados por espaços
arr = list(arr)
igual = 0
partidas = []


arr.sort()
while True:
    if not arr[-1 - igual] == arr[-2 - igual]:
        vice = arr[-2 - igual]
        break
    igual += 1
print(vice)
