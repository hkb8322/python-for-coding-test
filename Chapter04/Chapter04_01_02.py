n = int(input())
answer = 0

for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if (str(hour) + str(minute) + str(second)).find('3') > -1:
                answer += 1

print(answer)