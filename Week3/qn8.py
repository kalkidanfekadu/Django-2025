class Animal:
  def make_sound():
    print("make sound")
class Cat(Animal):
  def make_sound():
    print("Meow!")
a1=Animal()
c1=Animal()
a1.make_sound()
c1.make_sound()