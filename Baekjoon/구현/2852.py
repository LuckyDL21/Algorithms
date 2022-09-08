"""
2852 NBA 농구 

농구경기: 48분 

* 예제 01
입력 
1
1 20:00
출력 
28:00 team 01
00:00 team 02

* 예제 02
입력3
1 01:10 
2 21:10
2 31:30

출력 
20:00 team 01
16:30 team 02

* 예제 03 
입력 

5
1 01:10
1 02:20
2 45:30
2 46:40
2 47:50

출력 

45:30 team 01
00:10 team 02

## 얼마나의 시간동안 출력되는가? 

--> 인덱스를 양옆끼리 비교하기보다는 그냥 <변수 하나>로 판별하는게 낫다. 

>>> "{:0>2d}".format(3)
'03'

"""
##
import sys
input = sys.stdin.readline

n = int(input())
score = {1: 0, 2: 0}
time = {1: 0, 2: 0}
ans = {1: 0, 2: 0}
state = 0  # 0 even, 1 team1 leads, 2 team2 leads


for _ in range(n):
    team, t = input().split()
    team = int(team)
    m, s = map(int, t.split(':'))
    t = m*60+s
    score[team] += 1

    if state == 0:
        time[team] = t
        state = team
    elif state != 0 and score[1] == score[2]:
        ans[state] += t-time[state]
        state = 0

if state != 0:
    ans[state] += 60*48-time[state]

print('{:0>2}:{:0>2}'.format(ans[1]//60, ans[1] % 60))
print('{:0>2}:{:0>2}'.format(ans[2]//60, ans[2] % 60))