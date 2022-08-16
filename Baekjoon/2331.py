"""
2331.py -- 반복수열

queue

"""
from collections import deque

A,P=map(int,input().split())

q=deque()
q.append(A)

save_all_list=[]
save_all_list.append(A)

while q:
  value=q.popleft()
  value_str=str(value)
  new_value=0
  for i in range(len(value_str)):
    new_value+=(int(value_str[i])**P)

  if new_value not in save_all_list:
    q.append(new_value)
    save_all_list.append(new_value)
  else:
    duplicate_point=new_value
    break

duplicate_idx=0

for idx,value in enumerate(save_all_list):
  if value==duplicate_point:
    duplicate_idx=idx
    break

print(len(save_all_list[:duplicate_idx]))