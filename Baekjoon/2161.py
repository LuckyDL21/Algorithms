"""

2161.py
---------
버리고 맨 밑으로 옮기기 반복 
---------
"""

"""
** Think: while문 리스트안에 반복하는 과정 진행 

Algorithms: implement, data structure, queue

"""

N=int(input())

card_numbers=[i for i in range(1,N+1)] ## deque

result=[]

while len(card_numbers)!=1:
  
  throw_card=card_numbers[0]
  card_numbers.remove(throw_card) ## popleft
  result.append(str(throw_card))
  
  go_back_card=card_numbers[0]
  card_numbers.remove(go_back_card)
  card_numbers.append(go_back_card)


result.append(str(card_numbers[0]))

print(" ".join(result))