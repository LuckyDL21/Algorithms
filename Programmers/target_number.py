## 더하기와 빼기만 가능하다.

import itertools

def solution(numbers, target):
    answer = 0 ## 방법의 수 
    
    candidates=['+','-']
        
    
    pl_ma=[] 
    
    possible_list=list(itertools.product(candidates,repeat=len(numbers)))
    
    
    print(len(possible_list))
    
    
    for sign in possible_list:
        result=0
        for sub_sign,number in zip(sign,numbers):
            if sub_sign=='-':
                number=-number
                result+=number
            else:
                result+=number
        if result==target:
            answer+=1
            
    
    
    return answer