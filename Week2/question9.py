num=[1,2,3,4,5,6,7,8]
target=int(input("Enter an intrger target number"))
for i in range(len(num)-1):
  for j in range(i+1,len(num)):
    if num[i]+num[j]==target and num[i]!=num[j]:
        print([i,j])
