"""
Baekjoon 1593

4 11
cAda
AbrAcadAbRa
"""
## 익히기

import itertools  ## list를 통해 permutation을 만들어주는 기능 d

g,s=map(int,input().split())

w=input()
w=list(w)

s=input()

npr=list(itertools.permutations(w,g))

result=[]

for i in range(len(npr)):
  sub_str=''
  for j in npr[i]:
    sub_str+=j
  result.append(sub_str)

#print(result)

count=0

for str in result:
  if str in s:
    count+=1
    
print(count)


"""
test=('a', 'b', 'c', 'd')

result=''

for i in test:
  result+=i

print(result)

## 이중반복문을 꼭사용해야 되는 걸까??
"""