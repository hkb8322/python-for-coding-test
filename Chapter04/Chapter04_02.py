location = input()
x = ord(location[0]) - 96
y = int(location[1])

move = [(-2, 1), (2, 1), (-2, -1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
answer = 0

for i in range(len(move)):
    nx = x + move[i][0]
    ny = y + move[i][1]

    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    else:
        answer += 1

print(answer)