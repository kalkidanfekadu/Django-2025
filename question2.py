prices=[120,45,300,85,150]
def get_expensive_product(price):
  new_list=[]
  for n in prices:
    if n>100:
      new_list.append(n)
  return new_list
result=get_expensive_product(prices)
print(f"the new price list is {result}")

  