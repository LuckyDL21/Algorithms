"""
이상한 문자 만들기 

각 단어는 하나이상의 공백문자로 구분됨: 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자 

"try hello world"	"TrY HeLlO WoRlD"
"""


s=input()

word_list=list(s.split(' '))

print(word_list)

change_list=[]
for word in word_list:
  change=''
  for idx in range(len(word)):
    if idx%2==0:
      change+=word[idx].upper()
    else:
      change+=word[idx].lower()
  change_list.append(change)

result=''

for sub_word in change_list:
  result+=sub_word
  result+=' '
result=result.rstrip()

print(result)