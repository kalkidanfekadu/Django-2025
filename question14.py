scores={"John":85,"Sara":92,"Fraol":78}
name=input("enter the student name")
try:
    print(scores[name])
except Exception:
    print("Student does not found in the system")
