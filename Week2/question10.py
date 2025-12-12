x=int(input("enter the number"))
original=x
reversed_num=0
while x>0:
  digit=x%10
  reversed_num=(reversed_num*10)+digit
  x//=10
if original==reversed_num:
  print(original, "is a palindrome")
else:
  print(original, "is not a palindrome")

