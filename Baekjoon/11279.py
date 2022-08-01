"""
알고리즘 직접 구현시에는 기호를 바꾸면 되지만, 
library 사용시에는 - 기호 

최대힙: - 기호

"""


import sys
import heapq

N=int(input())
heap=[]
save_list=[]


for _ in range(N):
  get_number=int(sys.stdin.readline())
  if get_number!=0:
    heapq.heappush(heap,-get_number)
  else:
    try:
      save_list.append(-heapq.heappop(heap))
    except:
      save_list.append(0)


for num in save_list:
  print(num)
