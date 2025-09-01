# โปรแกรมตัดเกรดอย่างง่าย
score = int(input("ใส่คะแนนของคุณ : "))
grade = None

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 0 <= score <= 69:
    grade = "F"
else:
    grade = "N"

print("Your grade is:", grade)
