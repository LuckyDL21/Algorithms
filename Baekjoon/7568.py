"""

7568.py

반복문을 돌릴때 자기 자신을 포함해도 사실상 무관하다고 볼 수 있다. 

- input

5
55 185         2       
58 183         2             2
88 186         1             1
60 175         2
46 155         5

- output

2 2 1 2 5

- 2 ≤ N ≤ 50
- 10 ≤ x, y ≤ 200

"""


N=int(input())

candidates=[]
priority=[]

## data input

for i in range(N):
  values=list(map(int,input().split()))
  #print('values',values)
  candidates.append(values)

  
### compare 

for idx in range(N):
  number=1
  for j in range(N):
    if candidates[idx][0]<candidates[j][0] and candidates[idx][1]<candidates[j][1]:
      number+=1
  priority.append(str(number))
      

print(' '.join(priority))