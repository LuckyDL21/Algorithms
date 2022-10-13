"""

answer = [x,y]라 쳤을때
(x-2)*(y-2) = yellow; 
"""

def solution(brown, yellow):
    answer = [] ## 가로길이, 세로길이 
    
    big=brown+yellow
    
    ## (1) 큰 사각형
    candidates1=[]
    for i in range(1,big+1):
        if big%i==0:
            if i>=big//i:
                candidates1.append((i,big//i))
                
    #print(candidates1)
    
    ## (2) 작은 사각형 
    candidates2=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            if i>=yellow//i:
                candidates2.append((i,yellow//i))
                
    #print(candidates2)
    
    for x_big,y_big in candidates1:
        for x_small,y_small in candidates2:
            if x_big-x_small>=2 and y_big-y_small>=2 and (x_big-x_small)%2==0 and (y_big-y_small)%2==0:
                answer.append(x_big)
                answer.append(y_big)
                break
            else:
                continue
    

    return answer