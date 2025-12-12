with open("sales.txt","w") as file:
  file.write("200\n450\nabc\n700")
with open("sales.txt","r") as file:
  sales_number=file.readlines()
for line in sales_number:
    ##line=line.strip()
    try:
       sales_number=int(line)
       print(sales_number)
    except ValueError:
       print(f"invalid sales number {line}")

