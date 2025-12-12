class Car:
  def __init__(self,make):
    self.make=make
  def get_make(self):
    return self.make
car1=Car("toyota")
print(car1.get_make())