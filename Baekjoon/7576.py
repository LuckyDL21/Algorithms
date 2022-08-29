"""
7576.py

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1   --> 8

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1  --> -1

6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1  --> 6

주의 1이 여러개 있는 상태임이 핵심이다. 

exit(0) --> 코드 강제종료

result-1 헤줘야 

"""

from collections import deque

## 일단 코드 막짜보기, 시작점이 여러개이기 때문에 동시에 움직이는 것을 고려해야할 것 같음 


M,N=map(int,input().split()) ## row, column 

### change row, column ex> 접근 4 6으로 해야함 

result=0

map_info=[[int(x) for x in input().split()] for i in range(N)]


q=deque([])

## 처음 저장해야 

for i in range(N):
  for j in range(M):
    if map_info[i][j]==1:
      q.append([i,j])

## 상 하 좌 우 
dx=[0,0,-1,1]
dy=[1,-1,0,0]

## N: row M: column

def bfs():
  while q:
    x,y=q.popleft()
    for move in range(4):
      new_x=x+dx[move]
      new_y=y+dy[move]
      if 0<=new_x<N and 0<=new_y<M and map_info[new_x][new_y]==0:
        map_info[new_x][new_y]=map_info[x][y]+1 ## 기존값 +=1
        q.append([new_x,new_y])
      
bfs()


for sub in map_info:
  for j in sub:
    if j==0:
      print(-1)
      exit(0)

  result=max(result,max(sub))

print(result-1)