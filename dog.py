class Dog:
  def bark():
    print("Woof!")
dog1=Dog()
Dog.bark()
class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
width=float(input("enter the width"))
height=float(input("enter the height"))
re1=Rectangle(width,height)
print(f"Area {re1.width*re1.height}")
    
  