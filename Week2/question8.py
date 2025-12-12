num=[0,1,0,3,12]
non_zero_index=0
for i in range(len(num)):
  if num[i]!=0:
    num[non_zero_index]=num[i]
    non_zero_index+=1
for i in range(non_zero_index,len(num)):
    num[i]=0
print(num)