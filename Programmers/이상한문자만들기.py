"""
대문자화 -- upper()
소문자화 -- lower()


"""

def solution(s):
    word_list=list(s.split(' '))
    change_list=[]
    answer=''
    for word in word_list:
        for idx in range(len(word)):
            if idx%2==0:
                answer+=word[idx].upper()
            else:
                answer+=word[idx].lower()
        answer+=' '
    
    answer =answer[:-1]
    return answer