from collections import deque
from sys import stdin

N=int(stdin.readline())

stack=[]

for i in range(N):
  new_input=(stdin.readline())
  if 'push' in new_input:
    num=int(new_input[5:])
    stack.append(num)
  elif 'pop' in new_input:
    if len(stack)==0:
      print(-1)
    else:
      num=stack[-1]
      print(num)
      del stack[-1]
  elif 'size' in new_input:
    length=len(stack)
    print(length)
  elif 'empty' in new_input:
    if len(stack)==0:
      print(1)
    else:
      print(0)
  elif 'top' in new_input:
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])