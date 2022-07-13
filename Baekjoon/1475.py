N=input()
set_list=[num for num in range(0,10)]
freq=dict()

result=0

#### data input

for value in set_list:
  freq[str(value)]=0

for sub_char in N:
  freq[sub_char]+=1

    
#### output
  
if (freq['6']+freq['9'])%2==0:
    
  sub_result=(freq['6']+freq['9'])//2

  freq['6']=sub_result
  freq['9']=sub_result
  
else:
  sub_result=(freq['6']+freq['9'])//2+1

  freq['6']=sub_result
  freq['9']=sub_result

      
 
print(max(freq.values()))