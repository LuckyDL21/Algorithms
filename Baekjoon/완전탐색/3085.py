"""
3085.py 사탕게임 

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수 --> brute
"""

from collections import defaultdict

N=int(input())

map_info=[]

maxcount=0

for i in range(N):
  a=input()
  map_info.append(list(a))


### row_check
def row_check():
  global maxcount
  for i in range(N):
    count=1
    for j in range(N-1):
      if map_info[i][j]==map_info[i][j+1]:
        count+=1
        maxcount=max(maxcount,count)
      else:
        count=1
      
### column_check
def column_check():
  global maxcount
  for i in range(N):
    count=1
    for j in range(N-1):
      if map_info[j][i]==map_info[j+1][i]:
        count+=1
        maxcount=max(maxcount,count)
      else:
        count=1


## main

for i in range(N):
  for j in range(N-1):
    if map_info[i][j]!=map_info[i][j+1]:
      map_info[i][j],map_info[i][j+1]=map_info[i][j+1],map_info[i][j]
      row_check()
      column_check()
      map_info[i][j+1],map_info[i][j]=map_info[i][j],map_info[i][j+1]

    if map_info[j][i]!=map_info[j+1][i]:
      map_info[j][i],map_info[j+1][i]=map_info[j+1][i],map_info[j][i]
      row_check()
      column_check()
      map_info[j+1][i],map_info[j][i]=map_info[j][i],map_info[j+1][i]
      
      
print(maxcount)