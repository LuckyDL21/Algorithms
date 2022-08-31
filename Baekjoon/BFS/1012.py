"""
1012.py 
유기농 배추
"""

import sys
from collections import deque

T=int(sys.stdin.readline().strip()) ## 맵반복

## 가로길이,세로길이,배추가 심어져있는 위치 

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(map_info,a,b):
  queue=deque([])
  queue.append([a,b])
  map_info[a][b]=0
  while queue:
    x,y=queue.popleft()
    for z in range(4):
      new_x=x+dx[z]
      new_y=y+dy[z]
      if 0>new_x or new_x>=M or new_y<0 or new_y>=N:
        continue
      if map_info[new_x][new_y]==1:
        map_info[new_x][new_y]=0
        queue.append([new_x,new_y])
  
for i in range(T): ## movement
  M,N,K=map(int,input().split())
  count=0
  map_info=[[0]*N for _ in range(M)]
  for j in range(K):
    input_x,input_y=map(int,input().split())
    map_info[input_x][input_y]=1

  for a in range(M):
    for b in range(N):
      if map_info[a][b]==1:## 배추가 있어용
        bfs(map_info,a,b) ## 탐색
        count+=1

  print(count)