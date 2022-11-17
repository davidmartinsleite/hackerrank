n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
notas = student_marks.get(query_name)
media = 0
for nota in notas:
    media += nota
media = media / len(notas)
print(f'{media:.2f}')
