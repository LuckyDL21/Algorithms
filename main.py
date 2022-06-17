# 1<=n<=25

"""
대문자끼리

소문자끼리

공백제거 

"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"

## keypoint

1.ascii_uppercase,ascii_lowercase
2.isupper,islower

"""

from string import ascii_lowercase
from string import ascii_uppercase

def solution(s, n):
    #sentence=s.replace(" ","")  ## remove strip    
    upper_list=list(ascii_uppercase) ##list
    lower_list=list(ascii_lowercase)
    
    result=[]
    
    for i in range(len(s)):
        if s[i].isupper()==True:
            for idx in range(len(upper_list)):
                if s[i]==upper_list[idx]:
                    new_idx=idx+n
                    if new_idx>=len(upper_list)-1:
                        new_idx=new_idx-(len(upper_list)-1)-1
                        result.append(upper_list[new_idx])
                    else:
                        result.append(upper_list[new_idx])
        elif s[i].islower()==True:
            for idx in range(len(lower_list)):
                if s[i]==lower_list[idx]:
                    new_idx=idx+n
                    if new_idx>=len(lower_list)-1:
                      new_idx=new_idx-(len(lower_list)-1)-1
                      result.append(lower_list[new_idx])
                    else:
                      result.append(lower_list[new_idx])
        elif s[i]==' ':
          result.append(s[i])
          
    answer="".join(result)            
            
    return answer


if __name__=="__main__":
  s=["AB","z","a B z"]
  n=[1,1,4]
  for sentence,idx in zip(s,n):
    answer=solution(sentence,idx)
    print(answer)