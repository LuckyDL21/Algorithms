"""
1238.py -- 파티
longest student의 path length를 출력해야함
sort할필요 없음
무조건 source에서 인접한(adj) 애들 중에서 가장 작은애로만 움직임 
갈수있는 애들 중에서 작은애로

** 2차원 리스트 생성

[[0]*N for i in range(N)]

"""

"""
찍고나서 다시 돌아오는 것까지 생각해야함 
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)