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

"""

numbers=int(input())

figure_list=list(input().split())

all_numbers=[0 for i in range(numbers+1)]

range=[ i for i in range(10)]

possible_num=[]

## 완탐 
## 모든숫자 다넣기 

all_possible_num=''

for i in range(len(figure_list)):
  if figure_list[i]=='<':
    for j in range(len(range)):
      all_numbers[i]=range[j]
      not_standard_list=[z for z in range if z >=all_numbers[i]]
      for z in not_standard_list:
        possible_num.append(int(str(all_numbers[i])+str(z)))
  else:
    for w in range()