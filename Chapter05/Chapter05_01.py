n, m = map(int, input().split())
ice_tray = []
answer = 0

def dfs(graph, row, col):
    # 방문 처리
    graph[row][col] = 1

    if row > 0 and graph[row - 1][col] == 0:
        dfs(graph, row - 1, col)
    elif row < n - 1 and graph[row + 1][col] == 0:
        dfs(graph, row + 1, col)
    elif col > 0 and graph[row][col - 1] == 0:
        dfs(graph, row, col - 1)
    elif col < m - 1 and graph[row][col + 1] == 0:
        dfs(graph, row, col + 1)
    else:
        global answer
        answer += 1


for i in range(n):
    ice_tray.append(list(map(int, input())))

dfs(ice_tray, 0, 0)

print(answer)