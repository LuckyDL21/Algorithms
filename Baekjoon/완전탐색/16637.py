"""
16637번 

9
3+8*7-9*2

5
8*3+5

7
8*3+5+2

19
1*2+3*4*5-6*7*8*9*0

19
1*2+3*4*5-6*7*8*9*9

19
1-9-1-9-1-9-1-9-1-9

1. Idea1 - queue에 넣어서 cal_num을 실행하는 함수 1

2. Idea2 - cal_num을 실행하는 함수 

list queue

"""

import sys

def calculate(num1,num2,oper)->int:
  if oper=='*':
    result=num1*num2
  elif oper=='-':
    result=num1-num2
  else:
    result=num1+num2
  return result

## 하나의 oper만 계산하는 함수 
def insert_func(queue):
  result=queue[0] ## 초기 result
  for i in range(0,len(queue)-2,2):
    oper=queue[i+1]
    result=calculate(queue[i],queue[i+2],oper)

  return result

  
## 괄호를 넣었을때와 넣지 않았을때의 결과 

def basket(idx,queue):

  if idx==N-1:
    insert=queue+[get_info[idx]]
    return insert_func(insert)
  if idx==N-3:
    no_insert=queue+[get_info[idx],get_info[idx+1]]
    insert_value=calculate(get_info[idx],get_info[idx+2],get_info[idx+1])
    insert=queue+[insert_value]
    return max(basket(idx+2,no_insert),insert_func(insert))

  candidates1=queue+[get_info[idx],get_info[idx+1]]

  candidates2=queue+[calculate(get_info[idx],get_info[idx+2],get_info[idx+1]),get_info[idx+3]]

  return max(basket(idx+2,candidates1),basket(idx+4,candidates2))



N=int(sys.stdin.readline().strip())

get_info=[int(x) if x!='*' and x!='-' and x!='+' else x for x in sys.stdin.readline().strip()]

print(basket(0,[]))