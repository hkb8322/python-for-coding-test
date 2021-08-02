n, m = map(int, input().split())

number = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    number[i] = list(map(int, input().split()))
    number[i].sort()

    if answer < number[i][0]:
        answer = number[i][0]

print(answer)
