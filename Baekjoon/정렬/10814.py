"""
Baekjoon 10814 나이순 정렬
3
21 junjyu
21 dohyun
20 sunyoung 

"""

import sys

N = sys.stdin.readline().strip()

info_list=[]

for i in range(int(N)):
  age,name=sys.stdin.readline().strip().split()
  info_list.append((int(age),name,i+1))## 나이 이름 가입 순서 


new_info=sorted(info_list,key=lambda x:(x[0],x[2]))

for i in new_info:
  print(i[0],i[1])