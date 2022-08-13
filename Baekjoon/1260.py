"""
1260

DFS & BFS

print(end=' ')

dfs -recursive
bfs - queue

"""
from collections import deque

v,w,start=map(int,input().split())

adj_matrix=[[0]*(v+1) for _ in range(v+1)]
visited=[False]*(v+1)


for i in range(w):
  v1,v2=map(int,input().split())
  adj_matrix[v1][v2]=adj_matrix[v2][v1]=1

def dfs(start):
  visited[start]=True

  print(start,end=' ')

  for i in range(1,v+1):
    if visited[i]==False and adj_matrix[start][i]==1:
      dfs(i)

## 반대로 생각
def bfs(start):
  q=deque()
  q.append(start)

  visited[start]=False
  while q:
    target=q.popleft()
    print(target,end=' ')
    for new_vertex in range(1,v+1):
      if visited[new_vertex]==True and adj_matrix[target][new_vertex]==1:
        q.append(new_vertex)
        visited[new_vertex]=False

dfs(start)
print()
bfs(start)