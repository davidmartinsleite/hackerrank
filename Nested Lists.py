turma = []
aluno = []
ordem = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    aluno.append(name)
    aluno.append(score)
    turma.append(aluno[:])
    aluno.clear()

contagem = 0
for aluno in turma:
    if contagem == 0:
        ordem.append(aluno[:])
    elif aluno[1] >= ordem[-1][1]:
        ordem.append(aluno[:])
    else:
        pos = 0
        while pos < len(ordem):
            if aluno[1] <= ordem[pos][1]:
                ordem.insert(pos, aluno[:])
                break
            pos += 1
    contagem += 1

nomes = []
n = 0
while True:
    if ordem[n][1] == ordem[n + 1][1]:
        n += 1
    else:
        break

nomes.append(ordem[n + 1][0])
try:
    if ordem[n + 1][1] == ordem[n + 2][1]:
        nomes.append(ordem[n + 2][0])
except:
    pass
nomes.sort()
for n in nomes:
    print(n)
