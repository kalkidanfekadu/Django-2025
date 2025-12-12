class Student:
  def set_grade(self,grade):
    self.__grade=grade
  def get_grade(self):
    return self.__grade
student1=Student()
student1.set_grade(3.8)
print(f"Grade {student1.get_grade()}")