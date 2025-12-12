student_grades={"Kalkidan":98,"Enas":95,"Abebe":89,"Meklit":93}
def get_grade(student_name,student_grade):
  try:
    return student_grade[name]
  except Exception:
    return("Student does not found in the system")
name=(input("Enter the name of the student"))
print(get_grade(name,student_grades))