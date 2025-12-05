n=int(input("Enter a non negative integer"))
x=n
for i in range(20):
  x=0.5*(x+n/x)
print("the square root is", int(x))