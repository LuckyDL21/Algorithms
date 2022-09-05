"""
1244.py 스위치 켜고 끄기 

"""

switch_num=int(input())

switch_info=list(map(int,input().split()))

#### 학생수 
grad_num=int(input())

## 성별 받음수 

grad_info=[]

for i in range(grad_num):
  gender,number=map(int,input().split())
  grad_info.append([gender,number])

"""
*** output: 최종출력 
** 고려: 성별, 받은숫자 , 
21번 스위치 --> 둘째줄 맨앞에 출력하기 

gender --- 1: 남학생 2: 여학생 

8
0 1 0 1 0 0 0 1
2
1 3
2 3

1 0 0 0 1 1 0 1


## Man info: [0, 1, 1, 1, 0, 1, 0, 1]

## [1,0,0,0,1,1,0,1]

"""

for gender,number in grad_info:
  if gender==1:
    mal_list=[]
    temp_num=number
    while temp_num<=switch_num:
      if switch_info[temp_num-1]==1:
        switch_info[temp_num-1]=0
      else:
        switch_info[temp_num-1]=1
      temp_num+=number
  else:
    if switch_info[number-1]==1:
      switch_info[number-1]=0
    else:
      switch_info[number-1]=1
    idx1=number ## -
    idx2=number ## +
    while idx1>1 and idx2<switch_num:
      idx1-=1
      idx2+=1
      if switch_info[idx1-1]!=switch_info[idx2-1]:
        break
      elif switch_info[idx1-1]==switch_info[idx2-1]:
        if switch_info[idx1-1]==1:
          switch_info[idx1-1]=0
          switch_info[idx2-1]=0
        else:
          switch_info[idx1-1]=1
          switch_info[idx2-1]=1

    
### switch_info

result=''

sub_value=1

for i in range(len(switch_info)):
  result=result+str(switch_info[i])+' '
  if i==(20*sub_value-1):
    result+='\n'
    sub_value+=1

print(result)