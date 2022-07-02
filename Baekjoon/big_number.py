
result=[]
while True:
  num1,num2=map(int,input().split())

  if num1>num2:
    result.append('Yes')
  elif num1<=num2 and num1!=0 or num2!=0:
    result.append('No')

  if num1==0 and num2==0:
    break

print("\n".join(result))