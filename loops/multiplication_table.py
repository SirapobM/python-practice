# แสดงสูตรแม่สูตรคูณของเลขเดียว
num = int(input("ใส่เลขที่ต้องการดูสูตรคูณ : "))
for i in range(1, 13):
    print(num, "x", i, "=", num * i)

# แสดงสูตรคูณจำนวนรอบตามที่ผู้ใช้กำหนด
num = int(input("ใส่เลขที่ต้องการดูสูตรคูณ : "))
count = int(input("ใส่จำนวนที่ต้องการดูรอบสูตรคูณ : "))
for i in range(1, count + 1):
    print(num, "x", i, "=", num * i)

# แสดงสูตรคูณช่วงของตัวเลข
start = int(input("ใส่จุดเริ่มต้น : "))
end = int(input("ใส่จุดสิ้นสุด : "))

for i in range(start, end + 1):
    for j in range(1, 13):
        print(i, "x", j, "=", i * j)
