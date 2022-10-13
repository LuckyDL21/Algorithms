"""
Baekjoon 3584 가까운 조상 
"""

def find(node,parent_set):
  global res
  if node==0 or res!=-1:
    return
  if node in parent_set:
    res=node
    return
  parent_set.add(node)
  find(parent_info[node],parent_set)
  

import sys

case=sys.stdin.readline().strip()


for _ in range(int(case)):
  
  N=int(sys.stdin.readline().strip())

  parent_info=[0 for i in range(N+1)]
  
  for _ in range(N-1):
    
    parent,child=map(int,sys.stdin.readline().split())
    
    parent_info[child]=parent

  que_one,que_two=map(int,sys.stdin.readline().split())
  
  ## find algorithms 

  parent_set=set()

  res=-1

  find(que_one,parent_set)
  find(que_two,parent_set)

  print(res)