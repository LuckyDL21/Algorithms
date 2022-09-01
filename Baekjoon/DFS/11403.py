"""
11403.py
경로찾기 

3
0 1 0
0 0 1
1 0 0  
=====
1 1 1
1 1 1
1 1 1

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
=============
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0

--> 플로이드 - 워셜 알고리즘 --> 최단 경로를 계산할 필요가 없기 때문에 매우 간단 

"""

N=int(input())

map_info=[]

for i in range(N):
  sub_list=list(map(int,input().split()))
  map_info.append(sub_list)


for k in range(N):
  for i in range(N):
    for j in range(N):
      if map_info[i][k] and map_info[k][j]:
        map_info[i][j]=1


for i in range(N):
  new_str=""
  for j in range(N):
    new_str+=str(map_info[i][j])+" " ## 개행
  print(new_str)
  