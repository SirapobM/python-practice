# -------------------------------------------------
for num in range(0, 6, 2):
    print(num)

for num in range(1, 10):
    if num % 3 == 0:
        continue
    print(num)

# -------------------------------------------------
# โจทย์หาผลรวมตัวเลข 5 จำนวน
total = 0
for i in range(1, 6):
    num = int(input("ใส่ตัวเลข : "))
    total += num
print("ผลรวมของตัวเลขทั้ง 5 ตัว คือ :", total)

# -------------------------------------------------
# รวมตัวเลขไปเรื่อยๆ จนกว่าจะกรอก 0
total = 0
while True:
    number = int(input("ใส่ตัวเลข (0 เพื่อหยุด) : "))
    if number == 0:
        break
    total += number
print("ผลรวมของตัวเลขทั้งหมด คือ :", total)

# -------------------------------------------------
for i in range(2):
    print(i)
    for j in range(3):
        print(j)

# -------------------------------------------------
counter = 0
while counter < 5:
    counter += 1
    print(counter)

