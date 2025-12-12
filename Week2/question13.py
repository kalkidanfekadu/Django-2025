with open("kal.txt","w") as file:
  file.write("hello world")
try:
  with open("kal.txt") as file:
    text=file.read()
    print(text.upper())
except Exception:
  print("file not found")
