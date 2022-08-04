"""
1748.py
수이어쓰기
리스트에 넣고 저장했다가 빼는 방식으로 
- 파이썬 
- 거듭제곱: **
- del은 index 삭제
- remove는 삭제할 수를 삭제
- 해당하는 인덱스 삭제:a.index(want_value
"""

### 1<=N<=100,000,000=10^9


num=int(input())
result=0

candidates=[sub_num for sub_num in range(1,num+1)]
number_length=len(str(num))
for counting in range(number_length,0,-1):
  split_numbering=10**(counting-1) ## value
  idx=candidates.index(split_numbering)
  result+=(len(candidates[idx:])*counting)
  del candidates[idx:]

print(result)