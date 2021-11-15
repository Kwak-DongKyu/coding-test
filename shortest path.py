#다익스트라 최단경로 알고리즘, 플로이드 워셜 ㅂㄹ만 포드 알고리즘
#다익스트라 최단 경로 알고리즘 : 음의 간선이 없을 때
#1. 출발 노드 설정 2. 최단 거리 테이블 초기화 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 4. 최단 거리 테이블 갱신 5. 3,4반복


#전보
# INF = int(1e9)
# n, m, c = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for a in range(n+1):
#     for b in range(n+1):
#         if a==b:
#             graph[a][b] = 0
#
# for i in range(m):
#     a, b, d = map(int, input().split())
#     graph[a][b] = d
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
#
# sum = 0
# sum2 = 0
# for i in range(1, n+1):
#     if c != i and graph[c][i] < INF:
#         sum += 1
#         sum2 = max(sum2, graph[c][i])
#
# print(sum, sum2)



#미래도시
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a==b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# x, k = map(int, input().split())
# distance = graph[1][k] + graph[k][x]
#
# if distance >= INF:
#     print(-1)
# else:
#     print(distance)

#플로이드 워셜 알고리즘 : 모든 노드에서 다른 모든 지점까지의 최단 경로를 구함
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[INF] * (n+1) for _ in range(n+1)]
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             if graph[a][b] > graph[a][k] +graph[k][b]:
#                 graph[a][b] = graph[a][k] + graph[k][b]
#
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if graph[a][b] == INF:
#             print("infinity", end=' ')
#         else:
#             print(graph[a][b], end =' ')
#     print('')




# #2개선된 다익스트라 알고리즘 소스코드
# # heapq는 이진트리 기반의 최소 힙 자료구조를 제공한다. k번쨰는 자식 노드인 2k+1, 2k+2보다 작은값을 만족한다.
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#
# def dijkstra(start):
#     q=[]
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("도달불가능")
#     else:
#         print(distance[i])





#1 간단한 다익스트라 알고리즘
# import sys
# input = sys.stdin.readline
# INF=int(1e9)
# n,m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
#
# for i in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#
# def get_smallest_node():
#     min_value = INF
#     index =0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])
