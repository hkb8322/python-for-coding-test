n = int(input())
data = []

for i in range(n):
    input_data = input().split()
    data.append((input_data[0], input_data[1]))

data = sorted(data, key=lambda item: item[0])

for student in data:
    print(student[0], end=' ')
