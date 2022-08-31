"""

1931.py 회의실 

TIP: 걸리는 시간은 상관없어 보임 

"""

import sys
from collections import deque

N=int(sys.stdin.readline().strip())

all_info=[] ## queue

for i in range(N):
  start,end=map(int,input().split())
  diff=end-start
  all_info.append([start,end])

## 두가지 조건으로 sorting진행 
## 작으면서 겹치지 않는!! 
all_info.sort(key=lambda x:x[0])
all_info.sort(key=lambda x:x[1])


#### 제일앞
count=1
end_point=all_info[0][1]

for i in range(1,N):
  if all_info[i][0]>=end_point:
    count+=1
    end_point=all_info[i][1]

print(count)