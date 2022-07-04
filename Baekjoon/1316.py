"""
1316.py - 그룹 단어 체커 

배운점:sort, sorted, sort(key=len)
keypoint: defaultdict

"""

from collections import defaultdict

N=int(input())

count=0

for i in range(N):
  new_str=input()
  alpha_dict=defaultdict(list)
  for i in range(len(new_str)):
    alpha_dict[new_str[i]].append(i)
  get_values=list(alpha_dict.values())
  #print('get_values',get_values)
  alpha_count=0
  true_false_saved=[]
  for sub_list in get_values:
    if len(sub_list)>1:
      threshold=len(sub_list)
      idx=0
      one_count=None
      #true_false_saved=[]
      save_sub=[]
      while idx+1!=len(sub_list):
        sub=sub_list[idx+1]-sub_list[idx]
        #print('sub_list',sub_list,'sub',sub)
        save_sub.append(sub)
        idx+=1
      #print('save_sub',save_sub)
      for element in save_sub:
        if element!=1:
          one_count=False
          true_false_saved.append(one_count)
        else:
          one_count=True
          true_false_saved.append(one_count)
      #print('true_false_saved:',true_false_saved)
    else:## 한개의 단어만 출력했을 경우
      alpha_count+=1
    if len(get_values)==alpha_count:
      count+=1
      #print('**')

  if (False not in true_false_saved) and (true_false_saved!=[]): ##
    count+=1
    #print('##')

print(count)