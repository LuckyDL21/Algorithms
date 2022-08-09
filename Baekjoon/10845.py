from collections import deque
from sys import stdin

N=int(stdin.readline())

queue=deque()

for i in range(N):
  new_input=(stdin.readline())
  if 'push' in new_input:
    num=int(new_input[5:])
    queue.append(num)
    print
  elif 'pop' in new_input:
    if len(queue)==0:
      print(-1)
    else:
      num=queue.popleft()
      print(num)
  elif 'size' in new_input:
    length=len(queue)
    print(length)
  elif 'empty' in new_input:
    if len(queue)==0:
      print(1)
    else:
      print(0)
  elif 'front' in new_input:
    if len(queue)==0:
      print(-1)
    else:
      print(queue[0])
  elif 'back' in new_input:
    if len(queue)==0:
      print(-1)
    else:
      print(queue[-1])