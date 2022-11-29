area = map(int, input().split())
area = list(area)
print(area)
titulo = 'WELCOME'
simbulo = simbuloBase = '.|.'
altura = int(area[0] /2)
elementos = -1
print(altura)
for linha in range(altura):
    print(simbulo.center(area[1], '-'))
    simbulo += simbuloBase * 2
    elementos += 2
print(titulo.center(area[1], '-'))
for linha in range(altura):
    print(simbulo[0:elementos*3].center(area[1], '-'))
    elementos -= 2
