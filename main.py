"""
2529.py 부등호
예제 01)

[입력]
2
< >
[출력]
897
021

예제 02)

[입력]
9
> < < < > > > < <
[출력]
9567843012
1023765489

## 0 ~ 9

** Hint: python permutation 

flag 변수를 줌으로써, 후보 리스트에 넣을 변수 안넣을 변수를 찾을 수 있다. 
flag가 false이면 즉시 탐색을 종료해야한다. 


"""

import itertools

number=int(input())

mark_list=list(input().split())

number_len=len(mark_list)+1

result=[]

for idx,value in enumerate(itertools.permutations([0,1,2,3,4,5,6,7,8,9],number_len)):
  for i in range(len(mark_list)):
    flag=True
    if mark_list[i]=='<':
      if value[i]<value[i+1]:
        continue
      else:
        flag=False
        break
    else:
      if value[i]>value[i+1]:
        continue
      else:
        flag=False
        break

  if flag:
    result.append(value)


print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))