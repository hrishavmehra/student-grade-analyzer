print("===== STUDENT GRADE ANALYZER =====")

name = input("Enter student name: ")

subjects = ["Python", "DSA", "DBMS", "Maths", "Data Science"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = "PASS" if percentage >= 40 else "FAIL"

print("\n===== RESULT =====")
print("Student:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
print("==================")