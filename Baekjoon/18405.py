"""
18405번
경쟁적 전염 

BFS이고, 0일때에만 탐색을 진행하면된다. --> 역시나 좌표로 접근하자!

딕셔너리로 저장할 필요X  

** 주의: 맵의 좌표값과, 지정 위치값은 다름을 유념할것

sort --> 맨앞 원소를 기준으로 sort를 진행함 

"""

from collections import deque

N,K=map(int,input().split())

map_info=[[int(x) for x in input().split()] for i in range(N)]

S,X,Y=map(int,input().split())

## 바이러스 종류도 기록해야함 

## 바이러스 종류가 낮은 종류의 바이러스부터 증식하는게 keypoint 

virus_info=[]

## 1. 바이러스 위치 잡아내기 
for row in range(N):
  for column in range(N):
    if map_info[row][column]!=0:
      virus_info.append((map_info[row][column],row,column)) ##  virus,x,y

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(S,X,Y):
  queue=deque(virus_info)
  count=0
  while queue:
    if count==S:
      break
    for _ in range(len(virus_info)):
      virus,x,y=queue.popleft()
      for move in range(4):
        new_x=x+dx[move]
        new_y=y+dy[move]
        if 0<=new_x<N and 0<=new_y<N:
          if map_info[new_x][new_y]==0:
            map_info[new_x][new_y]=map_info[x][y]
            queue.append((map_info[new_x][new_y],new_x,new_y))
    count+=1
  return map_info[X-1][Y-1]

virus_info.sort()

print(bfs(S,X,Y))