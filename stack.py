#from collections import deque

# graph = [[], [ 2,3,8], [ 1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# visited = [False] * 9
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# bfs(graph, 1, visited)

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v , end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# dfs(graph, 1, visited)

n, m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or y <0 or x >= n or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x , y-1)
        dfs(x , y+1)
        dfs(x + 1, y)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)