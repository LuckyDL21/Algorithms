"""
4673.py 셀프넘버

keypoint: % //
코드 단순하게 짜봄 (직관적으로)

참고하기: 재귀함수 (j022207)

"""

all_list=[i for i in range(1,10001)]
oper_list=[]


for num in range(1,10001):
  if 1<=num<10:
    make_num=num+num
    oper_list.append(make_num)
  elif 10<=num<100:
    one_element=num//10
    two_element=num%10
    make_num=num+one_element+two_element
    oper_list.append(make_num)
    
  elif 100<=num<1000:
    one_element=num//100
    two_element=(num-(one_element*100))//10
    three_element=(num-(one_element*100))%10
    make_num=num+one_element+two_element+three_element
    oper_list.append(make_num)
  elif 1000<=num<10000:
    one_element=num//1000
    two_element=(num-(one_element*1000))//100
    three_element=((num-(one_element*1000))-(two_element*100))//10
    four_element=((num-(one_element*1000))-(two_element*100))%10
    make_num=num+one_element+two_element+three_element+four_element
    oper_list.append(make_num)
  elif num==10000:
    one_element=num//10000
    two_element=(num-(one_element*10000))//1000
    three_element=((num-(one_element*10000))-(two_element*1000))//100
    four_element=((num-(one_element*10000))-(two_element*1000)-(three_element*100))//10
    five_element=((num-(one_element*10000))-(two_element*1000)-(three_element*100))%10
    make_num=num+one_element+two_element+three_element+four_element+five_element
    oper_list.append(make_num)
  
for num in all_list:
  if num not in oper_list:
    print(num)
