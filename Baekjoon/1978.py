"""
1978.py - 소수 찾기 

Time: 15 minutes
"""
N=int(input())

################ 꼭 익히자 !! ############
get_list=list(map(int,input().split()))
########################################

overall_count=0

for num in get_list:
  count=0
  split_num=num//2
  if num==1:
    continue
  elif num==2:
    count=0
  else:
    candidates=[i for i in range(2,split_num+1)]
    for sub_num in candidates:
      if num%sub_num==0:
        count+=1
  if count==0:
    overall_count+=1

print(overall_count)