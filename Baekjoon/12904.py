"""
c

1. 문자열 뒤에 A추가
2. 문자열 뒤집고 뒤에 B추가 

S -> T possible 1 impossible 0
-------------
B
ABBA --> 1
-------------

------------
AB
ABB --> 0
------------

"""

import sys
from collections import deque

source=list(map(str, input())) ## S ## string
target=list(map(str, input())) ## T

while len(source)!=len(target):
  if target[-1]=='A':
    target.pop()

  elif target[-1]=='B':
    target.pop()
    target=target[::-1]

if source==target:
  print(1)
else:
  print(0)