N = int(input())
lista = []


for turno in range(N):
    entrada = input()
    funcao = entrada.split(' ')
    if funcao[0] == 'insert':
        lista.insert(int(funcao[1]), int(funcao[2]))
    if funcao[0] == 'print':
        print(lista)
    if funcao[0] == 'remove':
        lista.remove(int(funcao[1]))
    if funcao[0] == 'append':
        lista.append(int(funcao[1]))
    if funcao[0] == 'sort':
        lista.sort()
    if funcao[0] == 'pop':
        lista.pop()
    if funcao[0] == 'reverse':
        lista.reverse()
