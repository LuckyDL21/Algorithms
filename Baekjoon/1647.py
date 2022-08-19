"""
1647 도시분할계획 
"""

node,paths=map(int,input().split())

graph_info=[]

for _ in range(paths):
  
  new_info=list(map(int,input().split())) ### node1,node2, weight
  graph_info.append(new_info)


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

for left,right,weight in graph_info:
  if find_parent(left)!=find_parent(right):
    union(left,right)
    check_list.append(weight)
  else:
    continue

overall_cost=sum(check_list[:-1])

print(overall_cost)  