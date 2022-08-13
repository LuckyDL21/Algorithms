"""
4485 who is jelda?

예외적으로 처음 distance도 cost가 있다. 좌표값이 곧 weight

"""
import heapq

INF = int(1e9)

def dij(start):
  q=[]
  cost_list=[[INF]*N for _ in range(N)] ## cost_list

  heapq.heappush(q,(graph[start[0]][start[1]],start)) ## cost, position(좌표)
  cost_list[start[0]][start[1]]=0
  
  ## 좌우상하 
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  
  while q:
    now_cost,now_node=heapq.heappop(q)

    if now_node==(N-1,N-1):
      print(f'Problem {count}: {cost_list[now_node[0]][now_node[1]]}')
      break
    
    for idx in range(4):
      move_x=now_node[0]+dx[idx]
      move_y=now_node[1]+dy[idx]
      if 0<=move_x<N and 0<=move_y<N:
        new_cost=now_cost+graph[move_x][move_y]
        if cost_list[move_x][move_y]>new_cost:
          cost_list[move_x][move_y]=new_cost
          heapq.heappush(q,(new_cost,(move_x,move_y)))

count=1
while True:
  N=int(input())
  if N==0:
    break
  graph=[list(map(int,input().split())) for _ in range(N)]
  
  dij((0,0))
  count+=1