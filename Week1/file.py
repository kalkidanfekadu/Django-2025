with open("kal.txt","w") as file:
  file.write("helloworld")
with open("kal.txt") as file:
  content=file.read()
  print(content)
try:
  with open("jo.txt") as file:
    text=file.read()
    print(f"hello{text}")
except Exception:
  with open("jo.txt","w") as file:
    file.write("Guest")