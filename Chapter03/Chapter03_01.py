n, m, k = map(int, input().split())
number = list(map(int, input().split()))

number.sort(reverse=True)

answer = number[0] * k * (m // k) + number[1] * (m % k)

print(answer)
