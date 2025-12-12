class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def annual_salary(self):
    yearly_salary=self.salary*12
    return yearly_salary
employee1=Employee("kal",7000)
print(f"your annual salary is {employee1.annual_salary()
}")
    