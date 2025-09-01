# Simple grading program
score = int(input("ใส่คะแนนของคุณ: "))
grade = None

if score >= 80 and score <= 100:
    grade = "A"
elif score >= 70 and score <= 79:
    grade = "B"
elif score >= 0 and score <= 69:
    grade = "F"
else:
    grade = "N"

print("Your grade is:", grade)
