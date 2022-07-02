"""
Problem 2577.py

"""

## 100<=all_num<=1000

num1=int(input())
num2=int(input())
num3=int(input())

multi_num=num1*num2*num3

num_check=dict()

for i in range(10):
  num_check[i]=0


## 한글짜씩 split
new_list=list(str(multi_num))

## input
for sub_num in new_list:
  num_check[int(sub_num)]+=1


## print
for value in num_check:
  print(num_check[value])