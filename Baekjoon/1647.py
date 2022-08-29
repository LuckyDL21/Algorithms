"""
1647 도시분할계획 
"""

node,paths=map(int,input().split())

graph_info=[]

for _ in range(paths):
  
  a,b,c=(map(int,input().split())) ### node1,node2, weight
  graph_info.append([c,a,b])


parent_list=[i for i in range(0,node+1)]

def find_parent(x):
  if parent_list[x]!=x:
    parent_list[x]=find_parent(parent_list[x])

  return parent_list[x]

def union(node_a,node_b):
  node_a=find_parent(node_a)
  node_b=find_parent(node_b)
  if node_a<node_b:
    parent_list[node_b]=node_a
  else:
    parent_list[node_a]=node_b

graph_info=sorted(graph_info,key=lambda x:x[2])

check_list=[]
cost=0

for weight,left,right in graph_info:
  if find_parent(left)!=find_parent(right):
    union(left,right)
    cost+=weight
    check_list.append(weight)

cost=cost-check_list.pop()

print(cost)  