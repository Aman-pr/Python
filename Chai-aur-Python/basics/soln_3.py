#This is solution 3 of question
score = int(input("Enter the student's score: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif score < 60:
    grade = "F"
else:
    grade = "Invalid Score"  

print(f"The student's grade is: {grade}")
