with open("log.txt","a") as file:
  file.write("user logged in\n")
with open("log.txt","r") as file:
  content=file.read()
  print(content)