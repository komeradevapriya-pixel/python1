name = input("Enter student name: ")
marks = float(input("Enter aggregate marks: "))
attendance = float(input("Enter attendance: "))
income = float(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 200000:
    print(name, "is Eligible for Scholarship")
else:
    print(name, "is Not Eligible")