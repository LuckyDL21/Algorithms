"""
1439.py

문자 두쌍씩 비교해서 풀려했음

알고리즘 분류
--> 문자열, 그리디 알고리즘 

"""


string=input()

change_to_zero=0
change_to_one=0

for idx in range(0,len(string)-1):
  if string[idx]!=string[idx+1] and string[idx]=='0':
    change_to_one+=1
  elif string[idx]!=string[idx+1] and string[idx]=='1':
    change_to_zero+=1

## last string

if string[-1]=='0':
  change_to_one+=1
elif string[-1]=='1':
  change_to_zero+=1

print(min(change_to_zero,change_to_one))


    