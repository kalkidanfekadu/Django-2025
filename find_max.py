n=int(input("enter how many numbers do u want to add" ))
my_list=[]
for i in range(n):
  num=input(f"enter number {i+1}: ")
  my_list.append(num)
max=my_list[0]
for i in range(n):
  if my_list[i]>max:
    max=my_list[i]
print(f"the maximum number is; {max}")
