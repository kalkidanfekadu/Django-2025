class Library:
  def __init__(self):
    self.book_list=[]
  def add_book(self,num):
    for i in range(num):
      self.title=input(f"Enter book {i+1} title: ")
      self.book_list.append(self.title)
  def show_book(self):
    for i in range(len(self.book_list)):
      print(f"Book {i+1}: {self.book_list[i]}\n")
L1=Library()
n=int(input("Enter the amount of books you want to add"))
L1.add_book(n)
L1.show_book()
    