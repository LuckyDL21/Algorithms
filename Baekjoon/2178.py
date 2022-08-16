"""
2178
(1,1) --> (N,M)

"""
from collections import deque

N,M=map(int,input().split())

map_list=[]

for _ in range(N):
  new_column=input()
  map_list.append(list(new_column)) ## string 


## 좌우상하 
dx=[-1,1,0,0]
dy=[0,0,1,-1]

## have to change string to number

q=deque()
q.append([0,0])


while q:
  point=q.popleft()
  for i in range(4):
    move_x=point[0]+dx[i]
    move_y=point[1]+dy[i]
    if 0<=move_x<N and 0<=move_y<M:
      if int(map_list[move_x][move_y])==1: ## not visit and search possible 
        q.append([move_x,move_y])
        map_list[move_x][move_y]=int(map_list[point[0]][point[1]])+1 ## cost_change

print(map_list[N-1][M-1])