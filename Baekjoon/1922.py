"""
1922

python sorted - lambda 

kruscal algorithms

부모를 찾는 함수필요

재귀
"""

N=int(input()) ## node
M=int(input())

graph_info=[]

for i in range(M):
  list_info=list(map(int,input().split()))
  graph_info.append(list_info)

graph_info=sorted(graph_info,key=lambda x:x[2])


parent_info=[parent for parent in range(N+1)]

def find_parent(x):
  if parent_info[x]!=x:
    parent_info[x]=find_parent(parent_info[x]) ## 갱신

  return parent_info[x]

cost=0

cost_node_info=[]

for standard in graph_info:
  left=find_parent(standard[0])
  right=find_parent(standard[1])
  if left!=right:
    cost+=standard[2]
    cost_node_info.append(standard)
    if left<right:
      parent_info[right]=left
    else:
      parent_info[left]=right


print(cost)