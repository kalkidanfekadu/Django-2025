with open("sales.txt","r") as file:
  sales_number=file.readlines()
new_list=[]
total_sales=0
for line in sales_number:
    line=line.strip()
    try:
       sales_number=int(line)
       print(sales_number)
       new_list.append(sales_number)
    except ValueError:
       pass
for n in new_list:
   total_sales+=n
print(f"the total sale is {total_sales}")