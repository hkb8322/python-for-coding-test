INF = int(1e9)

# 회사 및 경로 개수 입력받기
n, m = map(int, input().split())

# 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 경로 초기화
for i in range(1, m + 1):
    a, b = map(int, input().split())

    # 연결되어 있는 경우 1만큼의 시간으로 이동 가능
    graph[a][b] = 1
    graph[b][a] = 1

# X번 회사, K번 회사 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for o in range(1, n + 1):
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            graph[p][q] = min(graph[p][q], graph[p][o] + graph[o][q])


# 최소 이동 시간 계산
answer = graph[1][k] + graph[k][x]

# 결과 출력
if answer >= INF:
    print(-1)
else:
    print(answer)

