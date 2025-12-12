with open("number.txt","w") as file:
  file.write("10\n20\n30\nabc\n40")
with open("number.txt","r") as file:
  number=file.readlines()
sum=0
for line in number:
    line=line.strip()
    try:
       number=int(line)
       sum+=number
    except ValueError:
       pass
print(f"the sum is {sum}")