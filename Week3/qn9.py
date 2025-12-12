class Vehicle:
  def __init__(self,brand,year):
    self.brand=brand
    self.year=year
  def info(self):
    print(f"Brand: {self.brand}\n Year: {self.year}")
class Car(Vehicle):
  def __init__(self, brand, year,model):
    super().__init__(brand, year)
    self.model=model
  def info(self):
    super().info()
    print(f"Model: {self.model}")
car=Car("Tesla",2024,"Model 3")
car.info()


  