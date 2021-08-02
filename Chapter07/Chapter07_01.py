import sys

# 가게 정보
n = int(input())
product = list(map(int, sys.stdin.readline().rstrip().split()))

# 손님의 확인 요청
m = int(input())
request = list(map(int, sys.stdin.readline().rstrip().split()))

for number in request:
    if number in product:
        print("yes", end=' ')
    else:
        print("no", end=' ')

